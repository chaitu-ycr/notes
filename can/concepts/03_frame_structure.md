# 📦 CAN Frame Structure

Data on the CAN bus is sent in packets called **Frames**. The most common is the **Data Frame**.

## 🖼️ Standard Data Frame (CAN 2.0A)
Uses an 11-bit Identifier.

```mermaid
flowchart LR
    SOF[SOF] --> ID[ID: 11 bits]
    ID --> RTR[RTR]
    RTR --> IDE[IDE]
    IDE --> r0[r0]
    r0 --> DLC[DLC: 4 bits]
    DLC --> DATA[Data: 0-8 Bytes]
    DATA --> CRC[CRC: 15 bits]
    CRC --> DEL[Del]
    DEL --> ACK[ACK]
    ACK --> DEL2[Del]
    DEL2 --> EOF[EOF: 7 bits]
```

### Field Breakdown

1.  **SOF (Start of Frame):** A single Dominant (0) bit. Synchronizes all nodes.
2.  **Arbitration Field:**
    *   **Identifier (ID):** 11 bits. Determines priority and content (e.g., `0x123`).
    *   **RTR (Remote Transmission Request):** Dominant (0) for Data Frames, Recessive (1) for Remote Frames.
3.  **Control Field:**
    *   **IDE (Identifier Extension):** Dominant (0) for Standard (11-bit), Recessive (1) for Extended (29-bit).
    *   **r0:** Reserved bit.
    *   **DLC (Data Length Code):** 4 bits. Indicates number of data bytes (0-8).
4.  **Data Field:** The payload. 0 to 8 bytes of actual information.
5.  **CRC Field (Cyclic Redundancy Check):**
    *   **CRC Sequence:** 15 bits calculated from the frame data. Used for error detection.
    *   **CRC Delimiter:** 1 Recessive bit.
6.  **ACK Field (Acknowledgment):**
    *   **ACK Slot:** Sender transmits Recessive (1). *Any* node that receives the frame correctly overwrites this with Dominant (0).
    *   **ACK Delimiter:** 1 Recessive bit.
7.  **EOF (End of Frame):** 7 consecutive Recessive bits.

## 📏 Extended Data Frame (CAN 2.0B)
Uses a 29-bit Identifier (11-bit Base ID + 18-bit Extension).
*   Allows for 536 million unique IDs (vs 2048 for Standard).
*   Used in J1939 (Heavy Duty) and modern passenger cars.

## 🧵 Bit Stuffing
*   **Rule:** To maintain synchronization, the bus cannot have more than **5 consecutive bits** of the same polarity.
*   **Action:** If the sender detects 5 identical bits, it automatically inserts (stuffs) one opposite bit.
*   **Receiver:** Automatically removes (destuffs) the extra bit.
*   *Note:* Stuffing applies from SOF up to the CRC Sequence. CRC Delimiter, ACK, and EOF are fixed form and not stuffed.

![Bit Stuffing Example 1](data/stuff_error_1.png)
![Bit Stuffing Example 2](data/stuff_error_2.png)
