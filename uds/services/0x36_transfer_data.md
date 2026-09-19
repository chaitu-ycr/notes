---
title: "📦 0x36: Transfer Data"
aliases:
  - "📦 0x36: Transfer Data"
---

# 📦 0x36: Transfer Data

**Purpose:** This is the "data pipeline" service. After initiating a download (0x34) or upload (0x35), you use 0x36 to actually transfer the data chunks. It's called repeatedly until all data is sent/received.

**When to Use:**
- Transferring flash/calibration data (after 0x34/0x35)
- Called in a loop for large files

---

## 📝 Request Format

```
[36] [blockSequenceCounter] [transferRequestParameterRecord...]
```

| Byte | Name | Description |
|------|------|-------------|
| 0 | SID | Service ID: `0x36` |
| 1 | Block Sequence Counter | 1,  2, 3... wraps at 0xFF back to 0 or 1 |
| 2... | Data | The actual bytes to transfer |

**Example (Download—sending TO ECU):**
```
36 01 AA BB CC DD EE FF ...
↑  ↑  ↑--------------------↑
|  |  Data chunk
|  Block #1
TransferData
```

**Example (Upload—receiving FROM ECU):**
```
Request:  36 01
Response: 76 01 AA BB CC DD EE FF ...
             ↑  ↑--------------------↑
             |  Data from ECU
             Block #1
```

---

## ✅ Positive Response

```
[76] [blockSequenceCounter] [transferResponseParameterRecord...]
```

**For Download:**
```
Request:  36 01 [data]
Response: 76 01
          (ACK: Block #1 received okay)
```

**For Upload:**
```
Request:  36 01
Response: 76 01 [data from ECU]
```

---

## ❌ Negative Response Codes

| NRC | Name | Description |
|-----|------|-------------|
| `0x24` | Request Sequence Error | Wrong block number |
| `0x72` | General Programming Failure | Write failed |
| `0x73` | Wrong Block Sequence Counter | Blocks out of order |
| `0x93` | Voltage Too High | Battery voltage issue |
| `0x94` | Voltage Too Low | Battery voltage issue |

---

## 💡 Example: Download Loop

```
→ 34 00 ... (Request Download)
← 74 ...

→ 36 01 [first 4KB]
← 76 01

→ 36 02 [next 4KB]
← 76 02

→ 36 03 [next 4KB]
← 76 03

... (continue until all data sent) ...

→ 37 (Request Transfer Exit)
← 77
```

---

## 🔧 Pro Tips

- **Block counter:** Starts at 1 (not 0), wraps at 0xFF
- **Max block size:** Determined by 0x34/0x35 response
- **Keep-alive:** Send 0x3E TesterPresent during long transfers

---

## 🔗 Related Services

- **0x34 RequestDownload:** Initiates download
- **0x35 RequestUpload:** Initiates upload
- **0x37 RequestTransferExit:** Finalize transfer



