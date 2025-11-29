# 🚪 0x10: Diagnostic Session Control

**Purpose:** Think of this as "opening different doors" in the ECU. Each diagnostic session unlocks different capabilities. Default session is like the lobby—you can look around but not touch much. Extended session is like having a key card to restricted areas.

**When to Use:** 
- Start of any diagnostic session
- Before performing protected operations (flashing, writing configuration)
- When you need access to advanced diagnostics

---

## 📝 Request Format

```
[10] [Sub-function]
```

| Byte | Name | Description |
|------|------|-------------|
| 0 | SID | Service ID: `0x10` |
| 1 | Sub-function | Session type (see table below) |

### Sub-functions

| Value | Session Type | Description |
|-------|--------------|-------------|
| `0x01` | Default Session | Normal operation mode, limited diagnostics |
| `0x02` | Programming Session | For ECU reprogramming/flashing |
| `0x03` | Extended Diagnostic Session | Full diagnostic access |
| `0x04` | Safety System Diagnostic Session | For safety-critical systems |
| `0x40-0x5F` | OEM-specific | Manufacturer-defined sessions |

---

## ✅ Positive Response

```
[50] [Sub-function] [P2ServerMax MSB] [P2ServerMax LSB] [P2*ServerMax MSB] [P2*ServerMax LSB]
```

| Byte | Name | Description |
|------|------|-------------|
| 0 | Response SID | `0x50` (0x10 + 0x40) |
| 1 | Sub-function | Echoes requested session type |
| 2-3 | P2ServerMax | Default P2 timing (ms) - how long tester waits for response |
| 4-5 | P2*ServerMax | Enhanced P2 timing (ms) - extended wait time |

**Example:**
```
Request:  10 03
Response: 50 03 00 32 0A 00
          ↑  ↑  ↑-----↑ ↑-----↑
          |  |     |       Enhanced P2: 2560ms (0x0A00)
          |  |     Default P2: 50ms (0x0032)
          |  Extended session confirmed
          Positive response SID
```

---

## ❌ Negative Response Codes

```
[7F] [10] [NRC]
```

| NRC | Name | Description | Example Scenario |
|-----|------|-------------|------------------|
| `0x12` | Sub-Function Not Supported | Requested session doesn't exist | Requesting session 0x05 when ECU only supports 0x01-0x03 |
| `0x13` | Incorrect Message Length | Wrong number of bytes | Sending `10 03 00` (extra byte) |
| `0x22` | Conditions Not Correct | Preconditions not met | Trying to enter programming session while car is moving |
| `0x33` | Security Access Denied | Security not unlocked | Attempting programming session without security access |

**Example:**
```
Request:  10 05
Response: 7F 10 12
          ↑  ↑  ↑
          |  |  Sub-function not supported
          |  Service ID that failed
          Negative response marker
```

---

## 💡 Practical Examples

### Example 1: Enter Extended Diagnostic Session

**Scenario:** You want to clear fault codes, which requires extended session.

```
→ Request:  10 03
← Response: 50 03 00 32 0A 00
            (Success! Extended session active)
```

### Example 2: Enter Programming Session (with timing info)

**Scenario:** Preparing to flash new software.

```
→ Request:  10 02
← Response: 50 02 00 64 13 88
            ↑  ↑  ↑-----↑ ↑-----↑
            |  |     |       P2*: 5000ms (enough time for flash operations)
            |  |     P2: 100ms (normal timeout)
            |  Programming session
            Success
```

### Example 3: Session Not Supported

**Scenario:** Trying to access a session the ECU doesn't have.

```
→ Request:  10 06
← Response: 7F 10 12
            (Error: Sub-function not supported)
```

### Example 4: Conditions Not Met

**Scenario:** Trying to enter programming session while vehicle speed > 0.

```
→ Request:  10 02
← Response: 7F 10 22
            (Error: Car must be stationary!)
```

---

## 🔧 Pro Tips

- **Default session timeout:** Most ECUs automatically return to default session after a period of inactivity (usually 5 seconds without a TesterPresent message).
- **Session dependency:** Some services are only available in specific sessions. Always check which session you're in!
- **Timing parameters:** The P2 and P2* values tell you how long to wait for responses. P2* is used when the ECU sends a "pending" response (0x78 NRC) indicating it needs more time.

---

## 🔗 Related Services

- **0x3E TesterPresent:** Keep session active
- **0x27 SecurityAccess:** Required before accessing programming session
- **0x11 ECUReset:** Often used after programming session
