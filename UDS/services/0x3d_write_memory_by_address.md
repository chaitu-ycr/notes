# ✏️ 0x3D: Write Memory By Address

**Purpose:** Direct memory writing—the opposite of 0x23. Write raw bytes to a specific ECU memory address. Extremely dangerous if misused!

**When to Use:**
- Writing calibration data
- Low-level ECU configuration
- Patching memory (debugging)

⚠️ **WARNING:** Writing to wrong addresses can **brick the ECU**!

---

## 📝 Request Format

```
[3D] [addressAndLengthFormatIdentifier] [Memory Address...] [Memory Size...] [Data...]
```

**Example:**
```
3D 24 00 01 A0 00 00 04 AA BB CC DD
↑  ↑  ↑--------------↑ ↑-----↑ ↑-----------↑
|  |   Address         Size   Data to write
|  Format (4 addr, 2 size)
WriteMemoryByAddress
```

---

## ✅ Positive Response

```
[7D] [addressAndLengthFormatIdentifier] [Memory Address...] [Memory Size...]
```

**Example:**
```
Request:  3D 24 00 01 A0 00 00 04 AA BB CC DD
Response: 7D 24 00 01 A0 00 00 04
          Success! 4 bytes written to 0x0001A000
```

---

## ❌ Negative Response Codes

| NRC | Name | Description |
|-----|------|-------------|
| `0x13` | Incorrect Message Length | Wrong format |
| `0x22` | Conditions Not Correct | Can't write now |
| `0x31` | Request Out Of Range | Invalid address/size |
| `0x33` | Security Access Denied | Protected memory |
| `0x72` | General Programming Failure | Write failed |

---

## 💡 Example

```
Step 1: Unlock
→ 27 01 / 27 02 [key]

Step 2: Write
→ 3D 14 00 00 80 00 04 11 22 33 44
← 7D 14 00 00 80 00 04
  (4 bytes written to 0x00008000)
```

---

## 🔧 Pro Tips

- **Always unlock first:** 0x27 Security Access required
- **VERIFY after write:** Read back with 0x23 to confirm
- **Know your memory map:** Writing to code regions can brick ECU

---

## 🔗 Related Services

- **0x23 ReadMemoryByAddress:** Read counterpart
- **0x2E WriteDataByIdentifier:** Safer structured alternative
- **0x27 SecurityAccess:** Always required
