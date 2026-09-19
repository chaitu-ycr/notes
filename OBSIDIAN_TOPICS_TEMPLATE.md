---
title: "Obsidian Topic Standards"
aliases:
  - "Obsidian Topic Standards"
---

# Obsidian Topic Standards

This repository follows a simple pattern for every future topic so the vault stays connected, searchable, and graph-friendly.

## Required structure for every topic note

Every major topic should have these sections:

1. Title and tags
   - Add 3–6 tags relevant to the topic domain.
   - Example: #can #automotive #embedded #network

2. Short intro paragraph
   - Explain what the topic is and why it matters.
   - Keep it brief and practical.

3. Related topics section
   - Add a short block of links to adjacent topics.
   - Link both upstream and downstream concepts.

4. Core concepts section
   - Explain the main ideas in simple, digestible sections.

5. Practical examples or workflows
   - Add examples, commands, or steps when relevant.

6. References or further reading
   - Link to standards, docs, or adjacent notes in the vault.

## Required link pattern

Use relative links in the repo and Obsidian-style note links when appropriate.

Examples:
- [[can/readme|CAN]]
- [[uds/readme|UDS]]
- [[testing/readme|Testing]]
- [Git](git/git.md)

## Minimum graph design rule

Every topic note must connect to at least 3 related notes in the vault.

Recommended connection pattern:
- parent concept
- adjacent concept
- practical application or validation topic

## Example block for future notes

```md
## Related topics

- [[can/readme|CAN]] — the underlying bus communication layer
- [[uds/readme|UDS]] — diagnostic services on top of CAN
- [[testing/readme|Testing]] — validation and regression of behavior
```

## Standard tags to use

Use topic-specific tags plus a few shared vault tags:
- #automotive
- #embedded
- #software
- #testing
- #devops
- #python
- #network
- #obsidian
- #knowledge-base

## Repo rule

When adding a new folder or note, always ask:
- What is the parent concept?
- What is the adjacent concept?
- What does this validate or enable?
- Which note should link back to this one?

If those three connections exist, the vault remains useful in Obsidian.



