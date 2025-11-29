# 🎮 0x31: Routine Control

**Purpose:** This is the "remote control" for ECU self-tests and procedures. It lets you start, stop, and check the results of built-in routines like actuator tests, self-diagnostics, or calibration procedures. Think of it as pressing buttons on the ECU's control panel.

**When to Use:**
- Running actuator tests (e.g., "click the fuel injectors")
- Performing self-diagnostics
- Calibration procedures
- Erasing flash memory (before reprogramming)

---

## 📝 Request Format

```
[31] [Sub-function] [Routine ID MSB] [Routine ID LSB] [Parameters...]
```

| Byte | Name | Description |
|------|------|-------------|
| 0 | SID | Service ID: `0x31` |
| 1 | Sub-function | Action to perform (see below) |
| 2-3 | Routine Identifier | Which routine (2 bytes) |
| 4... | Routine Parameters | Input data (if needed) |

### Sub-functions

| Value | Name | Description |
|-------|------|-------------|
| `0x01` | startRoutine | Begin execution |
| `0x02` | stopRoutine | Halt execution |
| `0x03` | requestRoutineResults | Get results/status |

### Example Routine IDs (Vary by OEM/ECU)

| Routine ID | Name | Description |
|------------|------|-------------|
| `0xFF00` | Erase Memory | Erase flash before programming |
| `0xFF01` | Check Programming Dependencies | Verify conditions before flash |
| `0x0203` | Injector Test | Pulse fuel injectors |
| `0x0250` | Pump Test | Run fuel pump |
| `0xF002` | Read VIN | Alternative VIN reading method |

---

## ✅ Positive Response

```
[71] [Sub-function] [Routine ID MSB] [Routine ID LSB] [Status/Results...]
```

| Byte | Name | Description |
|------|------|-------------|
| 0 | Response SID | `0x71` (0x31 + 0x40) |
| 1 | Sub-function | Echoes requested action |
| 2-3 | Routine Identifier | Echoes routine ID |
| 4... | Routine Status/Results | Output data |

**Example: Start Routine**
```
Request:  31 01 02 03
          ↑  ↑  ↑-----↑
          |  |  Routine ID: 0x0203 (injector test)
          |  Start routine
          RoutineControl

Response: 71 01 02 03 00
          ↑  ↑  ↑-----↑ ↑
          |  |  Routine |  Status: 0x00 = Started successfully
          |  |  ID      
          |  Start
          Success
```

**Example: Request Results**
```
Request:  31 03 02 03
          (Check status of injector test)

Response: 71 03 02 03 01 [result data]
          ↑  ↑  ↑-----↑ ↑  ↑-------------↑
          |  |    ID   |  Result bytes
          |  |         Status: 0x01 = Completed
          |  Request results
          Success
```

---

## ❌ Negative Response Codes

```
[7F] [31] [NRC]
```

| NRC | Name | Description | Example Scenario |
|-----|------|-------------|------------------|
| `0x12` | Sub-Function Not Supported | Invalid sub-function | Using sub-function 0x05 |
| `0x13` | Incorrect Message Length | Wrong parameter count | Missing required parameters |
| `0x22` | Conditions Not Correct | Preconditions not met | Engine must be off for this routine |
| `0x24` | Request Sequence Error | Wrong order | Trying to get results before starting |
| `0x31` | Request Out Of Range | Routine doesn't exist | Invalid routine ID |
| `0x33` | Security Access Denied | Not unlocked | Routine requires security |
| `0x72` | General Programming Failure | Routine execution failed | Erase failed due to hardware issue |

**Example:**
```
Request:  31 01 FF FF
Response: 7F 31 31
          ↑  ↑  ↑
          |  |  Request out of range (routine doesn't exist)
          |  RoutineControl
          Error
```

---

## 💡 Practical Examples

### Example 1: Run Actuator Test (Fuel Injectors)

**Scenario:** Testing if injectors are working.

```
Step 1: Start the test
→ Request:  31 01 02 03
← Response: 71 01 02 03 00
            (Routine started, injectors clicking!)

Step 2: Check if test completed
→ Request:  31 03 02 03
← Response: 71 03 02 03 01 00
            (Completed successfully, result = 0x00 = PASS)
```

### Example 2: Erase Flash Memory (Before Programming)

**Scenario:** Preparing ECU for software update.

```
Step 1: Enter programming session & unlock
→ Request:  10 02
← Response: 50 02 ...

→ Request:  27 03
← Response: 67 03 [seed]
→ Request:  27 04 [key]
← Response: 67 04

Step 2: Start erase routine
→ Request:  31 01 FF 00
← Response: 71 01 FF 00 00
            (Erase started... takes 10-30 seconds)

Step 3: Check erase status (while sending 3E 80 keep-alive)
→ Request:  31 03 FF 00
← Response: 71 03 FF 00 01
            (Still in progress, status = 0x01)

... wait ...

→ Request:  31 03 FF 00
← Response: 71 03 FF 00 00
            (Completed! Status = 0x00 = Success)
```

### Example 3: Stop a Running Routine

**Scenario:** Aborting a long-running test.

```
→ Request:  31 01 12 34
← Response: 71 01 12 34 00
            (Routine started)

... User cancels...

→ Request:  31 02 12 34
← Response: 71 02 12 34
            (Routine stopped)
```

### Example 4: Conditions Not Met

**Scenario:** Trying to run a routine with engine on.

```
→ Request:  31 01 02 50
← Response: 7F 31 22
            (Error: Turn engine off first!)
```

---

## 🔧 Pro Tips

- **Routine results format:** Each routine has its own result format. Always check the spec!
- **Long-running routines:** Some routines take time (erase flash = 30s). Use TesterPresent (0x3E) to keep session alive while polling results with sub-function 0x03.
- **Status byte interpretation:**
  - `0x00` = Completed successfully
  - `0x01` = In progress
  - `0x02` = Failed
  - (Varies by routine—check spec!)
- **Security often required:** Dangerous routines (erase flash, actuator tests) typically require unlocking first.
- **Session requirements:** Most routines need extended or programming session.

---

## Common Routine Control Flow

```
1. Enter appropriate session (0x10)
2. Unlock security if needed (0x27)
3. Start routine (0x31 01 [ID])
4. Poll for results (0x31 03 [ID]) while sending TesterPresent
5. Verify success
6. (Optional) Stop if needed (0x31 02 [ID])
```

---

## 🔗 Related Services

- **0x10 DiagnosticSessionControl:** Often need extended/programming session
- **0x27 SecurityAccess:** Usually required for routines
- **0x3E TesterPresent:** Keep session alive during long routines
- **0x22 ReadDataByIdentifier:** Read related data before/after
