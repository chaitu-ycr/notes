---
title: "Knowledge Vault Home"
---

---
aliases:
  - Notes
  - Repo Home
  - Knowledge Vault
tags:
  - #obsidian
  - #knowledge-base
  - #automotive
  - #embedded
---

# Knowledge Vault Home

This vault is a structured learning repository for automotive software, embedded systems, testing, tooling, and software engineering. It is designed for fast exploration in Obsidian and strong graph-based connection building.

## Primary clusters

### Automotive and diagnostics
- [[can/readme|CAN]]
- [[uds/readme|UDS]]
- [[doip/readme|DoIP]]
- [[projects/IDS/readme|IDS]]
- [[vector_capl/readme|Vector CAPL]]
- [[vector_canoe/readme|Vector CANoe]]
- [[vector_hardware/readme|Vector Hardware]]

### Software engineering and delivery
- [[git/readme|Git]]
- [[integration/readme|Integration]]
- [[github_actions/readme|GitHub Actions]]
- [[jenkins/readme|Jenkins]]
- [[yaml/readme|YAML]]
- [[plantuml/readme|PlantUML]]
- [[cmake/readme|CMake]]
- [[conan/readme|Conan]]

### Programming and quality
- [[python/readme|Python]]
- [[bash/readme|Bash]]
- [[testing/readme|Testing]]
- [[sdlc/readme|SDLC]]
- [[aspice/readme|ASPICE]]

## Strong graph connections

- CAN -> UDS -> DoIP -> IDS
- CAN -> CAPL -> CANoe -> Validation
- CAN -> Vector hardware -> ECU stimulus -> system test
- Testing -> SDLC -> ASPICE -> Quality processes
- Python -> Bash -> YAML -> Git -> CI/CD
- Git -> Integration -> Automation -> Delivery

## Recommended Obsidian workflow

Start on one of these paths depending on the goal:
- Diagnostics and automotive networking: CAN → UDS → DoIP → IDS
- ECU validation and simulation: CAN → CAPL → CANoe → Testing
- Build and delivery workflow: Git → GitHub Actions / Jenkins → Integration → Testing
- Quality and process improvement: Testing → SDLC → ASPICE


1. Open this note first.
2. Follow the cluster you need.
3. Use the Backlinks panel to discover adjacent concepts.
4. Keep notes focused on one concept; let graph view connect the topics.
5. Prefer relative cross-links like [[can/readme]] and [[testing/readme]] instead of disconnected one-off documents.
6. Keep the vault grounded in the existing notes already in the repo rather than creating speculative branches.

## Quick links

- [[README|Repository landing page]]
- [[can/readme|CAN guide]]
- [[uds/readme|UDS guide]]
- [[testing/readme|Testing guide]]
- [[integration/readme|Integration toolkit]]


