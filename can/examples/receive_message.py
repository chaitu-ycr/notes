import can

def receive_message():
    # Create a bus instance
    bus = can.Bus(interface='virtual', channel='vcan0', bitrate=500000)

    print("Listening for messages...")
    
    try:
        while True:
            msg = bus.recv(1) # Timeout 1 second
            if msg is not None:
                print(f"Timestamp: {msg.timestamp:.6f}")
                print(f"ID: {hex(msg.arbitration_id)}")
                print(f"DLC: {msg.dlc}")
                print(f"Data: {msg.data.hex()}")
                print("-" * 20)
    except KeyboardInterrupt:
        print("\nStopped listening")

if __name__ == "__main__":
    receive_message()
