---
title: "Projects"
aliases:
  - "Projects"
---
# Projects

This folder groups the main automotive system and vehicle-function project notes already present in the repo. The goal is to keep each project understandable on its own while still connecting it to the larger automotive and validation graph.

## Project clusters

### Vehicle safety and drivability
- [ABS](ABS/readme.md) — anti-lock braking system behavior and validation
- [BMS](BMS/readme.md) — battery safety, balancing, and monitoring
- [IPC](IPC/readme.md) — instrument panel cluster and driver information delivery

### ADAS and autonomy
- [ADAS](ADAS/readme.md) — advanced driver assistance systems overview
- [MFC](ADAS/MFC/readme.md) — multi-function camera for perception and lane/object detection
- [CEM](ADAS/CEM/readme.md) — collision evasion maneuver logic
- [RVC](ADAS/RVC/readme.md) — rear view camera and parking safety assistance

### Diagnostics and security
- [IDS](IDS/readme.md) — intrusion detection and vehicle network security monitoring

## How these projects connect

- ABS ↔ BMS ↔ IPC are core vehicle function and safety topics
- ADAS ↔ MFC ↔ CEM ↔ RVC form the perception and automation cluster
- IDS connects to CAN, UDS, DoIP, and testing as the security/validation layer
- All project notes relate back to the automotive bus and validation stack: [CAN](../can/can.md), [UDS](../uds/uds.md), [Testing](../testing/testing.md)

## Related repo topics

- [CAN](../can/can.md)
- [UDS](../uds/uds.md)
- [DoIP](../doip/doip.md)
- [Vector CANoe](../vector_canoe/vector_canoe.md)
- [Vector CAPL](../vector_capl/vector_capl.md)
- [Testing](../testing/testing.md)
- [SDLC](../sdlc/sdlc.md)



