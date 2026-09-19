---
title: "Notes"
aliases:
  - "Notes"
---
# Notes

This repository is a learning vault for automotive software, embedded systems, testing, tooling, and engineering knowledge. It is structured for quick browsing in Obsidian and for building a clean graph of concepts and topics.

#automotive #embedded #testing #software #knowledge-base #obsidian

## Start here

- [Home](Home.md)
- [CAN](can/can.md)
- [UDS](uds/uds.md)
- [DoIP](doip/doip.md)
- [Vector CAPL](vector_capl/vector_capl.md)
- [Vector CANoe](vector_canoe/vector_canoe.md)
- [Python](python/python.md)
- [Git](git/git.md)
- [Integration](integration/integration.md)
- [Testing](testing/testing.md)
- [ASPICE](aspice/aspice.md)

## Topic clusters

### Automotive and embedded systems
- [CAN](can/can.md)
- [UDS](uds/uds.md)
- [DoIP](doip/doip.md)
- [Vehicle security and IDS](projects/IDS/IDS.md)
- [Vector CAPL](vector_capl/vector_capl.md)
- [Vector CANoe](vector_canoe/vector_canoe.md)
- [Vector hardware](vector_hardware/vn_hw_io_piggy.md)

### Recommended Obsidian paths
- CAN → UDS → DoIP → IDS
- CAN → CAPL → CANoe → test validation
- CAN → Vector hardware → ECU stimulus → system test
- Git → GitHub Actions / Jenkins → Testing → SDLC → ASPICE
- Python → Bash → YAML → Integration → Delivery

### Engineering and delivery
- [Git](git/git.md)
- [GitHub Actions](github_actions/github_actions.md)
- [Jenkins](jenkins/jenkins.md)
- [PlantUML](plantuml/plantuml.md)
- [YAML](yaml/yaml.md)
- [CMake](cmake/cmake.md)
- [Conan](conan/conan.md)

### Programming and quality
- [Python](python/python.md)
- [Bash](bash/bash.md)
- [Testing](testing/testing.md)
- [ASPICE](aspice/aspice.md)
- [SDLC](sdlc/sdlc.md)

## Obsidian graph strategy

This vault works best when you navigate from the hub note, then drill into the related topic pages. The strongest graph edges are:

- CAN -> UDS -> DoIP -> IDS
- Testing -> SDLC -> ASPICE -> Quality
- Python -> Bash -> YAML -> Git -> CI/CD
- Vector CAPL -> Vector CANoe -> CAN/UDS workflows
- Projects -> Automotive system patterns -> Diagnostics and security

Use the graph view to explore these clusters and the backlinks panel to see which notes connect to a topic.

## Available topic map

The repo is already organized around real, existing engineering topics. Keep each note connected to its parent cluster and adjacent concepts rather than introducing new speculative topics.

The strongest current graph clusters are:

- Automotive and diagnostics: CAN, UDS, DoIP, IDS, CAPL, CANoe
- Software quality and delivery: Git, GitHub Actions, Jenkins, YAML, PlantUML, testing, SDLC, ASPICE
- Programming and tooling: Python, Bash, CMake, Conan, integration

This keeps the vault grounded in the actual knowledge already in the repo and makes the Obsidian graph useful and reliable.


