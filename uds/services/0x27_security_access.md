# 🔐 0x27: Security Access

**Purpose:** This is the "password check" service. Some operations (like writing calibration data or flashing software) are dangerous, so the ECU requires proof that you're authorized. It's a challenge-response system: the ECU gives you a random "seed," you transform it using a secret algorithm into a "key," and send it back.

**When to Use:**
- Before writing protected data (calibrations, configuration)
- Before entering programming session
- Before clearing certain fault codes
- Before executing sensitive routines

---

## 📝 Request Format

Security Access is a **two-step process**:

### Step 1: Request Seed

```
[27] [Security Level (odd)]
```

| Byte | Name | Description |
|------|------|-------------|
| 0 | SID | Service ID: `0x27` |
| 1 | Sub-function | Security level (0x01, 0x03, 0x05, ..., odd numbers) |

### Step 2: Send Key

```
[27] [Security Level + 1 (even)] [Key byte 1] [Key byte 2] ...
```

| Byte | Name | Description |
|------|------|-------------|
| 0 | SID | Service ID: `0x27` |
| 1 | Sub-function | Security level + 1 (0x02, 0x04, 0x06, ..., even numbers) |
| 2... | Key | The calculated key (length varies, typically 2-16 bytes) |

### Security Levels

| Level | Description | Typical Use |
|-------|-------------|-------------|
| `0x01/0x02` | Level 1 | Basic protected operations |
| `0x03/0x04` | Level 2 | Programming/flashing |
| `0x05/0x06` | Level 3 | Factory/calibration access |
| `0x07...` | Higher levels | OEM-specific |

---

## ✅ Positive Response

### Response to Seed Request

```
[67] [Security Level] [Seed byte 1] [Seed byte 2] ...
```

| Byte | Name | Description |
|------|------|-------------|
| 0 | Response SID | `0x67` (0x27 + 0x40) |
| 1 | Security Level | Echoes requested level |
| 2... | Seed | Random seed value (typically 2-4 bytes) |

**Special case:** If security is already unlocked for this level, the ECU responds with **zero seed**:
```
67 01 00 00
```
This means "you're already unlocked, no need to send a key."

### Response to Key (Success)

```
[67] [Security Level + 1]
```

| Byte | Name | Description |
|------|------|-------------|
| 0 | Response SID | `0x67` (0x27 + 0x40) |
| 1 | Security Level + 1 | Confirmation of unlock |

**Example: Full Successful Sequence**
```
Step 1 - Request Seed:
→ Request:  27 01
← Response: 67 01 12 34
            ↑  ↑  ↑-----↑
            |  |  Seed: 0x1234
            |  Level 1
            Success

Step 2 - Calculate key from seed (using secret algorithm)
Key = MagicFunction(0x1234) = 0xABCD

Step 3 - Send Key:
→ Request:  27 02 AB CD
← Response: 67 02
            ↑  ↑
            |  Level 1 unlocked!
            Success
```

---

## ❌ Negative Response Codes

```
[7F] [27] [NRC]
```

| NRC | Name | Description | Example Scenario |
|-----|------|-------------|------------------|
| `0x12` | Sub-Function Not Supported | Security level doesn't exist | Requesting level 0x07 when ECU only has 0x01 and 0x03 |
| `0x13` | Incorrect Message Length | Wrong key length | Sending 4-byte key when ECU expects 2 bytes |
| `0x22` | Conditions Not Correct | Can't unlock right now | Trying to unlock while vehicle is moving |
| `0x24` | Request Sequence Error | Wrong step order | Sending key before requesting seed |
| `0x35` | Invalid Key | Wrong key value | Your calculation doesn't match ECU's expectation |
| `0x36` | Exceed Number Of Attempts | Too many wrong keys | Failed 3+ times, ECU locks you out |
| `0x37` | Required Time Delay Not Expired | retry too fast | Must wait 10 seconds after failed attempt |

**Example: Invalid Key**
```
→ Request:  27 01
← Response: 67 01 12 34
            (Seed received: 0x1234)

→ Request:  27 02 99 99
            (Wrong key sent)
← Response: 7F 27 35
            ↑  ↑  ↑
            |  |  Invalid key!
            |  SecurityAccess
            Error
```

**Example: Too Many Attempts**
```
→ Request:  27 02 WR ON G1
← Response: 7F 27 35 (Attempt 1 failed)

→ Request:  27 02 WR ON G2
← Response: 7F 27 35 (Attempt 2 failed)

→ Request:  27 02 WR ON G3
← Response: 7F 27 36
            (Locked out! Too many failed attempts)
```

---

## 💡 Practical Examples

### Example 1: Unlock Before Programming

**Scenario:** You need to flash new software and must unlock Level 2 security.

```
Step 1: Request seed
→ Request:  27 03
← Response: 67 03 AB CD EF 12
            (Seed: 0xABCDEF12)

Step 2: Calculate key offline using OEM algorithm
Key = CalculateKey(0xABCDEF12) = 0x11223344

Step 3: Send key
→ Request:  27 04 11 22 33 44
← Response: 67 04
            (Unlocked! Can now flash software)
```

### Example 2: Already Unlocked

**Scenario:** Requesting seed when already unlocked.

```
→ Request:  27 01
← Response: 67 01 00 00
            (Zero seed = already unlocked, skip step 2)
```

### Example 3: Sequence Error

**Scenario:** Sending key without requesting seed first.

```
→ Request:  27 02 AB CD
← Response: 7F 27 24
            (Error: You must request seed first!)
```

### Example 4: Lockout with Time Delay

**Scenario:** Failed too many times, must wait.

```
→ Request:  27 01
← Response: 7F 27 37
            (Error: Wait 10 seconds before trying again)
            
(Wait 10 seconds...)

→ Request:  27 01
← Response: 67 01 12 34
            (OK, you can try again now)
```

---

## 🔧 Pro Tips

- **Seed-Key algorithms are secret:** Each OEM has proprietary algorithms. You need the official algorithm or a key database to unlock.
- **Implement lockout logic:** After 3-5 failed attempts, most ECUs lock you out for 10-60 seconds (or until ignition cycle).
- **Check if already unlocked:** Always request seed first. If you get zero seed, you're already unlocked and can skip sending the key.
- **Timing matters:** Some ECUs have time limits. If you take too long between seed request and key send, the seed expires.
- **Security state loss:** Security access is lost when:
  - ECU resets
  - Diagnostic session changes
  - Timeout occurs (no TesterPresent)

---

## 🔗 Related Services

- **0x10 DiagnosticSessionControl:** Required before security access
- **0x2E WriteDataByIdentifier:** Often requires security
- **0x34-0x37 Download/Upload:** Programming requires security
- **0x3E TesterPresent:** Keep session alive to maintain security
