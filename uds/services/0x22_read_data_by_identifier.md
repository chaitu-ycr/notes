# 📖 0x22: Read Data By Identifier

**Purpose:** This is your "ask anything" service. Want to know the VIN? Battery voltage? Software version? ECU temperature? Each piece of data has a unique 2-byte ID (called a DID), and this service lets you request it.

**When to Use:**
- Reading vehicle identification (VIN, part numbers)
- Monitoring live data (sensor values, temperatures)
- Checking software versions
- Reading configuration values

---

## 📝 Request Format

```
[22] [DID MSB] [DID LSB] [DID 2 MSB] [DID 2 LSB] ...
```

| Byte | Name | Description |
|------|------|-------------|
| 0 | SID | Service ID: `0x22` |
| 1-2 | Data Identifier 1 | First DID to read (MSB, LSB) |
| 3-4 | Data Identifier 2 | (Optional) Second DID to read |
| ... | ... | You can request multiple DIDs in one message |

**⚠️ Note:** Some ECUs support reading multiple DIDs at once, others require separate requests.

### Common DIDs (Examples)

| DID | Name | Description |
|-----|------|-------------|
| `0xF186` | Active Diagnostic Session | Current session (default/extended/programming) |
| `0xF187` | Vehicle Manufacturer Spare Part Number | ECU part number |
| `0xF18A` | Vehicle Manufacturer ECU Software Number | Software version |
| `0xF18C` | ECU Serial Number | Unique ECU serial |
| `0xF190` | VIN | Vehicle Identification Number (17 bytes) |
| `0xF191` | Vehicle Manufacturer ECU Hardware Number | Hardware version |
| `0xF19E` | Active Diagnostic Session Data Identifier | Extended session info |

---

## ✅ Positive Response

```
[62] [DID MSB] [DID LSB] [Data...] [DID 2 MSB] [DID 2 LSB] [Data 2...]
```

| Byte | Name | Description |
|------|------|-------------|
| 0 | Response SID | `0x62` (0x22 + 0x40) |
| 1-2 | Data Identifier | Echo of requested DID |
| 3... | Data Record | Actual data for this DID |
| ... | ... | Repeat for additional DIDs if multiple were requested |

**Example 1: Read VIN**
```
Request:  22 F1 90
Response: 62 F1 90 57 44 42 5A 5A 5A 31 4B 5A 30 30 39 31 32 33 34 35 36
          ↑  ↑-----↑ ↑-------------------------------------------------------↑
          |    DID         VIN: "WDBZZZ1KZ009123456" (17 ASCII bytes)
          Positive response
```

**Example 2: Read Software Version**
```
Request:  22 F1 8A
Response: 62 F1 8A 01 02 03 04
          ↑  ↑-----↑ ↑-----------↑
          |    DID    Software version bytes (format varies by OEM)
          Positive response
```

---

## ❌ Negative Response Codes

```
[7F] [22] [NRC]
```

| NRC | Name | Description | Example Scenario |
|-----|------|-------------|------------------|
| `0x13` | Incorrect Message Length | Wrong byte count | Sending `22 F1` (incomplete DID) |
| `0x14` | Response Too Long | Response doesn't fit in one message | Reading  a huge data block |
| `0x31` | Request Out Of Range | DID doesn't exist | Requesting DID 0xABCD that ECU doesn't support |
| `0x33` | Security Access Denied | DID is protected | Reading calibration data without security access |
| `0x22` | Conditions Not Correct | Can't read right now | Reading dynamic DID while ECU is in wrong state |

**Example:**
```
Request:  22 AB CD
Response: 7F 22 31
          ↑  ↑  ↑
          |  |  Request out of range (DID doesn't exist)
          |  ReadDataByIdentifier
          Negative response
```

---

## 💡 Practical Examples

### Example 1: Read VIN (Most Common Use Case)

**Scenario:** You need to identify the vehicle for a repair.

```
→ Request:  22 F1 90
← Response: 62 F1 90 57 44 42 5A 5A 5A 31 4B 5A 30 30 39 31 32 33 34 35 36
            
Decoded VIN: W D B Z Z Z 1 K Z 0 0 9 1 2 3 4 5 6
             ↑ Manufacturer code (Mercedes-Benz)
```

### Example 2: Read ECU Part Number

**Scenario:** Checking if correct ECU is installed.

```
→ Request:  22 F1 87
← Response: 62 F1 87 41 30 30 34 37 30 37 38 35 39
            ↑  ↑-----↑ ↑-----------------------------↑
            |    DID    Part number: "A0047078859" (ASCII)
            Success
```

### Example 3: Read Multiple DIDs at Once

**Scenario:** Reading both VIN and part number in one request.

```
→ Request:  22 F1 90 F1 87
← Response: 62 F1 90 [17 VIN bytes] F1 87 [part number bytes]
            (Both DIDs returned in one response)
```

### Example 4: DID Not Supported

**Scenario:** Requesting a DID that doesn't exist in this ECU.

```
→ Request:  22 12 34
← Response: 7F 22 31
            (Error: This DID is not implemented)
```

### Example 5: Security Required

**Scenario:** Trying to read protected calibration data.

```
→ Request:  22 F1 00
← Response: 7F 22 33
            (Error: You need security access first!)
```

---

## 🔧 Pro Tips

- **DID ranges:** 
  - `0xF000-0xF0FF`: Network configuration
  - `0xF100-0xF1FF`: Vehicle manufacturer specific
  - `0xF200-0xF2FF`: Network configuration (more)
  - `0xF300-0xF3FF`: Vehicle manufacturer specific (more)
- **Data format:** The response data format varies by DID. Some are ASCII text, some are binary. Always check the specification!
- **Multiple DIDs:** Reading multiple DIDs saves time, but not all ECUs support it. If you get NRC 0x13, try one DID at a time.
- **Dynamic DIDs:** Some DIDs are "live"—they return current sensor readings. Their values change in real-time.

---

## 🔗 Related Services

- **0x2E WriteDataByIdentifier:** Write data to a DID
- **0x2C DynamicallyDefineDataIdentifier:** Create custom composite DIDs
- **0x10 DiagnosticSessionControl:** Some DIDs only readable in certain sessions
