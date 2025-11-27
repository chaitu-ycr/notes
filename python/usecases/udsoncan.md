# 🚗 Usecase: Vehicle Diagnostics with `udsoncan`

**UDS (Unified Diagnostic Services)** is the standard protocol (ISO 14229-1) used in the automotive industry to diagnose, test, and configure electronic control units (ECUs). It allows you to ask an ECU questions like "What's your serial number?" (Read Data by Identifier) or give it commands like "Reset yourself" (ECU Reset).

These UDS messages are typically sent over a CAN bus using a transport protocol called **ISO-TP** (ISO 15765-2). The `udsoncan` library is a powerful Python tool that handles all the complexity of the UDS and ISO-TP layers, allowing you to interact with ECUs using a clean, high-level API.

---

## 🎯 udsoncan: Practical, Tricky, and Fun Usages

```python
# ===== 1. Install udsoncan =====
# pip install udsoncan python-can python-can-isotp

# ===== 2. Setup CAN and ISO-TP Connection =====
import can, isotp
from udsoncan.connections import PythonIsoTpConnection
bus = can.interface.Bus(bustype='socketcan', channel='vcan0', bitrate=500000)
tp_addr = isotp.Address(addressing_mode=isotp.AddressingMode.Normal_11bits, txid=0x7E0, rxid=0x7E8)
stack = isotp.CanStack(bus=bus, address=tp_addr)
conn = PythonIsoTpConnection(stack)

# ===== 3. UDS Client Session =====
from udsoncan.client import Client
from udsoncan.services import *
config = {
    'security_algo': lambda level, seed: bytes([s+1 for s in seed]),
    'exception_on_negative_response': True,
    'request_timeout': 5,
}
with Client(conn, config=config) as client:
    client.change_session(DiagnosticSessionControl.ExtendedDiagnosticSession)
    client.unlock_security_access(SecurityAccess.Level1)
    resp = client.read_data_by_identifier(DataIdentifier.VehicleIdentificationNumber)
    vin = resp.service_data.values[DataIdentifier.VehicleIdentificationNumber]
    print(f"VIN: {vin}")
    client.ecu_reset(ECUReset.HardReset)

# ===== 4. Fun: Read ECU Software Version =====
with Client(conn, config=config) as client:
    resp = client.read_data_by_identifier(0xF190)  # Example ID for software version
    print(resp.service_data.values)

# ===== 5. Exception Handling =====
try:
    with Client(conn, config=config) as client:
        client.change_session(DiagnosticSessionControl.ProgrammingSession)
except udsoncan.exceptions.NegativeResponseException as e:
    print(f"Negative response: {e.response}")

# ===== 6. Pro-Tips =====
# Use python-can for hardware abstraction
# Use custom security_algo for real ECUs
# Always reset ECU after tests
# Use DataIdentifier for standard IDs
```
