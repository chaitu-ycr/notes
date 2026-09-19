---
title: "🎛️ 0x85: Control DTC Setting"
aliases:
  - "🎛️ 0x85: Control DTC Setting"
---

# 🎛️ 0x85: Control DTC Setting

**Purpose:** Turn fault code recording ON or OFF. This is useful during testing—you don't want temporary test faults cluttering up the fault memory. It's like muting the check engine light during diagnostics.

**When to Use:**
- During actuator testing (prevent false DTCs)
- Manufacturing/EOL testing
- Calibration procedures

---

## 📝 Request Format

```
[85] [Sub-function] [DTCSettingControlOptionRecord]
```

| Byte | Name | Description |
|------|------|-------------|
| 0 | SID | Service ID: `0x85` |
| 1 | Sub-function | ON/OFF (see below) |
| 2... | Option Record | Optional DTC group filter |

### Sub-functions

| Value | Name | Description |
|-------|------|-------------|
| `0x01` | ON | Enable DTC recording (default state) |
| `0x02` | OFF | Disable DTC recording |

**Most common:**
```
85 02
(Turn OFF DTCrecording)
```

---

## ✅ Positive Response

```
[C5] [Sub-function]
```

**Example:**
```
Request:  85 02
Response: C5 02
          Success! DTC recording disabled.
```

---

## ❌ Negative Response Codes

| NRC | Name | Description |
|-----|------|-------------|
| `0x12` | Sub-Function Not Supported | Invalid sub-function |
| `0x22` | Conditions Not Correct | Can't change now |
| `0x31` | Request Out Of Range | Invalid DTC group |

---

## 💡 Practical Example

```
Scenario: Testing fuel injectors without triggering DTCs

Step 1: Disable DTC recording
→ 85 02
← C5 02

Step 2: Run actuator test
→ 31 01 02 03 (Start injector test)
← 71 01 02 03

(Injectors click, but no DTCs stored!)

Step 3: Re-enable DTC recording
→ 85 01
← C5 01
```

---

## 🔧 Pro Tips

- **Always re-enable!** Don't leave DTC recording disabled—you'll miss real faults!
- **Session timeout:** DTC recording auto-enables when session ends
- **Not all DTCs:** Safety-critical DTCs may ignore this command

---

## 🔗 Related Services

- **0x19 ReadDTCInformation:** Read DTCs
- **0x14 ClearDiagnosticInformation:** Clear DTCs
- **0x31 RoutineControl:** Often used together



