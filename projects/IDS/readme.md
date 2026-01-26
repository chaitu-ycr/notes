# IDS - Intrusion Detection System

🚨 **Hook**: In automotive systems, an IDS is the guard dog watching the vehicle network — it must be fast, explainable, and never false-trigger the brakes.

---

## 📋 Table of Contents
1. [What is an IDS?](#what-is-an-ids)
2. [Tester Quickstart (10 min)](#tester-quickstart--10-min)
3. [Key Concepts](#key-concepts)
4. [Detection Approaches](#detection-approaches)
5. [Test Strategies & Recipes](#test-strategies--recipes)
6. [Metrics & Quality](#metrics--quality)
7. [Deployment & Ops](#deployment--ops)
8. [Common Pitfalls & Warnings](#common-pitfalls--warnings)

---

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

---

## Tester Quickstart (10 min)

### Prerequisites
- Python 3.8+
- Basic CAN/UDS familiarity (if unsure, [CAN docs](../can/readme.md) cover it)
- A text editor and terminal

### Run the Minimal Example

**Step 1:** Save this code as `ids_minimal.py`:

```python
# Minimal IDS simulation: rule-based CAN frame checker
import time

class CANFrame:
    def __init__(self, arbitration_id, data):
        self.id = arbitration_id
        self.data = data

def is_suspicious(frame):
    # Simple rule: repeated toggling of a bit in a control ID
    if frame.id == 0x200 and frame.data == b"\x00\xFF":
        return True
    return False

def simulate_bus(frames, detector):
    for f in frames:
        if detector(f):
            print(f"ALERT: suspicious frame id=0x{f.id:X} data={f.data}")
        time.sleep(0.01)

if __name__ == '__main__':
    frames = [CANFrame(0x100, b"\x01\x02"), CANFrame(0x200, b"\x00\xFF"), CANFrame(0x200, b"\x00\xFF")]
    simulate_bus(frames, is_suspicious)
```

**Step 2:** Run:

```bash
python3 ids_minimal.py
```

**Step 3:** You should see:
```
ALERT: suspicious frame id=0x200 data=b'\x00\xff'
ALERT: suspicious frame id=0x200 data=b'\x00\xff'
```

✅ You just ran your first IDS detector. Congratulations!

---

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

---

## Detection Approaches

### 1. **Rule / Signature-Based** (Simple, Explainable)
- Check for illegal IDs, invalid sequences, impossible states
- Example: "ECU X never sends at >100 Hz; if it does, alert"
- **Pros**: Deterministic, explainable, cheap
- **Cons**: Manual tuning per vehicle variant

### 2. **Statistical / Anomaly** (Lightweight)
- Track frequency histograms, inter-frame timing variance
- Example: "ID 0x123 usually arrives every 20 ms ±2 ms; flag if jitter >5 ms"
- **Pros**: Catches gradual drift, works on-device
- **Cons**: Needs baseline calibration

### 3. **Machine Learning** (Sophisticated)
- Autoencoder or 1D-CNN for complex patterns
- **Pros**: Detects subtle, multi-dimensional attacks
- **Cons**: Model drift, retraining overhead, explainability challenges

### 4. **Hybrid** (Best Practice)
- Rules for high-confidence events (illegal ID)
- Anomaly for marginal deviations (timing jitter)
- ML for nuanced patterns (sequence anomalies)
- Combine with confidence scoring

### Data Sources Available
- Raw CAN/FlexRay/Ethernet frames
- Diagnostic (UDS) requests/responses
- ECU state telemetry (CPU, memory, task timing)
- Gateway correlation (cross-bus timing)

---

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

---

### Recipe 2: SIL Replay Test

**Goal**: Validate detector on recorded trace
**Steps**:
1. Export your CAN log to CSV (id, data, timestamp)
2. Load and replay with the harness snippet below
3. Capture alerts to file
4. Compare expected vs. observed

**Example CSV**:
```
id,data,timestamp
0x100,010203,0.0
0x200,00FF,0.01
0x200,00FF,0.02
```

**Harness**:
```python
import csv, time

class CANFrame:
    def __init__(self, arbitration_id, data):
        self.id = int(arbitration_id, 0)
        self.data = bytes.fromhex(data)

def load_csv(path):
    frames = []
    with open(path, newline='') as f:
        r = csv.DictReader(f)
        for row in r:
            frames.append(CANFrame(row['id'], row['data']))
    return frames

def replay(frames, detector, delay=0.01):
    alerts = []
    for f in frames:
        if detector(f):
            alerts.append(f"id=0x{f.id:X} data={f.data.hex()}")
    return alerts

# Usage:
# frames = load_csv('trace.csv')
# alerts = replay(frames, is_suspicious)
# print(f"Detected {len(alerts)} alerts")
```

**Expected**: Reproduce known incidents with high fidelity

---

### Recipe 3: Rate-Burst (DoS) Test

**Goal**: Validate behavior under bus overload
**Steps**:
1. Generate synthetic high-rate frame stream (>10x normal)
2. Replay for 1–5 seconds
3. Monitor CPU, memory, and alert generation
4. Document graceful degradation behavior

**Expected**: IDS must not crash; behavior under overload must be predictable

---

### Recipe 4: Replay & Arbitration Attack

**Goal**: Test multi-ID coordinated attacks
**Steps**:
1. Craft sequences that exercise CAN arbitration (high ID priority vs. low)
2. Inject messages in rapid succession to test priority inversion
3. Verify detection of impossible state sequences

**Expected**: Detection of out-of-spec timing or impossible sequences

---

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

---

## Deployment & Ops

### Deployment Modes

- **Passive Monitoring**: IDS only logs, no mitigation. Safe, non-intrusive.
- **Active Mitigation**: IDS triggers safety responses (e.g., gateway disconnects). Requires safety case (ISO 26262).

### Over-the-Air (OTA) Updates

- **Sign & Version**: All IDS models/rules must be signed and versioned
- **Rollback**: Support fallback to previous version if new rules cause high FPR
- **A/B Updates**: Test on subset of fleet before fleet-wide rollout
- **Monitoring**: Track alert rates post-update for drift detection

### Logging & Forensics

- **On-Device**: Store compressed event summaries (<1 MB per hour)
- **Off-Board**: Extended logs uploaded when vehicle is idle/charging
- **Integrity**: Sign logs with vehicle key to prevent tampering
- **Retention**: Keep 7–30 days depending on storage budget

### Forensic Workflow

1. Keep immutable alert trail with timestamps and correlated frames
2. Provide tools to reconstruct sequence-of-events across ECUs
3. Prioritize alerts: safety-critical > functional > informational
4. Link alerts to known attack patterns or anomalies for faster response

---

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

---

## Quick Reference: Test Checklist

- [ ] Design: threat model, detection boundary, safety requirements defined
- [ ] Implementation: rule engine, feature extractor, model (if ML) complete
- [ ] Unit Tests: 100% coverage of detection rules
- [ ] SIL Tests: replay recorded traces, validate alerts
- [ ] HIL Tests: measure latency, CPU, memory, jitter
- [ ] Fuzzing: randomize IDs, payloads, timings to find blind spots
- [ ] Adversarial: inject known attacks, verify detection
- [ ] Regression: test after firmware/ECU updates
- [ ] Deployment: signed rules/models, rollback plan, monitoring dashboards
- [ ] Documentation: test report, root cause analysis, lessons learned

---
