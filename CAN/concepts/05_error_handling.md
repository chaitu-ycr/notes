# 🛡️ Error Handling & Confinement

CAN is famous for its robustness. It has a built-in "immune system" to detect errors and isolate faulty nodes.

## 🚨 Error Types
1.  **Bit Error:** Sender puts a bit on the bus but reads back a different value (except during arbitration or ACK).
2.  **Stuff Error:** More than 5 consecutive bits of the same polarity detected.
3.  **CRC Error:** Calculated checksum doesn't match the received checksum.
4.  **Form Error:** Fixed-format fields (CRC Delimiter, ACK Delimiter, EOF) are violated.
5.  **ACK Error:** Sender transmits a message but no one acknowledges it (ACK slot remains Recessive).

![Bit Error](data/bit_error_1.png)
![CRC Error](data/crc_error.png)
![ACK Error](data/ack_error.png)

## 🛑 Error Frames
When *any* node detects an error, it immediately transmits an **Error Frame**.
*   **Active Error Flag:** 6 consecutive Dominant bits. This deliberately violates the bit-stuffing rule, causing *all other nodes* to also see an error and reject the frame.
*   **Result:** The bad message is destroyed globally. The sender will automatically retransmit.

## 📉 Error States (The Penalty System)
Every CAN controller has two counters: **TEC** (Transmit Error Counter) and **REC** (Receive Error Counter).

### 1. Error Active (Normal)
*   **Condition:** TEC < 128 AND REC < 128.
*   **Behavior:** Node participates normally. Sends **Active Error Flags** (Dominant) to destroy bad frames.

### 2. Error Passive (Yellow Card)
*   **Condition:** TEC > 127 OR REC > 127.
*   **Behavior:**
    *   Sends **Passive Error Flags** (Recessive). It can't stop bus traffic anymore; it can only complain quietly.
    *   Must wait an extra 8 bits (Suspend Transmission Time) before sending again, giving other nodes priority.

### 3. Bus Off (Red Card)
*   **Condition:** TEC > 255.
*   **Behavior:** The node disconnects itself from the bus physically (transistors off). It stays silent to protect the network.
*   **Recovery:** Requires a software reset or waiting for 128 occurrences of 11 consecutive recessive bits (idle bus).

![Error States](data/error_states.png)

## 🧮 Counter Rules (Simplified)
*   **Success:** Decrement counters.
*   **Rx Error:** REC + 1 (Receiver assumes it *might* be the only one seeing the error).
*   **Tx Error:** TEC + 8 (Sender assumes it is likely the problem).

> **Expert Insight:** This is why a node transmitting into an open circuit (no termination/no other nodes) goes Bus Off very quickly. It sends, gets no ACK (Error), TEC+8. Retries, no ACK, TEC+8... until 255.
