# 📥 0x34: Request Download

**Purpose:** "I want to send you a file." This initiates a download (from tester TO ECU) session. It's the first step in software flashing—you tell the ECU "get ready to receive data" and specify how much and where.

**When to Use:**
- Software flashing/reprogramming
- Downloading calibration files
- Updating configuration data

---

## 📝 Request Format

```
[34] [dataFormatIdentifier] [addressAndLengthFormatIdentifier] [Memory Address...] [Memory Size...]
```

| Byte | Name | Description |
|------|------|-------------|
| 0 | SID | Service ID: `0x34` |
| 1 | Data Format | Compression/encryption (usually `0x00` = uncompressed/unencrypted) |
| 2 | Format Identifier | Address/size byte counts |
| 3... | Memory Address | Where to write |
| ... | Memory Size | How many bytes |

**Example:**
```
34 00 44 00 01 A0 00 00 00 10 00
↑  ↑  ↑  ↑--------------↑ ↑--------↑
|  |  |   Address         Size
|  |  Format (4 addr, 4 size)
|  Data format (uncompressed)
RequestDownload
```

---

## ✅ Positive Response

```
[74] [lengthFormatIdentifier] [maxNumberOfBlockLength...]
```

**Example:**
```
Request:  34 00 44 00 01 A0 00 00 00 10 00
Response: 74 20 10 00
          ↑  ↑  ↑-----↑
          |  |  Max block size: 4096 bytes
          |  Format (2 bytes)
          Success—ready to receive!
```

---

## ❌ Negative Response Codes

| NRC | Name | Description |
|-----|------|-------------|
| `0x22` | Conditions Not Correct | Not in programming session |
| `0x31` | Request Out Of Range | Invalid address/size |
| `0x33` | Security Access Denied | Not unlocked |
| `0x70` | Upload Download Not Accepted | Can't accept transfer |

---

## 💡 Example Flow

```
1. Request Download
→ 34 00 44 00 01 A0 00 00 00 10 00
← 74 20 10 00

2. Transfer Data (multiple 0x36 messages)
3. Request Transfer Exit (0x37)
```

---

## 🔗 Related Services

- **0x36 TransferData:** Actual data transfer
- **0x37 RequestTransferExit:** Complete download
- **0x10 DiagnosticSessionControl:** Need programming session
- **0x27 SecurityAccess:** Required first
