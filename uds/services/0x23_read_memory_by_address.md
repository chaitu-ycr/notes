# 🔍 0x23: Read Memory By Address

**Purpose:** Direct memory access—bypass DIDs and read raw ECU memory. Unlike 0x22 (which reads structured data), this service lets you specify an exact memory address and read bytes from it. It's like poking around in the ECU's RAM/Flash with a hex editor.

**When to Use:**
- Reading calibration data
- Debugging (peeking at memory regions)
- Accessing data without a defined DID

⚠️ **Danger:** Reading from invalid addresses can crash the ECU!

---

## 📝 Request Format

```
[23] [addressAndLengthFormatIdentifier] [Memory Address...] [Memory Size...]
```

| Byte | Name | Description |
|------|------|-------------|
| 0 | SID | Service ID: `0x23` |
| 1 | Format Identifier | Specifies address/size byte counts (see below) |
| 2... | Memory Address | Starting address (1-4 bytes) |
| ...  | Memory Size | Number of bytes to read (1-4 bytes) |

### Format Identifier

Format: `0xXY` where:
- **X** (high nibble) = size byte count
- **Y** (low nibble) = address byte count

**Example:** `0x24` means:
- Address: 4 bytes
- Size: 2 bytes

**Common values:**
- `0x14` = 4-byte address, 1-byte size
- `0x24` = 4-byte address, 2-byte size
- `0x34` = 4-byte address, 3-byte size

**Example Request:**
```
23 24 00 01 A0 00 00 10
↑  ↑  ↑--------------↑ ↑-----↑
|  |   Address        Size
|  Format (4 addr, 2 size)
ReadMemoryByAddress

Reads 16 bytes from address 0x0001A000
```

---

## ✅ Positive Response

```
[63] [Data bytes...]
```

**Example:**
```
Request:  23 24 00 01 A0 00 00 10
Response: 63 AA BB CC DD EE FF 11 22 33 44 55 66 77 88 99 00
          ↑  ↑---------------------------------------------------------↑
          |  16 bytes of data from address 0x0001A000
          Success
```

---

## ❌ Negative Response Codes

| NRC | Name | Description |
|-----|------|-------------|
| `0x13` | Incorrect Message Length | Wrong format |
| `0x22` | Conditions Not Correct | Can't read now |
| `0x31` | Request Out Of Range | Invalid memory address/size |
| `0x33` | Security Access Denied | Protected memory |

---

## 💡 Example

```
→ Request:  23 14 00 00 80 00 20
            (Read 32 bytes from 0x00008000)
← Response: 63 [32 bytes of  calibration data...]
```

---

## 🔗 Related Services

- **0x22 ReadDataByIdentifier:** Structured alternative
- **0x3D WriteMemoryByAddress:** Write counterpart
- **0x27 SecurityAccess:** Often required
