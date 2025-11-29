# 🚀 CAN FD (Flexible Data-Rate)

**CAN FD** is the modern successor to Classical CAN. It addresses the two main limitations of the original protocol: **Speed** and **Payload Size**.

## 🏎️ The Need for Speed
Classical CAN is limited to **1 Mbit/s**. As cars became more complex (ADAS, infotainment), this wasn't enough.
CAN FD allows the data phase of the frame to switch to a higher speed (typically **2 Mbit/s**, **5 Mbit/s**, or even **8 Mbit/s**).

## 📦 Bigger Payloads
Classical CAN can only send **8 bytes** per frame.
*   *Problem:* To send a 64-byte security key, you needed 8 separate frames (overhead!).
*   *Solution:* CAN FD supports payloads up to **64 bytes**.

## 🔑 Key Differences in Frame Structure

### 1. BRS (Bit Rate Switch)
A new bit in the Control Field.
*   **Recessive (1):** Switch to fast clock (Data Phase).
*   **Dominant (0):** Stay at arbitration speed.
*   *Note:* The Arbitration phase (ID) is *always* sent at the standard speed (e.g., 500k) to ensure robust arbitration. The speed boost only happens for the Data and CRC fields.

### 2. ESI (Error State Indicator)
Allows a node to report its own health.
*   **Dominant:** Node is Error Active (Healthy).
*   **Recessive:** Node is Error Passive (Sick).
*   *Benefit:* Diagnostic tools can identify failing nodes just by listening to their messages.

### 3. DLC Changes
For values 0-8, DLC works the same. For 9-15, it maps to larger sizes:
*   9 = 12 bytes
*   10 = 16 bytes
*   11 = 20 bytes
*   12 = 24 bytes
*   13 = 32 bytes
*   14 = 48 bytes
*   15 = 64 bytes

## ⚠️ Compatibility
*   **CAN FD controllers** can read Classical CAN frames.
*   **Classical CAN controllers** CANNOT read CAN FD frames (they will see them as errors).
*   *Implication:* You cannot mix old and new controllers on the same bus if you intend to use FD frames.
