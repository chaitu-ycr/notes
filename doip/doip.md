---
title: "DoIP"
aliases:
  - "DoIP"
---
# 🌐 DoIP: Supercharging Car Diagnostics with Ethernet

Welcome to Diagnostics over Internet Protocol (DoIP)! As cars become more like computers on wheels, the amount of data needed for diagnostics, software updates, and testing has exploded. The traditional CAN bus, while reliable, can be too slow for these tasks. DoIP is the solution.

Think of DoIP as a **high-speed network gateway** that allows you to run standard diagnostic protocols (like UDS) over the fast and familiar TCP/IP and Ethernet protocols. It's the bridge that connects the robust world of automotive diagnostics to the high-speed world of IT infrastructure.

This guide will introduce you to the core concepts of DoIP and walk you through a typical diagnostic session.

## 🔗 Related topics

- [CAN](../can/can.md) — DoIP carries diagnostic traffic over Ethernet and often bridges the vehicle bus
- [UDS](../uds/uds.md) — the diagnostic protocol that runs inside DoIP sessions
- [Intrusion Detection System](../projects/IDS/IDS.md) — security monitoring around diagnostic and gateway traffic
- [Vector CANoe](../vector_canoe/vector_canoe.md) — a common tool for validating vehicle networking and diagnostics
- [Testing](../testing/testing.md) — protocol validation, regression checks, and diagnostic replay workflows

## 🧩 The Building Blocks: Core Concepts Explained

Before we walk through a session, let's learn the key vocabulary.

*   **DoIP Gateway:** A central ECU in the vehicle with an Ethernet connection. It acts as a router, forwarding diagnostic messages from an external tool to the correct internal ECU on other buses (like CAN).
*   **DoIP Node:** Any ECU on the internal vehicle network that is accessible through the DoIP Gateway.
*   **Vehicle Announcement:** A UDP broadcast message sent out by the DoIP Gateway when it's "awake" and ready to be discovered. This is how a diagnostic tool knows a vehicle is on the network.
*   **Routing Activation:** The process of telling the DoIP Gateway that you want to establish a dedicated diagnostic session with a specific ECU. This is a necessary security and resource management step before you can send UDS commands.

## 💡 Practical Use Cases

### Example 1: ECU Flashing over DoIP

The biggest advantage of DoIP is speed. Flashing a modern ECU (like an infotainment system) can involve hundreds of megabytes of data.
*   **Over CAN:** This could take over an hour.
*   **Over DoIP:** This can be done in just a few minutes.
The process follows the same steps: discover, connect, activate a route to the ECU you want to flash, and then use UDS commands to transfer the data at high speed.

### Example 2: DoIP vs. Traditional CAN Diagnostics

| Feature | Traditional CAN Diagnostics | DoIP |
|---|---|---|
| **Speed** | Slow (max 1 Mbps) | Fast (100+ Mbps) |
| **Connection** | Requires specific CAN hardware (e.g., a VN1630) | Uses standard Ethernet ports and cables |
| **Discovery** | No standard discovery mechanism | Built-in UDP discovery |
| **Use Case** | Good for routine diagnostics, reading DTCs | Essential for large data transfers (flashing, logging) and remote diagnostics |

## 🔗 Further Reading

*   [ISO 13400-2:2019](https://www.iso.org/standard/72342.html) (The official standard)


