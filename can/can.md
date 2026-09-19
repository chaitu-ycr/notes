---
title: "🚌 Controller Area Network (CAN): The Complete Guide"
aliases:
  - "🚌 Controller Area Network (CAN): The Complete Guide"
---
# 🚌 Controller Area Network (CAN): The Complete Guide

#can #automotive #network #embedded #vehicle-bus

> **"From 0V to 5V, and everything in between."** — *Antigravity*

Welcome to the ultimate guide on the CAN protocol. We have structured this documentation to take you from a complete beginner to a protocol expert.

## 🗺️ CAN folder map

This folder is organized into two connected learning tracks:

- [Concepts](concepts/readme.md) — the protocol fundamentals, layer behavior, timing, and error handling
- [Examples](examples/notes.md) — practical logs, DBC snippets, and Python scripts for real CAN workflows

Use the concepts section to understand the protocol, then use the examples directory to apply it in traffic capture, decoding, and test automation.

## � Documentation Structure

We have organized the concepts into logical levels to avoid information overload.

### 🟢 Level 1: The Basics
*Start here to understand the "What" and "Why".*

*   **[01_introduction.md](concepts/01_introduction.md)**
    *   What is CAN? History, benefits, and applications.
    *   *Key Visual:* Network Topology.
*   **[02_physical_layer.md](concepts/02_physical_layer.md)**
    *   Differential signaling (CAN_H, CAN_L).
    *   Termination (120Ω).
    *   *Key Visuals:* Bus Logic, Encoding, Oscilloscope View.
*   **[03_frame_structure.md](concepts/03_frame_structure.md)**
    *   Standard vs. Extended Frames.
    *   Bit Stuffing rules.
    *   *Key Visuals:* Frame Layout, Bit Stuffing.

### � Level 2: The Protocol Logic
*Understand the "How".*

*   **[04_arbitration.md](concepts/04_arbitration.md)**
    *   CSMA/CR and Priority.
    *   Why Dominant (0) beats Recessive (1).
*   **[05_error_handling.md](concepts/05_error_handling.md)**
    *   Error Types (Bit, Stuff, CRC, Form, ACK).
    *   Error States (Active, Passive, Bus Off).
    *   *Key Visuals:* Error Frames, State Machine Diagram.

### 🔴 Level 3: The Expert Zone
*Deep dives for debugging and validation.*

*   **[06_bit_timing.md](concepts/06_bit_timing.md)**
    *   Time Quanta (tq) and Segments (Sync, Prop, Phase).
    *   Sample Points and Synchronization Jump Width (SJW).
*   **[07_can_fd.md](concepts/07_can_fd.md)**
    *   Flexible Data-rate features.
    *   BRS (Bit Rate Switch) and ESI (Error State Indicator).

## ⚡ Quick Reference

| Feature | Description |
| :--- | :--- |
| **Voltages** | Dom: 3.5V/1.5V (Diff 2V) \| Rec: 2.5V/2.5V (Diff 0V) |
| **Termination** | 120Ω at both ends (60Ω total parallel) |
| **Logic** | 0 (Dominant) overwrites 1 (Recessive) |
| **Max Payload** | 8 Bytes (Classic) \| 64 Bytes (FD) |
| **Max Speed** | 1 Mbit/s (Classic) \| 5-8 Mbit/s (FD Data) |

## 🔗 Related topics

- [UDS](../uds/uds.md) — the diagnostic layer above CAN communication
- [DoIP](../doip/doip.md) — automotive network transport for diagnostics and flashing
- [Vector CAPL](../vector_capl/vector_capl.md) — simulate or instrument CAN networks
- [Vector CANoe](../vector_canoe/vector_canoe.md) — analysis and validation environment
- [Intrusion Detection System](../projects/IDS/IDS.md) — security monitoring for vehicle networks
- [Testing](../testing/testing.md) — how to validate CAN behavior and regressions



