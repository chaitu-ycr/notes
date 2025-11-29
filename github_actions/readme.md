
# 🤖 GitHub Actions — Practical Guide

Think of GitHub Actions as the automation engine inside your repo: small YAML files that run tests, build artifacts, and deploy — without leaving GitHub.

🚀 Quick win: This guide adds practical how-tos, production tips (security, self-hosted runners), local testing, troubleshooting steps, and copy-paste workflow examples under `github_actions/examples/`.

---

**What this guide contains:**
- **Quick Start:** create your first workflow in minutes.
- **Examples:** copy-paste workflows for Node.js, Python, and C++.
- **Runner types:** GitHub-hosted vs self-hosted, labels and usage.
- **Security:** secrets, permission scoping, and best practices.
- **Caching & performance:** dependency caches, artifacts, and parallelism.
- **Local testing & debugging:** tools and techniques (e.g., `act`).
- **Troubleshooting:** common failures and fixes.

---

## 🚀 Quick Start (copy-paste)

1) Create `.github/workflows/hello-world.yml` in your repo.

2) Minimal workflow (copy-paste):

```yaml
name: Hello World Workflow
on: [push]
jobs:
  say-hello:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Greet
        run: echo "Hello, World! This ran in GitHub Actions."
```

3) Commit and push; check the Actions tab for the run.

---

## 🧩 Runners: GitHub-hosted vs Self-hosted

- **GitHub-hosted:** quick to start, maintained by GitHub (`ubuntu-latest`, `windows-latest`, `macos-latest`). Good for most CI needs.
- **Self-hosted runners:** run on your infra for specialized hardware, tooling, or isolated networks (HIL benches, automotive test rigs). Use labels to target them.

Example targeting a self-hosted runner:

```yaml
jobs:
  build:
    runs-on: [self-hosted, linux, hil-bench]
    steps: ...
```

Keep self-hosted runners patched, limit inbound access, and use ephemeral runners where possible.

---

## 🔐 Security & Secrets (practical)

- **Use `secrets`:** add secrets in repo/org settings and reference with `${{ secrets.MY_SECRET }}`.
- **Least privilege:** set workflow `permissions` to the minimal scopes needed.
- **Avoid secrets in logs:** mask or avoid printing secrets; use `env`/`secrets` carefully.
- **Protect branches & environments:** require approvals for production deployments and use `environments` with required reviewers.

Example: limit permissions and use secrets

```yaml
permissions:
  contents: read
  id-token: write

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Use secret
        run: echo "${{ secrets.MY_DEPLOY_KEY }}" | base64 --decode > key.pem
```

For enterprise-grade secrets, consider using HashiCorp Vault or cloud provider secret managers with short-lived tokens.

---

## ⚡ Performance: Caching & Artifacts

- **Cache dependencies:** use `actions/cache` to speed up builds (npm, pip, gradle, etc.).
- **Upload artifacts:** store binaries, test results, coverage reports with `actions/upload-artifact`.
- **Parallelize tests:** use matrix strategies or split tests across jobs to reduce wall-clock time.

Cache example (npm):

```yaml
- name: Cache node modules
  uses: actions/cache@v4
  with:
    path: ~/.npm
    key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
    restore-keys: |
      ${{ runner.os }}-node-
```

---

## 🧰 Reusable Workflows & Actions

- **Reusable workflows:** call workflows from other workflows using `workflow_call` for DRY pipelines.
- **Composite actions:** bundle common shell steps into a reusable action.
- **Marketplace actions:** prefer well-maintained actions; prefer pinned versions (`@v3` or commit SHA).

Example `workflow_call` usage:

```yaml
# .github/workflows/ci.yml
on:
  workflow_call:
    inputs:
      repo:
        required: true
        type: string
jobs:
  build:
    runs-on: ubuntu-latest
    steps: ...
```

---

## 🐞 Local Testing & Debugging

- **`act`**: run workflows locally for quick iteration (not perfect for GitHub-hosted specifics).
- **Verbose logs:** add `ACTIONS_RUNNER_DEBUG` and `ACTIONS_STEP_DEBUG` as repository secrets to get more debugging info (use sparingly).

Local `act` example:

```bash
# install act, then run the workflow
act -P ubuntu-latest=nektos/act-environments-ubuntu:18.04 -j say-hello
```

---

## 🐛 Troubleshooting (common failures)

- **Workflow stuck/queued:** Check concurrency limits, billing limits, and runner availability.
- **Authentication / permission errors:** Ensure `GITHUB_TOKEN` has needed permissions and any used secrets are set at org/repo level.
- **Matrix job failures on one axis:** re-run single job, inspect environment differences, pin tool versions.
- **Service container issues:** ensure ports don't conflict and waits are used before tests connect.

Quick check-list:
- Check Actions tab logs and job-level steps.
- Reproduce with `act` or the same Docker image locally.
- Verify secret values and branch protections.

---

## 🚗 Automotive & HIL notes

GitHub Actions can orchestrate HIL runs if your runners have network access to the lab or you use self-hosted runners colocated with the benches. Typical pattern:

- Use a scheduled/nightly workflow that triggers a self-hosted runner attached to the HIL lab.
- Archive test reports, logs and artifact images for traceability (useful for ASPICE evidence).

Example snippet to trigger HIL job on a labeled runner:

```yaml
jobs:
  hil-run:
    runs-on: [self-hosted, linux, hil-bench]
    steps:
      - uses: actions/checkout@v3
      - name: Run HIL tests
        run: run-hil-tests --config tests/hil_config.yaml
      - name: Publish results
        uses: actions/upload-artifact@v3
        with:
          name: hil-reports
          path: reports/
```

---

## 📂 Examples (in-repo)

See `github_actions/examples/` for copy-paste workflows:

1) **Node.js CI** (`examples/nodejs_ci_workflow.yml`)
   - Node.js CI with cache & artifacts.

2) **Python CI** (`examples/python_ci_workflow.yml`)
   - Python pytest matrix example.

3) **C++ CI** (`examples/cpp_ci_workflow.yml`)
   - CMake build in Docker.

4) **Scheduled / Nightly** (`examples/scheduled_workflow.yml`)
   - Cron trigger example.

5) **Manual Trigger** (`examples/manual_trigger_workflow.yml`)
   - `workflow_dispatch` with input parameters.

6) **Secure Secrets** (`examples/secrets_usage_workflow.yml`)
   - Best practices for using secrets.

7) **Deployment** (`examples/deployment_workflow.yml`)
   - Multi-stage deployment with environment protection rules.

8) **Composite Action** (`examples/composite_action/action.yml`)
   - Reusable action example.

---

## 🔗 Resources

- Official docs: https://docs.github.com/en/actions
- Marketplace: https://github.com/marketplace?type=actions
- `act` tool: https://github.com/nektos/act

---

## ✅ Next steps

- Try the Node.js or C++ example by adding the workflow file to `.github/workflows/` in your repo.
- Explore `examples/` for more advanced patterns like deployment and composite actions.
