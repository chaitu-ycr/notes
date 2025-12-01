# 🔰 CAN Bus Introduction

## What is CAN?
**Controller Area Network (CAN)** is a robust vehicle bus standard designed to allow microcontrollers and devices to communicate with each other's applications without a host computer. It is a message-based protocol, designed originally for multiplex electrical wiring within automobiles to save on copper, but it is also used in many other contexts.

## 📜 History
- **1983:** Bosch begins developing CAN.
- **1986:** Protocol officially released.
- **1993:** ISO 11898 standard published.
- **2012:** CAN FD (Flexible Data-rate) introduced.

## 🚀 Why Use CAN?
Before CAN, automotive electronics used point-to-point wiring.
*   **The Problem:** As the number of ECUs increased (Engine, Transmission, ABS, Windows, Radio...), the wiring harness became massive, heavy, and expensive.
*   **The Solution:** CAN uses a single twisted pair of wires (High and Low) connecting all ECUs.

### Key Benefits
1.  **Low Cost:** Reduces wiring weight and complexity.
2.  **Robustness:** High immunity to electrical interference (EMI).
3.  **Efficiency:** Message-based priority ensures critical data gets through first.
4.  **Flexibility:** Easy to add new nodes without rewiring the whole system.

## 🌍 Applications
*   **Automotive:** Engine management, body control, safety systems.
*   **Industrial:** Factory automation, elevator control.
*   **Aerospace:** Avionics data buses.
*   **Medical:** MRI machines, operating room equipment.

![CAN Network Topology](data/can_network.png)

## 🧠 Core Concepts Overview
*   **Multi-Master:** Any node can start transmitting when the bus is free.
*   **Broadcast:** All nodes receive all messages; filters determine relevance.
*   **Event-Driven:** Messages are sent when events occur (or periodically).
