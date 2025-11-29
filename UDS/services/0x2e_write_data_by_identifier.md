# ✍️ 0x2E: Write Data By Identifier

**Purpose:** This is the "write" counterpart to 0x22 (Read Data By Identifier). It lets you change ECU configuration, calibration values, or settings by writing to specific Data Identifiers (D IDs). Think of it as editing the ECU's configuration file.

**When to Use:**
- Writing vehicle configuration (VIN coding, option bytes)
- Updating calibration parameters
- Setting production data
- Configuring ECU behavior

⚠️ **Danger Zone:** Writing wrong values can brick an ECU. Always verify what you're writing!

---

## 📝 Request Format

```
[2E] [DID MSB] [DID LSB] [Data byte 1] [Data byte 2] ...
```

| Byte | Name | Description |
|------|------|-------------|
| 0 | SID | Service ID: `0x2E` |
| 1-2 | Data Identifier | DID to write (MSB, LSB) |
| 3... | Data Record | Bytes to write |

**Example:**
```
2E F1 90 V I N D A T A H E R E 1 2 3 4 5
↑  ↑-----↑ ↑-----------------------------------↑
|    DID     New VIN (17 bytes)
WriteDataByIdentifier
```

---

## ✅ Positive Response

```
[6E] [DID MSB] [DID LSB]
```

| Byte | Name | Description |
|------|------|-------------|
| 0 | Response SID | `0x6E` (0x2E + 0x40) |
| 1-2 | Data Identifier | Echoes the DID that was written |

**Example:**
```
Request:  2E F1 90 [17 VIN bytes]
Response: 6E F1 90
          ↑  ↑-----↑
          |  DID F190 written successfully
          Success
```

---

## ❌ Negative Response Codes

```
[7F] [2E] [NRC]
```

| NRC | Name | Description | Example Scenario |
|-----|------|-------------|------------------|
| `0x13` | Incorrect Message Length | Wrong data length | Writing 16 bytes when VIN needs 17 |
| `0x22` | Conditions Not Correct | Preconditions not met | Trying to write while vehicle is moving |
| `0x31` | Request Out Of Range | DID doesn't exist or not writable | Writing to read-only DID |
| `0x33` | Security Access Denied | Not unlocked | Protected DID requires security access |
| `0x72` | General Programming Failure | Write operation failed | EEPROM write error |

**Example:**
```
Request:  2E F1 90 [VIN data]
Response: 7F 2E 33
          ↑  ↑  ↑
          |  |  Security access denied
          |  WriteDataByIdentifier
          Error
```

---

## 💡 Practical Examples

### Example 1: Write VIN (Vehicle Identification Number)

**Scenario:** Programming VIN during vehicle production.

```
Step 1: Enter extended session & unlock security
→ Request:  10 03
← Response: 50 03 ...

→ Request:  27 01
← Response: 67 01 [seed]
→ Request:  27 02 [key]
← Response: 67 02

Step 2: Write VIN
→ Request:  2E F1 90 57 44 42 5A 5A 5A 31 4B 5A 30 30 39 31 32 33 34 35 36
            (WriteDataByIdentifier, DID F190, VIN: "WDBZZZ1KZ009123456")
← Response: 6E F1 90
            (Success!)

Step 3: Verify
→ Request:  22 F1 90
← Response: 62 F1 90 57 44 42 5A 5A 5A 31 4B 5A 30 30 39 31 32 33 34 35 36
            (Read back confirms write succeeded)
```

### Example 2: Write Configuration Byte

**Scenario:** Enabling optional equipment (e.g., parking sensors).

```
→ Request:  2E F1 50 03
            (Write config byte to enable feature #3)
← Response: 6E F1 50
            (Success! Feature enabled)
```

### Example 3: Write Fails—Wrong Length

**Scenario:** Sending wrong number of bytes.

```
→ Request:  2E F1 90 12 34
            (VIN needs 17 bytes, only sent 2!)
← Response: 7F 2E 13
            (Error: Incorrect message length)
```

### Example 4: Security Required

**Scenario:** Trying to write protected calibration.

```
→ Request:  2E F1 00 [calibration data]
← Response: 7F 2E 33
            (Error: Security access required first!)
```

---

## 🔧 Pro Tips

- **Read first:** Always read the current value with 0x22 before writing. You might need to preserve some bits or know the format.
- **Data format matters:** DIDs have specific data formats. A 2-byte temperature might be in units of 0.1°C with an offset. Know your spec!
- **Security is almost always required:** Most writable DIDs are protected. Expect to unlock with 0x27 first.
- **Session requirements:** Many DIDs can only be written in extended or programming session.
- **Verify after write:** Always read back (0x22) to confirm the write worked.
- **EEPROM wear:** Writing to EEPROM/Flash has limited write cycles (typically 100,000+). Don't write unnecessarily!

---

## Common Writable DIDs

| DID | Name | Typical Use |
|-----|------|-------------|
| `0xF110...0xF18F` | VIN-related data | Vehicle identification |
| `0xF190` | VIN | Vehicle ID number (17 ASCII bytes) |
| `0xF1Cx` | Tester/Factory data | Serial numbers, test stamps |
| `0xF1xx` | Vehicle manufacturer data | Configuration, coding |

**⚠️ Note:** Exact DIDs vary by manufacturer and ECU. Always consult the ECU specification!

---

## 🔗 Related Services

- **0x22 ReadDataByIdentifier:** Read before/after writing
- **0x27 SecurityAccess:** Almost always required first
- **0x10 DiagnosticSessionControl:** Extended session usually needed
- **0x2C DynamicallyDefineDataIdentifier:** Create custom DIDs
