# 📂 CAPL Examples

This directory contains ready-to-use CAPL scripts for various scenarios. Copy, paste, and adapt them to your CANoe/CANalyzer projects.

## 📡 Communication

| File | Description |
|------|-------------|
| **[hello_world.can](hello_world.can)** | Basic syntax, timers, and message transmission. |
| **[periodic_message.can](periodic_message.can)** | Send a message cyclically (e.g., every 100ms). |
| **[keyboard_control.can](keyboard_control.can)** | Trigger messages manually using keyboard shortcuts. |
| **[sysvar_reaction.can](sysvar_reaction.can)** | React to system variable changes (e.g., from a panel). |

## 🧠 Logic & Processing

| File | Description |
|------|-------------|
| **[data_types.can](data_types.can)** | Examples of all CAPL data types (int, float, arrays, maps). |
| **[user_functions.can](user_functions.can)** | Defining and calling custom functions. |
| **[string_manipulation.can](string_manipulation.can)** | Handling strings, formatting, and parsing. |
| **[array_processing.can](array_processing.can)** | Working with arrays and message buffers. |
| **[error_handling.can](error_handling.can)** | Handling bus-off events and invalid data. |
| **[event_handlers.can](event_handlers.can)** | Examples of `on start`, `on message`, `on signal`, etc. |

## 🧪 Testing & Diagnostics

| File | Description |
|------|-------------|
| **[test_case_signal.can](test_case_signal.can)** | Test module to validate signal ranges. |
| **[test_case_diag.can](test_case_diag.can)** | Test module to send UDS requests and check responses. |
| **[window_capture.can](window_capture.can)** | Capture screenshots of CANoe windows for reports. |

## 🔧 Utilities

| File | Description |
|------|-------------|
| **[logging_example.can](logging_example.can)** | Writing formatted logs to the Write Window. |
| **[exec_external.can](exec_external.can)** | Execute external programs (Python, batch) from CAPL. |

---

## 🚀 How to Use

1.  **Open CANoe.**
2.  **Simulation Setup:** Right-click a node -> "Configuration".
3.  **Load File:** Browse and select one of these `.can` files.
4.  **Compile:** Press F9 or click the Compile button.
5.  **Run:** Start the measurement!
