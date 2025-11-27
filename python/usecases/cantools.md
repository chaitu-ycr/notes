# 🚗 Usecase: Decoding CAN Bus Data with `cantools`

If you've ever worked with automotive systems, robotics, or industrial machinery, you've likely encountered the **CAN bus**. It's the nervous system for most modern vehicles, carrying a constant stream of messages between components. But this data is raw and cryptic—just a bunch of IDs and bytes.

How do you turn `Arbitration ID: 0x18FEF100, Data: [0x10, 0x20, 0x30, ...]` into meaningful information like `EngineSpeed = 2500 rpm`? You need a "dictionary" that defines the rules for that specific vehicle. This dictionary is a **DBC file** (`.dbc`), and `cantools` is the essential Python library for reading it.

---

## 🎯 cantools: Practical, Tricky, and Fun Usages

```python
# ===== 1. Install cantools =====
# pip install cantools python-can

# ===== 2. Load a DBC File =====
import cantools
db = cantools.db.load_file('./_data/can_powertrain.dbc')
print([node.name for node in db.nodes])
print([msg.name for msg in db.messages])

# ===== 3. Decode a Raw CAN Message =====
message_id = 0x123
raw_data = b'\x1a\x2b\x00\x00\x00\x00\x00\x00'
message_def = db.get_message_by_frame_id(message_id)
decoded = message_def.decode(raw_data)
print(decoded)

# ===== 4. Encode a Signal to Raw Bytes =====
signal_data = {'EngineSpeed': 2500.5, 'EngineTemp': 90.0}
encoded = message_def.encode(signal_data)
print(encoded)

# ===== 5. Decode CAN Log File (.blf) =====
import can
can_log = can.BLFReader('./_data/can_log_file.blf')
for msg in can_log:
    if msg.arbitration_id == 256:
        try:
            decoded = db.decode_message(msg.arbitration_id, msg.data)
            print(decoded)
        except Exception as e:
            print(f"Error: {e}")

# ===== 6. Fun: Plotting CAN Signal with pandas & plotly =====
import pandas as pd
import plotly.express as px
engine_data = []
for msg in can_log:
    if msg.arbitration_id == 256:
        decoded = db.decode_message(msg.arbitration_id, msg.data)
        speed = decoded.get('EngSpeed')
        if speed is not None:
            engine_data.append({'timestamp': msg.timestamp, 'EngSpeed': speed})
if engine_data:
    df = pd.DataFrame(engine_data)
    fig = px.line(df, x='timestamp', y='EngSpeed', title='Engine Speed Over Time')
    fig.show()

# ===== 7. Generate C Code from DBC =====
# cantools generate_c_source ./_data/can_powertrain.dbc --output ./generated_code/

# ===== 8. Pro-Tips =====
# - Use db.get_message_by_name('MessageName') for direct access
# - Handle exceptions for robust decoding
# - Use db.messages for all message definitions
# - Use db.encode_message for encoding signals
```
