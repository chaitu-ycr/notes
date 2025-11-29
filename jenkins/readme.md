# 🤖 Jenkins: The Original Automation Butler — Practical Guide

CAN is like a crowded dinner table and Jenkins is the head waiter who remembers who ordered what. If your release process involves repeating manual steps, Jenkins will do them reliably and faster.

🚀 Quick win: This file shows how to get a pipeline running, real-world examples (Node.js, Docker), security hardening pointers, and troubleshooting tips you can copy-paste.

---

**What this guide contains:**
- **Why Jenkins:** short rationale and when to pick it.
- **Quick Start:** create a `Jenkinsfile` and run a pipeline in minutes.
- **Examples:** Declarative pipelines for common use-cases.
- **Architecture & Agents:** Controller vs Agent, labels, Docker.
- **Security & Credentials:** practical hardening suggestions.
- **Plugins & Extensibility:** recommended plugins and patterns.
- **Troubleshooting & Pro Tips:** reproducible fixes and gotchas.

---

## 🤔 Why Jenkins (short)

- **Flexible & self-hosted:** run anywhere and integrate with almost anything via plugins.
- **Pipelines-as-code:** reproducible CI/CD via a `Jenkinsfile` in your repo.
- **Scale with agents:** add workers with different toolchains (Windows, Linux, macOS, ARM).

Use Jenkins when you need full control, custom integrations, or self-hosted enterprise CI/CD. If you want a fully managed CI solution (no infra), consider GitHub Actions / GitLab CI first.

---

## 🚀 Quick Start (copy-paste)

1) Add a `Jenkinsfile` to your repo root.

2) Minimal Declarative pipeline (Copy-Paste):

```groovy
pipeline {
    agent any
    stages {
        stage('Build') { steps { echo 'Building...' } }
        stage('Test')  { steps { echo 'Testing...'  } }
        stage('Deploy'){ steps { echo 'Deploying...' } }
    }
}
```

3) In Jenkins: New Item → Pipeline → choose "Pipeline script from SCM" → set your repo URL → Script Path `Jenkinsfile` → Save → Build Now.

If this fails, open the job Console Output and check agent connectivity and workspace checkout.

---

## 🧩 Key Concepts (practical)

- **Controller (master):** Orchestrates jobs, stores config; keep it light — don't run heavy builds here.
- **Agent (node):** Execute builds; identify agents with `labels` (e.g., `linux`, `windows`, `docker`).
- **Jenkinsfile:** Pipeline-as-code; prefer Declarative pipelines for readability and safety.
- **Stages & Steps:** Use stages for major milestones; steps for commands.

---

## 💡 Practical Jenkinsfile Examples

1) **Node.js CI** (`examples/nodejs_pipeline.jenkinsfile`)
   - Checkout, install, test, archive artifacts.

2) **Docker Agent** (`examples/docker_build_pipeline.jenkinsfile`)
   - Run build inside a Docker container for reproducibility.

3) **Matrix Build** (`examples/matrix_build_pipeline.jenkinsfile`)
   - Run tests across multiple Node.js versions in parallel.

4) **C++ Pipeline** (`examples/cpp_pipeline.jenkinsfile`)
   - CMake build inside a GCC Docker container.

5) **Python Pipeline** (`examples/python_pipeline.jenkinsfile`)
   - Python testing with pytest.

6) **Scheduled / Nightly Build** (`examples/scheduled_pipeline.jenkinsfile`)
   - Cron trigger example for nightly regression tests.

7) **Input Parameters** (`examples/input_parameters_pipeline.jenkinsfile`)
   - Build with user-defined parameters (checkboxes, dropdowns).

8) **Deployment Pipeline** (`examples/deployment_pipeline.jenkinsfile`)
   - Multi-stage deployment with manual approval gate for production.

---

## 🔧 Controller vs Agents — Practical Tips

- **Never run heavy builds on the controller.** Keep controller for orchestration, not CPU-heavy workloads.
- **Label your agents.** Use labels like `linux`, `arm`, `windows`, `gpu` and target them in the `agent { label 'linux' }` block.
- **Ephemeral agents:** Use Kubernetes or Docker agents for clean, reproducible environments and to avoid flaky state.

Example label usage:

```groovy
pipeline { agent { label 'linux && docker' } ... }
```

---

## 🔐 Security & Credentials — Practical Hardening

⚠️ Jenkins is powerful — treat it like a critical service.

- **Enable security:** Use Matrix-based security or integrate with LDAP/AD/OAuth.
- **Use Credentials Plugin:** Never store secrets in the `Jenkinsfile` or repo. Use `credentials()` and `withCredentials`.
- **Least privilege:** Give agents and users the least privileges required.
- **Update plugins & core regularly:** Many attacks target outdated plugins.
- **CSRF & CLI:** Keep CLI access and remote API tokens restricted.

Example of using credentials safely:

```groovy
pipeline {
    agent any
    stages {
        stage('Deploy') {
            steps {
                withCredentials([string(credentialsId: 'aws-secret', variable: 'AWS_SECRET')]) {
                    sh 'deploy-script --secret $AWS_SECRET'
                }
            }
        }
    }
}
```

---

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

---

## 🏁 Best Practices (short checklist)

- **Pipeline as Code:** Keep `Jenkinsfile` in repo.
- **Small, focused stages:** Easier to debug and retry.
- **Artifacts & test reports:** Archive and publish test reports and coverage.
- **Immutable agents:** Prefer containers/k8s for reproducibility.
- **Secrets management:** Use Credentials store, HashiCorp Vault, or cloud secrets.
- **Shared Libraries:** Factor common steps into shared libraries.

---

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

---

## 🚗 Automotive Context (real-world example)

If you're working on automotive software (CAN, UDS, HIL), Jenkins pipelines are great for automating:
- nightly builds with regression tests on HIL benches,
- automated flashing steps using secure artifact storage,
- generating release notes and traceability artifacts for ASPICE compliance.

Example: nightly HIL run pipeline stage

```groovy
stage('HIL Test') {
    agent { label 'hil-bench' }
    steps {
        sh 'run-hil-tests --config tests/hil_config.yaml'
        junit 'reports/hil-*.xml'
    }
}
```

Pro tip: store bench-specific runners as ephemeral VMs/containers to avoid state bleed between runs.

---

## 🔗 Resources & Further Reading

- **Official docs:** https://www.jenkins.io/doc/
- **Pipeline syntax:** https://www.jenkins.io/doc/book/pipeline/syntax/
- **Best practices:** https://www.jenkins.io/doc/book/pipeline/best-practices/
- **Blue Ocean:** https://www.jenkins.io/projects/blueocean/

---

## ✅ Done — Next steps

- Try the Node.js or Docker example by adding a `Jenkinsfile` to your repo and creating a Pipeline job in Jenkins.
- Explore the `examples/` folder for more specific use cases.
