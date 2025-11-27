# 🚌 Usecase: Interacting with CAN Hardware with `python-can`

To work with a real CAN bus, your computer needs a physical hardware interface (e.g., a Vector VN1630, a PEAK-System PCAN-USB, or a Kvaser Leaf). The problem is that every hardware vendor provides a different driver and API.

**`python-can`** solves this problem by providing a single, consistent Python library for sending and receiving CAN messages across a wide variety of hardware devices. It's the foundational layer that lets your Python scripts talk to the physical world of CAN.

---

## 🎯 python-can: Practical, Tricky, and Fun Usages

```python
# ===== 1. Install python-can =====
# pip install python-can

# ===== 2. Open CAN Bus =====
import can
try:
    with can.Bus(interface='vector', channel=0, bustype='vector') as bus:
        print(bus.channel_info)
        # ...
except can.CanError as e:
    print(f"Error: {e}")

# ===== 3. Send CAN Message =====
msg = can.Message(arbitration_id=0x7E0, data=[0x02,0x10,0x03,0,0,0,0,0], is_extended_id=False)
bus.send(msg)
print("Message sent!")

# ===== 4. Receive CAN Message =====
message = bus.recv(timeout=1.0)
if message:
    print(f"Received: {message}")
else:
    print("No message received.")

# ===== 5. Listen for Messages =====
for msg in bus:
    print(msg)

# ===== 6. Set CAN Filters =====
filters = [{"can_id": 0x7E8, "can_mask": 0x7FF, "extended": False}]
bus.set_filters(filters)
for msg in bus:
    print(f"Filtered: {msg}")

# ===== 7. Fun: Log and Replay =====
from can import Logger, LogReader
logger = Logger("logfile.log", "asc")
logger.on_message_received(msg)
reader = LogReader("logfile.log")
for m in reader:
    print(m)

# ===== 8. Pro-Tips =====
# Use with statement for safe bus closing
# Use python-can with cantools for decoding signals
# Use bus.send_periodic for cyclic messages
# Use bus.shutdown() to close bus manually
```
