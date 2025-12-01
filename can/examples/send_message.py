import can
import time

def send_message():
    # Create a bus instance
    # 'interface' and 'channel' depend on your hardware
    # For virtual testing, use 'virtual' interface
    bus = can.Bus(interface='virtual', channel='vcan0', bitrate=500000)

    # Create a message
    msg = can.Message(
        arbitration_id=0x123,
        data=[0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88],
        is_extended_id=False
    )

    try:
        bus.send(msg)
        print(f"Message sent on {bus.channel_info}")
        print(f"ID: {hex(msg.arbitration_id)} Data: {msg.data.hex()}")
    except can.CanError:
        print("Message NOT sent")

if __name__ == "__main__":
    send_message()
