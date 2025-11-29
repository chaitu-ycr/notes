# 🔬 Bit Timing (Expert Topic)

A "bit" on the CAN bus isn't just a simple high/low pulse. It is a complex interval divided into segments to ensure all nodes—even with slightly different clock speeds—can stay synchronized.

## ⏱️ The Time Quantum (tq)
The atomic unit of time in CAN.
$$ tq = \frac{Prescaler + 1}{f_{sys}} $$

## 🍰 The 4 Segments of a Bit
Every bit is constructed of integer multiples of `tq`.

1.  **SYNC_SEG (1 tq):**
    *   The "Start Line". The edge of the signal (Recessive -> Dominant) is expected to occur here.
2.  **PROP_SEG (1-8 tq):**
    *   Compensates for physical delay times within the network (transceiver delay + cable propagation delay).
    *   *Rule:* Must be long enough for the signal to travel to the furthest node and back.
3.  **PHASE_SEG1 (1-8 tq):**
    *   Used to compensate for positive phase errors (clock running slow). Can be lengthened.
4.  **PHASE_SEG2 (1-8 tq):**
    *   Used to compensate for negative phase errors (clock running fast). Can be shortened.

## 📍 The Sample Point
The moment the controller actually reads the bus level to decide if it's a `0` or `1`.
*   **Location:** Between PHASE_SEG1 and PHASE_SEG2.
*   **Calculation:** $\frac{SYNC + PROP + PHASE1}{Total Bit Time}$
*   **Target:** Typically **75% to 87.5%** for automotive applications.
    *   *Too Early:* Susceptible to ringing/noise at the start of the bit.
    *   *Too Late:* Susceptible to clock drift issues.

## 🤸 SJW (Synchronization Jump Width)
The maximum number of `tq` that the controller can lengthen or shorten a bit during resynchronization.
*   **Range:** 1 to 4 tq.
*   **Purpose:** Allows the controller to "jump" its timing to realign with the actual bus edges.
*   **Trade-off:** Larger SJW allows for worse oscillators (cheaper) but requires better signal quality.

## 🧮 Calculation Example
**Goal:** 500 kbps with 80 MHz clock.
1.  **Bit Time:** $1 / 500000 = 2 \mu s$.
2.  **Choose Prescaler:** Let's try 4. $tq = 5 / 80MHz = 62.5 ns$.
3.  **Total tq per bit:** $2 \mu s / 62.5 ns = 32 tq$. (Too high! Max is usually 25).
4.  **Adjust Prescaler:** Try 9. $tq = 10 / 80MHz = 125 ns$.
5.  **Total tq:** $2 \mu s / 125 ns = 16 tq$. (Perfect).
6.  **Distribute Segments (Target 80% sample point):**
    *   Sync = 1
    *   Sample Point @ 16 * 0.8 = 12.8 -> Round to 13.
    *   Prop + Phase1 = 13 - 1 = 12.
    *   Phase2 = 16 - 13 = 3.
    *   Let Prop = 6, Phase1 = 6.
    *   **Result:** Sync=1, Prop=6, Phase1=6, Phase2=3. Total=16. Sample=81%.
