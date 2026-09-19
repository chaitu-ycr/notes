---
title: "Jenkins"
aliases:
  - "Jenkins"
---
# 🤖 Jenkins: The Original Automation Butler — Practical Guide

CAN is like a crowded dinner table and Jenkins is the head waiter who remembers who ordered what. If your release process involves repeating manual steps, Jenkins will do them reliably and faster.

🚀 Quick win: This file shows how to get a pipeline running, real-world examples (Node.js, Docker), security hardening pointers, and troubleshooting tips you can copy-paste.

## 🔗 Related topics

- [GitHub Actions](../github_actions/github_actions.md) — managed CI/CD alternative
- [Git](../git/git.md) — version control backbone of the delivery pipeline
- [YAML](../yaml/yaml.md) — pipeline configuration syntax
- [Docker / integration patterns](../integration/integration.md) — tooling and deployment flow
- [Testing](../testing/testing.md) — quality gates and automated validation

## 🤔 Why Jenkins (short)

- **Flexible & self-hosted:** run anywhere and integrate with almost anything via plugins.
- **Pipelines-as-code:** reproducible CI/CD via a `Jenkinsfile` in your repo.
- **Scale with agents:** add workers with different toolchains (Windows, Linux, macOS, ARM).

Use Jenkins when you need full control, custom integrations, or self-hosted enterprise CI/CD. If you want a fully managed CI solution (no infra), consider GitHub Actions / GitLab CI first.

## 🧩 Key Concepts (practical)

- **Controller (master):** Orchestrates jobs, stores config; keep it light — don't run heavy builds here.
- **Agent (node):** Execute builds; identify agents with `labels` (e.g., `linux`, `windows`, `docker`).
- **Jenkinsfile:** Pipeline-as-code; prefer Declarative pipelines for readability and safety.
- **Stages & Steps:** Use stages for major milestones; steps for commands.

## 🔧 Controller vs Agents — Practical Tips

- **Never run heavy builds on the controller.** Keep controller for orchestration, not CPU-heavy workloads.
- **Label your agents.** Use labels like `linux`, `arm`, `windows`, `gpu` and target them in the `agent { label 'linux' }` block.
- **Ephemeral agents:** Use Kubernetes or Docker agents for clean, reproducible environments and to avoid flaky state.

Example label usage:

```groovy
pipeline { agent { label 'linux && docker' } ... }
```

## 🧰 Recommended Plugins (starter list)

- **Pipeline** (core pipelines support)
- **Credentials Binding Plugin** (manage secrets)
- **Blue Ocean** (modern UI)
- **Git / GitHub / GitLab** integrations
- **Docker Pipeline** (docker build/push inside pipelines)
- **Kubernetes** (ephemeral agents)
- **Matrix Authorization Strategy** (fine-grained security)
- **Job DSL / Shared Libraries** (DRY pipelines)

Install only what you need; each plugin increases your maintenance surface.

## 🐛 Troubleshooting Stories & Gotchas

⚠️ Common symptom: "Job never leaves queued" — means no matching agent or labels mismatch.

Hunt checklist:
- Check agent connected status (Manage Jenkins → Nodes).
- Confirm labels match pipeline `agent { label '...' }`.
- Check resource availability on agents (disk, memory).

Symptom: "Checkout fails with permission" — likely SSH key or credentials misconfigured.

Symptom: "Build works locally but fails on Jenkins" — usually environment mismatch; use Docker agents or replicate environment using the same image.

Mini troubleshooting example: build passes locally but fails in Jenkins due to missing `NPM_TOKEN`.

Fix:
1. Add `NPM_TOKEN` to Jenkins Credentials.
2. Use `withCredentials` to inject during `npm ci`.

## 🔗 Resources & Further Reading

- **Official docs:** https://www.jenkins.io/doc/
- **Pipeline syntax:** https://www.jenkins.io/doc/book/pipeline/syntax/
- **Best practices:** https://www.jenkins.io/doc/book/pipeline/best-practices/
- **Blue Ocean:** https://www.jenkins.io/projects/blueocean/

---

## ✅ Done — Next steps

- Try the Node.js or Docker example by adding a `Jenkinsfile` to your repo and creating a Pipeline job in Jenkins.
- Explore the `examples/` folder for more specific use cases.


