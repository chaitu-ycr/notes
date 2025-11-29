# 🚌 CAN Examples

This directory contains practical examples for understanding and working with the CAN protocol.

## 📂 Files

| File | Type | Description |
|------|------|-------------|
| **[sample_log.asc](sample_log.asc)** | Log | A raw CAN log file in Vector ASCII format. Shows what data looks like "on the wire". |
| **[simple_db.dbc](simple_db.dbc)** | Database | A snippet of a DBC file defining messages and signals. |
| **[send_message.py](send_message.py)** | Python | Script to send a CAN message using `python-can`. |
| **[receive_message.py](receive_message.py)** | Python | Script to listen for and decode CAN messages. |
| **[bit_timing_calc.py](bit_timing_calc.py)** | Python | A simple calculator to understand Prescalers and Time Quanta. |

## 🐍 Running Python Examples

1.  **Install python-can:**
    ```bash
    pip install python-can
    ```
2.  **Run the script:**
    ```bash
    python send_message.py
    ```

> **Note:** The scripts are configured to use a `virtual` interface by default. This allows you to test without physical hardware!
