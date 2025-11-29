# 📤 0x35: Request Upload

**Purpose:** "I want to receive a file from you." This initiates an upload (from ECU TO tester) session. It's the opposite of 0x34—you're asking the ECU to send you data (e.g., reading out current firmware).

**When to Use:**
- Backing up ECU firmware
- Reading calibration files
- Extracting diagnostic data

---

## 📝 Request Format

```
[35] [dataFormatIdentifier] [addressAndLengthFormatIdentifier] [Memory Address...] [Memory Size...]
```

Same format as 0x34 RequestDownload.

**Example:**
```
35 00 44 00 01 A0 00 00 00 10 00
```

---

## ✅ Positive Response

```
[75] [lengthFormatIdentifier] [maxNumberOfBlockLength...]
```

**Example:**
```
Response: 75 20 10 00
          (Max 4096 bytes per block)
```

---

## ❌ Negative Response Codes

Same as 0x34 RequestDownload.

---

## 💡 Example Flow

```
1. Request Upload
→ 35 00 44 00 01 A0 00 00 00 10 00
← 75 20 10 00

2. Transfer Data (0x36 to receive)
3. Request Transfer Exit (0x37)
```

---

## 🔗 Related Services

- **0x34 RequestDownload:** Opposite direction
- **0x36 TransferData:** Actual data transfer
- **0x37 RequestTransferExit:** Complete upload
