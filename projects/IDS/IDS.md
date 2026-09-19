---
title: "IDS - Intrusion Detection System"
aliases:
  - "IDS - Intrusion Detection System"
---
# IDS - Intrusion Detection System

🚨 **Hook**: In automotive systems, an IDS is the guard dog watching the vehicle network — it must be fast, explainable, and never false-trigger the brakes.

## 🔗 Related topics

- [CAN](../../can/can.md) — the primary vehicle network monitored for traffic anomalies
- [UDS](../../uds/uds.md) — diagnostic traffic is a key security and abuse surface
- [DoIP](../../doip/doip.md) — Ethernet-based diagnostics and gateway routing that may also need monitoring
- [Vector CANoe](../../vector_canoe/vector_canoe.md) — a common environment for replaying and validating attack scenarios
- [Testing](../../testing/testing.md) — IDS evaluation relies on adversarial and regression test strategies

## What is an IDS?

An **Intrusion Detection System** monitors vehicle networks (CAN, Ethernet, diagnostics) to identify anomalous or malicious behavior. It does NOT take control actions; instead, it alerts and logs suspicious activity for safe mitigation.

### Key Responsibilities
- Detect compromised ECUs or gateway attacks
- Flag unusual message frequencies, payloads, or timings
- Provide forensic data for incident investigation
- Never interfere with safety-critical functions

### Design Constraints (Reality Check)
- **Limited Resources**: Many ECUs have <100 MB RAM, no floating-point hardware
- **Real-Time**: Detection latency must be <100 ms for relevance
- **Safety-First**: IDS failures must not cascade into actuator failures
- **Privacy**: On-device detection preferable to centralized logging

## Key Concepts

### Architecture Considerations

| Aspect | Per-ECU IDS | Gateway IDS | Hybrid |
|--------|-----------|-----------|--------|
| **Detection Speed** | Fast (local) | Slower (centralized) | Balanced |
| **Coverage** | Single ECU patterns | Cross-bus correlation | Best |
| **Resource Cost** | High (per ECU) | Low (centralized) | Medium |
| **Privacy** | High | Low (central logging) | Medium |

### Threat Model (Start Here)
Define these for your system:
- **Assets**: Which functions are critical? (brakes, steering, gateway, diagnostics)
- **Attack Surface**: CAN, LIN, Ethernet, UDS port, Bluetooth, OTA channel?
- **Attacker Capability**: One message? Sustained flood? Coordinated multi-ECU?
- **Detection Boundary**: Per-ECU vs. gateway? Real-time vs. post-incident?

### Resource Constraints
- Many ECUs: 32-bit ARM, <100 MB RAM, <20% CPU headroom for IDS
- Favor: integer arithmetic, small lookup tables, fixed-size buffers
- Avoid: floating-point, ML models >1 MB, dynamic memory

### Safety Integration
- IDS must NOT initiate safety actions (no brake trigger, no steering intervention)
- IDS alerts inform the safety system, which decides response
- Ensure ISO 26262 alignment if detection influences safety decisions

## Test Strategies & Recipes

### Testing Pyramid

```
             ╔════════════════════╗
             ║   Adversarial /    ║  Expensive, realistic
             ║   Attack Replay    ║
             ╠════════════════════╣
             ║  HIL (Hardware)    ║  Resource-intensive
             ║  + Fuzzing         ║
             ╠════════════════════╣
             ║   SIL (Logs +      ║  Moderate cost
             ║   Synthetic)       ║
             ╠════════════════════╣
             ║   Unit Tests       ║  Fast, deterministic
             ╚════════════════════╝
```

### Recipe 1: Unit Rule Test

**Goal**: Verify rule triggers correctly for edge cases
**Steps**:
```python
def test_is_suspicious():
    # Normal frame — should not alert
    assert not is_suspicious(CANFrame(0x100, b"\x01\x02"))
    # Suspicious frame — should alert
    assert is_suspicious(CANFrame(0x200, b"\x00\xFF"))
    # Boundary: just below threshold — should not alert
    assert not is_suspicious(CANFrame(0x200, b"\x00\xFE"))
```
**Expected**: Deterministic pass/fail; no timing dependencies
**Tools**: pytest, unittest

### Recipe 3: Rate-Burst (DoS) Test

**Goal**: Validate behavior under bus overload
**Steps**:
1. Generate synthetic high-rate frame stream (>10x normal)
2. Replay for 1–5 seconds
3. Monitor CPU, memory, and alert generation
4. Document graceful degradation behavior

**Expected**: IDS must not crash; behavior under overload must be predictable

## Metrics & Quality

### Track These During Testing

| Metric | Definition | Target |
|--------|-----------|--------|
| **Detection Rate (Recall)** | % of known attacks detected | >95% |
| **False Positive Rate (FPR)** | Benign frames incorrectly flagged | <0.1% |
| **Latency (P99)** | Time from frame arrival to alert | <100 ms |
| **CPU Impact** | IDS overhead on ECU baseline | <5% |
| **Memory Peak** | Worst-case RAM during operation | <10 MB |
| **WCET** | Worst-case execution time per frame | <1 ms |
| **Explainability** | Can you trace alert to signal? | 100% |

### How to Log & Triage

| Timestamp | Alert ID | Detector Reason | Offending Frame | ECU State |
|-----------|----------|-----------------|-----------------|-----------|
| 2026-01-26T10:30:45.123Z | RATE_BURST_0x300 | freq > 100 Hz | 0x300 [00FF] | CPU: 45% / RAM: 8MB |


**Triage Approach**:
1. Sort by severity (safety > functional > info)
2. Reproduce with SIL traces
3. Annotate root cause (ID, timing pattern, payload)
4. Assign to development or close as expected

## Common Pitfalls & Warnings

### ⚠️ False Positives Are Your Enemy
- High FPR destroys user trust and fleet credibility
- Tune thresholds per vehicle variant and ECU
- Example: "Vehicle is offline for 2 weeks; don't trigger on first frame"

### ⚠️ ML Model Drift
- Retraining cadence: monthly or quarterly (establish baseline first)
- OTA safeguards: always allow fallback to rule-based detector
- Version control: store model training data and code

### ⚠️ Time Synchronization Mismatch
- Timing-based detection breaks if clocks are unsynced
- Require robust timebase (GPS, PTP, or gateway time)
- Test with intentional clock skew

### ⚠️ Resource Exhaustion Under Attack
- A flood of high-rate frames can starve detection
- Plan for graceful degradation (drop oldest alerts, summarize, etc.)
- Document this behavior in safety case



