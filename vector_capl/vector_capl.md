---
title: "⚡ CAPL: The Magic Wand of Vector CANoe"
aliases:
  - "⚡ CAPL: The Magic Wand of Vector CANoe"
---
# ⚡ CAPL: The Magic Wand of Vector CANoe

Welcome to **CAPL** (Communication Access Programming Language). If CANoe is the simulation universe, CAPL is the physics engine you control. It looks like C, smells like C++, but behaves like an event-driven wizard. 🧙‍♂️

With CAPL, you can simulate ECUs, automate tests, analyze data, and basically make the CAN bus dance to your tune.

## 🔗 Related topics

- [CAN](../can/can.md) — CAPL is a direct tool for modeling and testing CAN behavior
- [UDS](../uds/uds.md) — diagnostics and ECU interactions are commonly exercised from CAPL
- [Vector CANoe](../vector_canoe/vector_canoe.md) — CAPL is normally used inside the CANoe environment
- [Testing](../testing/testing.md) — CAPL is frequently used to automate validation and regression checks
- [Projects / IDS](../projects/IDS/IDS.md) — simulation and traffic analysis support security and anomaly testing

## ⚡ Quick Start: Your First Script

CAPL is **event-driven**. Code only runs when something happens (a timer ticks, a message arrives, a key is pressed).

### The "Hello World" of CAPL (`examples/hello_world.can`)

[View File](examples/hello_world.can)

```capl
variables {
  msTimer myTimer;
}

on start {
  write("Hello, CAN bus!");
  setTimer(myTimer, 1000);
}

on timer myTimer {
  write("Tick...");
  setTimer(myTimer, 1000);
}
```

## 🛠️ Practical Examples (Copy-Paste-Run)

We've extracted the best examples into the `examples/` folder.

### 📡 Communication
- **[periodic_message.can](examples/periodic_message.can)**: Send a message every 100ms.
- **[keyboard_control.can](examples/keyboard_control.can)**: Press keys to send messages.
- **[sysvar_reaction.can](examples/sysvar_reaction.can)**: React to panel buttons/switches.

### 🧠 Logic & Processing
- **[user_functions.can](examples/user_functions.can)**: Create your own helper functions (checksums, etc.).
- **[string_manipulation.can](examples/string_manipulation.can)**: Handle text and ASCII data.
- **[array_processing.can](examples/array_processing.can)**: Buffer and process multiple signals.
- **[error_handling.can](examples/error_handling.can)**: Handle bus-off and invalid data.

### 🧪 Testing & Diagnostics
- **[test_case_signal.can](examples/test_case_signal.can)**: Verify a signal stays within range.
- **[test_case_diag.can](examples/test_case_diag.can)**: Send UDS requests and check responses.
- **[window_capture.can](examples/window_capture.can)**: Take screenshots for test reports.

### 🔧 Utilities
- **[logging_example.can](examples/logging_example.can)**: Write formatted logs to the Write Window.
- **[exec_external.can](examples/exec_external.can)**: Run external programs (Python, batch scripts) from CAPL.

## 📚 References

- [Vector CAPL Functions](https://vector.com/int/en/products/products-a-z/software/capl/capl-function-library/) - The official bible.
- [CANoe Demo Download](https://www.vector.com/int/en/download/canoe-demo-17-windows/) - Try it for free.



