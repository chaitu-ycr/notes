---
title: "💓 0x3E: Tester Present"
aliases:
  - "💓 0x3E: Tester Present"
---

# 💓 0x3E: Tester Present

**Purpose:** This is the "keep-alive" heartbeat. When you enter an extended diagnostic session, the ECU will automatically return to default session after ~5 seconds of inactivity. TesterPresent tells the ECU "I'm still here, don't timeout!" It's like wiggling the mouse to prevent your computer from locking.

**When to Use:**
- During long diagnostic procedures
- While performing time-consuming operations
- To maintain extended or programming session

---

## 📝 Request Format

```
[3E] [Sub-function]
```

| Byte | Name | Description |
|------|------|-------------|
| 0 | SID | Service ID: `0x3E` |
| 1 | Sub-function | Response mode (see below) |

### Sub-functions

| Value | Name | Description |
|-------|------|-------------|
| `0x00` | zeroSubFunction | Send positive response |
| `0x80` | zeroSubFunction + suppressPositiveResponse | **Don't** send response (most common) |

**🎯 Pro tip:** Almost everyone uses `3E 80` to avoid flooding the bus with responses.

---

## ✅ Positive Response

```
[7E] [Sub-function]
```

| Byte | Name | Description |
|------|------|-------------|
| 0 | Response SID | `0x7E` (0x3E + 0x40) |
| 1 | Sub-function | Echoes requested sub-function |

**Example (with response):**
```
Request:  3E 00
Response: 7E 00
          ↑  ↑
          |  Confirmed
          Success
```

**Example (suppressed response—most common):**
```
Request:  3E 80
Response: (none—response suppressed)
```

---

## ❌ Negative Response Codes

```
[7F] [3E] [NRC]
```

| NRC | Name | Description | Example Scenario |
|-----|------|-------------|------------------|
| `0x12` | Sub-Function Not Supported | Invalid sub-function | Sending `3E 05` (invalid sub-function) |
| `0x13` | Incorrect Message Length | Wrong byte count | Sending `3E` alone (missing sub-function) |
| `0x22` | Conditions Not Correct | Can't process now | ECU in a state that doesn't allow it |

**Example:**
```
Request:  3E
Response: 7F 3E 13
          ↑  ↑  ↑
          |  |  Incorrect message length
          |  TesterPresent
          Error
```

---

## 💡 Practical Examples

### Example 1: Keep Session Alive During Long Operation

**Scenario:** You're waiting for a routine to complete. Send TesterPresent every 2 seconds.

```
Time 0s:
→ Request:  31 01 [start routine]
← Response: 71 01 ...
            (Routine started, will take 10 seconds)

Time 2s:
→ Request:  3E 80
← Response: (no response—suppressed)

Time 4s:
→ Request:  3E 80
← Response: (no response)

Time 6s:
→ Request:  3E 80
← Response: (no response)

Time 8s:
→ Request:  3E 80
← Response: (no response)

Time 10s:
→ Request:  31 03 [check routine status]
← Response: 71 03 00
            (Routine completed!)
```

### Example 2: Programming Session Maintenance

**Scenario:** During software flashing (which can take minutes).

```
→ Request:  10 02
← Response: 50 02 ...
            (Entered programming session)

(Start background thread: send 3E 80 every 2 seconds)

→ Request:  34 00 11 [start download]
← Response: 74 ...

... (Thread continues sending 3E 80 every 2s) ...

→ Request:  36 [transfer data]
← Response: 76

... (TesterPresent running in background) ...
```

### Example 3: Requesting Response

**Scenario:** Debugging—you want to see that the ECU acknowledged.

```
→ Request:  3E 00
← Response: 7E 00
            (Got confirmation!)
```

---

## 🔧 Pro Tips

- **Timing:** Send every 2-3 seconds. Session timeout is typically 5 seconds, so 2 seconds gives you safety margin.
- **Background task:** Implement TesterPresent as a background thread/timer. Don't interrupt your main diagnostic logic.
- **Suppress response (0x80):** ALWAYS use `3E 80` in production. Why?
  - Reduces bus traffic
  - Avoids response buffer overflow
  - Prevents timing issues
- **Session dependency:** TesterPresent is only needed for non-default sessions (extended, programming, etc.). Default session doesn't timeout.
- **Don't spam:** Sending too frequently (e.g., every 100ms) is unnecessary and wastes bandwidth.

---

## Timing Diagram

```
Default Session: No TesterPresent needed
│
v
Enter Extended Session (10 03)
│
│<─────── 5 second timeout window ────────>│
│         ↑ TesterPresent (3E 80)           │
│         │ sent every 2s                   │
│         ↓                                  │
│         Reset timeout ──┐                  │
│<──────────────────────── 5s window ────────>│
                          ↑
                   Another 3E 80

Without TesterPresent:
│
│<─────── 5 second timeout ────────>│ → Auto-return to Default Session
```

---

## Common Implementation Pattern (Pseudocode)

```python
# Start background thread
def tester_present_thread():
    while in_extended_session:
        send_uds_message([0x3E, 0x80])
        sleep(2.0)  # Wait 2 seconds

# Main diagnostic flow
enter_extended_session()
start_thread(tester_present_thread)

# Do your diagnostic work...
read_dtcs()
clear_dtcs()
flash_software()

# Clean up
in_extended_session = False
exit_session()
```

---

## 🔗 Related Services

- **0x10 DiagnosticSessionControl:** Creates sessions that need TesterPresent
- All services that take time to execute (0x34-0x37 download/upload, 0x31 routines)



