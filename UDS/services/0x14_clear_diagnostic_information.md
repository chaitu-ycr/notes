# 🧹 0x14: Clear Diagnostic Information

**Purpose:** The "reset" button for fault memory. This service clears all stored DTCs (Diagnostic Trouble Codes) and associated data like freeze frames and test results. It's like a clean slate for diagnostics.

**When to Use:**
- After fixing a problem (to verify the fix worked)
- Before performing diagnostic tests (to isolate new faults)
- As part of maintenance procedures

⚠️ **Warning:** Clearing DTCs erases valuable diagnostic history. Only do this after you've recorded necessary information!

---

## 📝 Request Format

```
[14] [Group Of DTC High] [Group Of DTC Mid] [Group Of DTC Low]
```

| Byte | Name | Description |
|------|------|-------------|
| 0 | SID | Service ID: `0x14` |
| 1-3 | Group Of DTC | Which DTCs to clear (3 bytes) |

### DTC Group Values

| Value | Meaning |
|-------|---------|
| `0xFFFFFF` | Clear ALL DTCs (most common) |
| `0xXXXXXX` | Clear specific DTC group (rarely used) |

**Most common usage:** `14 FF FF FF` (clear everything)

---

## ✅ Positive Response

```
[54]
```

| Byte | Name | Description |
|------|------|-------------|
| 0 | Response SID | `0x54` (0x14 + 0x40) |

**Example:**
```
Request:  14 FF FF FF
Response: 54
          ↑
          Success! All DTCs cleared.
```

**That's it!** The simplest positive response in UDS—just one byte.

---

## ❌ Negative Response Codes

```
[7F] [14] [NRC]
```

| NRC | Name | Description | Example Scenario |
|-----|------|-------------|------------------|
| `0x13` | Incorrect Message Length | Wrong byte count | Sending `14 FF FF` (missing one byte) |
| `0x22` | Conditions Not Correct | Can't clear now | Engine running, ECU requires engine off |
| `0x31` | Request Out Of Range | Invalid DTC group | Requesting to clear non-existent DTC group |
| `0x33` | Security Access Denied | Not unlocked | Some ECUs require security access to clear |

**Example:**
```
Request:  14 FF FF FF
Response: 7F 14 22
          ↑  ↑  ↑
          |  |  Conditions not correct (maybe engine is running?)
          |  ClearDiagnosticInformation
          Error
```

---

## 💡 Practical Examples

### Example 1: Clear All DTCs (Standard Procedure)

**Scenario:** You fixed an O2 sensor issue and want to verify the fix by clearing codes.

```
→ Request:  14 FF FF FF
← Response: 54
            (Success! All fault codes cleared)

Then verify:
→ Request:  19 02 09
            (Read DTCs again to confirm)
← Response: 59 02 FF
            (No DTCs returned—memory is clean!)
```

### Example 2: Can't Clear (Engine Running)

**Scenario:** Some ECUs require engine off before clearing.

```
→ Request:  14 FF FF FF
← Response: 7F 14 22
            (Error: Turn engine off first!)

(Turn off engine)

→ Request:  14 FF FF FF
← Response: 54
            (Now it works!)
```

### Example 3: Security Required

**Scenario:** ECU requires unlocking before clearing DTCs.

```
→ Request:  14 FF FF FF
← Response: 7F 14 33
            (Error: Security access required!)

(Perform security access sequence 0x27)

→ Request:  14 FF FF FF
← Response: 54
            (Success after unlocking)
```

### Example 4: Wrong Message Length

**Scenario:** Forgot a byte in the request.

```
→ Request:  14 FF FF
← Response: 7F 14 13
            (Error: Must be exactly 4 bytes: 14 FF FF FF)
```

---

## 🔧 Pro Tips

- **Document first!** Always read and save DTCs (and freeze frames!) BEFORE clearing. You might need that diagnostic history later.
- **Verify the clear:** After clearing, read DTCs again (`19 02 09`) to confirm they're gone.
- **What gets cleared:**
  - ✅ All stored DTCs
  - ✅ Freeze frame data (snapshots)
  - ✅ Test results
  - ✅ Pending DTCs
  - ❌ **NOT cleared:** Permanent DTCs (some emissions-related faults can only be cleared by the ECU after successful test cycles)
- **Readiness monitors reset:** After clearing, emission readiness monitors go to "not ready" status. The car needs to drive through specific test cycles to reset them.
- **MIL (Check Engine Light):** Will turn off immediately after clearing (if no new faults occur).

---

## What Happens After Clearing?

1. **Immediate:**
   - All DTCs erased from memory
   - Check engine light (MIL) turns off
   - Freeze frames deleted
   
2. **Next drive cycle:**
   - ECU runs diagnostic tests again
   - If fault is still present, DTC will come back
   - This is how you verify a repair worked!

---

## 🔗 Related Services

- **0x19 ReadDTCInformation:** Read DTCs before clearing
- **0x85 ControlDTCSetting:** Disable DTC storage during testing
- **0x10 DiagnosticSessionControl:** May need extended session to clear
- **0x27 SecurityAccess:** May be required before clearing
