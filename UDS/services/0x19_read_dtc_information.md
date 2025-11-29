# 🚨 0x19: Read DTC Information

**Purpose:** This is your "check engine light decoder." DTCs (Diagnostic Trouble Codes) are the breadcrumbs the ECU leaves when something goes wrong. This service lets you read what faults are stored, when they occurred, and their status.

**When to Use:**
- Reading fault codes (check engine light is on)
- Getting snapshot data (freeze frame) from when a fault occurred
- Checking fault history
- Monitoring fault status during testing

---

## 📝 Request Format

```
[19] [Sub-function] [Parameters...]
```

| Byte | Name | Description |
|------|------|-------------|
| 0 | SID | Service ID: `0x19` |
| 1 | Sub-function | Which DTC info to read (see table below) |
| 2... | Parameters | Varies by sub-function |

### Sub-functions (Most Common)

| Value | Name | Description | Parameters |
|-------|------|-------------|------------|
| `0x01` | reportNumberOfDTCByStatusMask | Count of DTCs matching status | Status mask (1 byte) |
| `0x02` | reportDTCByStatusMask | List DTCs matching status | Status mask (1 byte) |
| `0x03` | reportDTCSnapshotIdentification | Get snapshot availability | None |
| `0x04` | reportDTCSnapshotRecordByDTCNumber | Read snapshot for specific DTC | DTC (3 bytes), Snapshot # (1 byte) |
| `0x06` | reportDTCExtendedDataRecordByDTCNumber | Read extended data | DTC (3 bytes), Record # (1 byte) |
| `0x0A` | reportSupportedDTCs | List all DTCs ECU can report | None |

### DTC Status Mask

The status mask is a bitmask that filters DTCs:

| Bit | Meaning |
|-----|---------|
| Bit 0 | Test failed |
| Bit 1 | Test failed this operation cycle |
| Bit 2 | Pending DTC |
| Bit 3 | Confirmed DTC |
| Bit 4 | Test not completed since last clear |
| Bit 5 | Test failed since last clear |
| Bit 6 | Test not completed this operation cycle |
| Bit 7 | Warning indicator requested |

**Common masks:**
- `0x09` = Confirmed and test-failed DTCs (typical for "active" faults)
- `0xFF` = All DTCs regardless of status

---

## ✅ Positive Response

### Sub-function 0x02: Report DTCs by Status Mask

```
[59] [02] [Status Availability Mask] [DTC High] [DTC Mid] [DTC Low] [Status] ...
```

**Example:**
```
Request:  19 02 09
Response: 59 02 FF P0 13 5A 09 P0 14 2B 08
          ↑  ↑  ↑  ↑-----------↑ ↑  ↑-----------↑ ↑
          |  |  |       DTC 1    |       DTC 2    |
          |  |  Availability     Status          Status
          |  Sub-function 0x02
          Positive response

Decoded:
- DTC 1: P0135A (O2 Sensor Circuit Malfunction), Status: 0x09 (confirmed, test failed)
- DTC 2: P01 42B (MAP Sensor Out of Range), Status: 0x08 (confirmed)
```

### Sub-function 0x01: Report Number of DTCs

```
[59] [01] [Status Availability Mask] [DTC Format] [DTC Count MSB] [DTC Count LSB]
```

**Example:**
```
Request:  19 01 09
Response: 59 01 FF 01 00 03
          ↑  ↑  ↑  ↑  ↑-----↑
          |  |  |  |  Count: 3 DTCs
          |  |  |  Format: ISO 14229-1 (0x01)
          |  |  Availability mask
          |  Sub-function
          Success
```

---

## ❌ Negative Response Codes

```
[7F] [19] [NRC]
```

| NRC | Name | Description | Example Scenario |
|-----|------|-------------|------------------|
| `0x12` | Sub-Function Not Supported | Sub-function doesn't exist | Requesting sub-function 0x20 |
| `0x13` | Incorrect Message Length | Wrong parameter count | Sending `19 02` (missing status mask) |
| `0x31` | Request Out Of Range | DTC doesn't exist | Requesting snapshot for non-existent DTC |
| `0x22` | Conditions Not Correct | Can't read DTCs now | ECU in wrong state |

**Example:**
```
Request:  19 15
Response: 7F 19 12
          ↑  ↑  ↑
          |  |  Sub-function not supported
          |  ReadDTCInformation
          Error
```

---

## 💡 Practical Examples

### Example 1: Read All Active Fault Codes

**Scenario:** Check engine light is on, read what's wrong.

```
→ Request:  19 02 09
← Response: 59 02 FF P0 13 5A 09
            
Decoded: P0135A - O2 Sensor Heater Circuit Malfunction (Bank 1, Sensor 1)
Status: 0x09 = Confirmed fault, test currently failing
```

### Example 2: Count Total DTCs

**Scenario:** How many faults are stored?

```
→ Request:  19 01 09
← Response: 59 01 FF 01 00 05
            (5 DTCs match the status mask)
```

### Example 3: Read DTC Snapshot (Freeze Frame)

**Scenario:** Get engine parameters when fault occurred.

```
→ Request:  19 04 P0 13 5A 01
            (Get snapshot #1 for DTC P0135A)
← Response: 59 04 [DTC] 01 [snapshot data...]
            
Snapshot data might include:
- Engine RPM at time of fault: 2500
- Vehicle speed: 60 km/h
- Coolant temp: 85°C
- etc.
```

### Example 4: Get All Supported DTCs

**Scenario:** What faults can this ECU detect?

```
→ Request:  19 0A
← Response: 59 0A FF P0 10 0A P0 11 5B P0 13 5A P0 14 2B ...
            (List of all DTCs this ECU can report)
```

---

## 🔧 Pro Tips

- **DTC Format:** DTCs are 3 bytes but displayed as alphanumeric codes:
  - First 2 bits determine letter (P/C/B/U)
  - Next 14 bits are the hex number
  - Example: `0x0135A` = P0135A
- **Status byte interpretation:** Always check the status byte to know if the fault is active, pending, or historical.
- **Freeze frames are gold:** Snapshot data tells you the exact conditions when the fault occurred—invaluable for debugging intermittent issues.
- **Emission-related vs. non-emission:** Not all DTCs light up the MIL (check engine light). Some are information-only.

---

## DTC Status Byte Decoder

```
Bit 0: testFailed                    (Fault is currently active)
Bit 1: testFailedThisOperationCycle  (Failed since ignition on)
Bit 2: pendingDTC                    (Not confirmed yet, needs 2nd occurrence)
Bit 3: confirmedDTC                  (Stored permanently)
Bit 4: testNotCompletedSinceLastClear
Bit 5: testFailedSinceLastClear
Bit 6: testNotCompletedThisOperationCycle
Bit 7: warningIndicatorRequested     (MIL/check engine light)
```

**Example:** Status = `0x09` = `0000 1001`
- Bit 0 = 1: Test failed (fault is active NOW)
- Bit 3 = 1: Confirmed DTC (stored)

---

## 🔗 Related Services

- **0x14 ClearDiagnosticInformation:** Clear DTCs
- **0x85 ControlDTCSetting:** Enable/disable DTC recording
- **0x22 ReadDataByIdentifier:** Read related live data
