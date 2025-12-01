# ⚡ CAPL: The Magic Wand of Vector CANoe

Welcome to **CAPL** (Communication Access Programming Language). If CANoe is the simulation universe, CAPL is the physics engine you control. It looks like C, smells like C++, but behaves like an event-driven wizard. 🧙‍♂️

With CAPL, you can simulate ECUs, automate tests, analyze data, and basically make the CAN bus dance to your tune.

---

## 🚀 Prerequisites

- **Vector CANoe/CANalyzer**: You need the tool (demo version works for learning).
- **C Knowledge**: If you know `if`, `else`, `for`, and `int`, you're 90% there.
- **A PC**: Preferably one that doesn't smoke when you open Chrome.

---

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

---

## 🧩 Core Concepts

### 1. Variables & Data Types
CAPL has your standard types plus some special ones.

**File:** [`examples/data_types.can`](examples/data_types.can)

```capl
byte b = 0x10;      // 1 byte
word w = 0x1000;    // 2 bytes
dword d = 0x10000;  // 4 bytes
message 0x100 msg;  // CAN message object
msTimer t1;         // Timer object
```

### 2. Event Handlers
This is where the magic happens. You define *what* triggers your code.

**File:** [`examples/event_handlers.can`](examples/event_handlers.can)

- `on start`: Runs once when measurement starts.
- `on message 0x123`: Runs when message 0x123 is received.
- `on key 'a'`: Runs when you press 'a'.
- `on timer t1`: Runs when timer `t1` expires.
- `on sysvar Engine::Speed`: Runs when a system variable changes.

### 3. Sending Messages
You can send messages periodically or on events.

**File:** [`examples/periodic_message.can`](examples/periodic_message.can)
**File:** [`examples/keyboard_control.can`](examples/keyboard_control.can)

```capl
on key 's' {
  message 0x100 msg;
  msg.dlc = 8;
  msg.byte(0) = 0x01;
  output(msg); // Send it!
}
```

---

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

---

## 💡 Pro Tips

1.  **`this` Keyword**: Inside an event (like `on message`), `this` refers to the object that triggered it.
    ```capl
    on message 0x100 {
      write("Received ID: %x", this.id);
    }
    ```
2.  **Write Window**: Use `write()` constantly for debugging. It's your best friend.
3.  **System Variables**: Use them to connect your CAPL script to graphical panels.
4.  **Compiling**: You must compile your script in CANoe before running. Look for the lightning bolt icon ⚡.

---

## 📚 References

- [Vector CAPL Functions](https://vector.com/int/en/products/products-a-z/software/capl/capl-function-library/) - The official bible.
- [CANoe Demo Download](https://www.vector.com/int/en/download/canoe-demo-17-windows/) - Try it for free.
