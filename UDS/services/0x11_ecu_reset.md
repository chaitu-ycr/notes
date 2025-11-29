# 🔄 0x11: ECU Reset

**Purpose:** Turn it off and on again—the universal fix! This service reboots the ECU, like hitting Ctrl+Alt+Delete on your computer. Different reset types give you control over what happens during the reboot.

**When to Use:**
- After flashing new software (to activate it)
- To clear temporary states or errors
- When ECU gets stuck in a diagnostic session

---

## 📝 Request Format

```
[11] [Sub-function]
```

| Byte | Name | Description |
|------|------|-------------|
| 0 | SID | Service ID: `0x11` |
| 1 | Sub-function | Reset type (see table below) |

### Sub-functions

| Value | Reset Type | Description |
|-------|------------|-------------|
| `0x01` | Hard Reset | Power cycle—brutal restart, clears everything |
| `0x02` | Key Off/On Reset | Simulates ignition off/on |
| `0x03` | Soft Reset | Gentle restart, preserves some states |
| `0x04` | Enable Rapid Power Shutdown | Prepare for fast shutdown |
| `0x05` | Disable Rapid Power Shutdown | Revert to normal shutdown |

---

## ✅ Positive Response

```
[51] [Sub-function]
```

| Byte | Name | Description |
|------|------|-------------|
| 0 | Response SID | `0x51` (0x11 + 0x40) |
| 1 | Sub-function | Echoes requested reset type |

**Example:**
```
Request:  11 01
Response: 51 01
          ↑  ↑
          |  Hard reset confirmed
          Positive response SID
```

**⚠️ Note:** In most cases, the ECU resets so fast you might NOT receive a response! The connection will drop as the ECU reboots.

---

## ❌ Negative Response Codes

```
[7F] [11] [NRC]
```

| NRC | Name | Description | Example Scenario |
|-----|------|-------------|------------------|
| `0x12` | Sub-Function Not Supported | Reset type not available | Requesting soft reset when ECU only supports hard reset |
| `0x13` | Incorrect Message Length | Wrong number of bytes | Sending `11 01 00` (extra byte) |
| `0x22` | Conditions Not Correct | Preconditions not met | Trying to reset while vehicle is moving |
| `0x33` | Security Access Denied | Security not unlocked | Reset requires security access first |

**Example:**
```
Request:  11 05
Response: 7F 11 12
          ↑  ↑  ↑
          |  |  Sub-function not supported
          |  ECU Reset service
          Negative response
```

---

## 💡 Practical Examples

### Example 1: Hard Reset After Flashing

**Scenario:** You just flashed new firmware and need to activate it.

```
→ Request:  11 01
← Response: (Connection lost—ECU is rebooting)
   (Wait 2-5 seconds, then reconnect)
```

### Example 2: Soft Reset for State Clearing

**Scenario:** ECU is stuck in a diagnostic state, but you don't want to lose configuration.

```
→ Request:  11 03
← Response: 51 03
            (Success! ECU performs soft reset)
```

### Example 3: Reset Type Not Supported

**Scenario:** Requesting a reset type the ECU doesn't implement.

```
→ Request:  11 06
← Response: 7F 11 12
            (Error: This reset type doesn't exist here)
```

### Example 4: Conditions Not Met

**Scenario:** Trying to reset while conditions are unsafe.

```
→ Request:  11 01
← Response: 7F 11 22
            (Error: Can't reset right now—maybe car is in drive?)
```

---

## 🔧 Pro Tips

- **Expect disconnection:** After a hard reset, the ECU reboots immediately. Your diagnostic tool will lose connection—this is normal!
- **Wait time:** After reset, wait 2-5 seconds before trying to reconnect. The ECU needs time to boot up.
- **Session loss:** After reset, the ECU returns to default diagnostic session. You'll need to re-enter extended session if needed.
- **Security state:** Security access is lost after reset. You'll need to unlock again via 0x27.

---

## 🔗 Related Services

- **0x10 DiagnosticSessionControl:** Used before/after reset
- **0x27 SecurityAccess:** May be required before reset
- **0x34-0x37 Download/Upload:** Typically followed by a reset
