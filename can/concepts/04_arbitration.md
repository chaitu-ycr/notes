# ⚖️ Arbitration (Priority)

How does CAN prevent collisions when two nodes try to talk at once? It uses a mechanism called **CSMA/CR** (Carrier Sense Multiple Access / Collision Resolution), also known as **Bitwise Arbitration**.

## 👑 The Golden Rule
**Dominant (0) beats Recessive (1).**

When a node transmits a Recessive bit but reads back a Dominant bit, it knows it has lost arbitration. It immediately stops transmitting and starts listening.

## 🥊 The Fight: Step-by-Step
Imagine Node A (ID `0x100`) and Node B (ID `0x110`) start transmitting at the exact same time.

| Bit Position | Node A (0x100) | Node B (0x110) | Bus State | Result |
| :--- | :--- | :--- | :--- | :--- |
| **Start of Frame** | 0 | 0 | 0 | Tie |
| **ID Bit 10** | 0 | 0 | 0 | Tie |
| ... | ... | ... | ... | ... |
| **ID Bit 4** | **0** (Dominant) | **1** (Recessive) | **0** | **Node A Wins!** |

1.  Both nodes send the first few bits identical.
2.  At **ID Bit 4**, Node A sends `0` and Node B sends `1`.
3.  The bus goes to `0` (because 0 dominates 1).
4.  Node A reads `0` (matches what it sent) -> **Continues**.
5.  Node B reads `0` (does NOT match what it sent) -> **Stops transmitting**.

## 🏆 Implications
1.  **Lower ID = Higher Priority:** Since 0 dominates, IDs with more leading zeros win.
    *   `0x000` is the highest priority possible.
    *   `0x7FF` is the lowest priority (Standard CAN).
2.  **Non-Destructive:** The winning message continues without *any* delay or corruption. Bandwidth is not wasted on collisions.
3.  **Latency:** High-priority messages (Engine, Brakes) have guaranteed low latency. Low-priority messages (Door locks, Radio) wait.
