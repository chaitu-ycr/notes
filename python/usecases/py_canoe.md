# 🛶 Usecase: Automating CANoe with `py_canoe`

**Vector CANoe** is the industry-standard tool for developing, testing, and analyzing automotive electronic control units (ECUs) and networks. While it's incredibly powerful for manual testing and simulation, its true power in a modern workflow is unleashed through **automation**.

`py_canoe` is a Python package that acts as a bridge, allowing you to control and interact with the CANoe application directly from your Python scripts. This enables you to build powerful, automated test sequences, manipulate signals, run diagnostics, and generate reports, all using the flexibility of Python.

---

## 🎯 py_canoe: Practical, Tricky, and Fun Usages

```python
# ===== 1. Install py-canoe =====
# pip install py-canoe

# ===== 2. Basic Automation Workflow =====
from py_canoe import CANoe
canoe = CANoe()
canoe.open(r'C:\path\to\your\demo.cfg')
canoe.start_measurement()
# ... test logic ...
canoe.stop_measurement()
canoe.quit()

# ===== 3. Set and Get Signal Value =====
canoe.set_signal_value('CAN', 1, 'LightState', 'FlashLight', 1)
status = canoe.get_signal_value('CAN', 1, 'LightState', 'FlashLight')
print(status)

# ===== 4. Set and Get System Variable =====
canoe.set_system_variable_value('demo::sys_var1', 123)
val = canoe.get_system_variable_value('demo::sys_var1')
print(val)

# ===== 5. Send Diagnostic Request =====
resp = canoe.send_diag_request('Door', 'DefaultSession_Start')
print(resp.response_code, resp.data)
raw_resp = canoe.send_diag_request('Door', '10 02')
print(raw_resp)

# ===== 6. Execute Test Modules =====
canoe.execute_all_test_modules()
canoe.execute_test_module('MyTestModule')

# ===== 7. Fun: Automated Test Sequence =====
import time
canoe.start_measurement()
canoe.set_signal_value('CAN', 1, 'Engine', 'RPM', 3000)
time.sleep(2)
if canoe.get_signal_value('CAN', 1, 'Engine', 'RPM') == 3000:
    print("RPM set correctly!")
canoe.stop_measurement()

# ===== 8. Pro-Tips =====
# Use try/finally to ensure CANoe is closed
# Integrate with pandas/matplotlib for analysis
# Use in CI/CD pipelines for regression testing
```
