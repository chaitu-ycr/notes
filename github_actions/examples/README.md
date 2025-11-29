## GitHub Actions examples

This folder contains ready-to-use workflow examples you can copy to `.github/workflows/` or point to from other repos.

Files:

**CI Workflows:**
- `nodejs_ci_workflow.yml` — Node.js CI (checkout, cache, test, upload artifacts)
- `python_ci_workflow.yml` — Python matrix with `actions/setup-python` and pytest
- `cpp_ci_workflow.yml` — C++ CMake build using Docker runner

**Advanced Workflows:**
- `scheduled_workflow.yml` — Cron trigger example (nightly builds)
- `manual_trigger_workflow.yml` — `workflow_dispatch` with input parameters
- `secrets_usage_workflow.yml` — Secure secrets usage example
- `deployment_workflow.yml` — Deployment with environment protection rules
- `composite_action/action.yml` — Reusable composite action example

Usage:

1. Copy one of the YAML files into your repo's `.github/workflows/` folder.
2. Adjust paths, test commands, and secrets as needed.
3. Commit and push; inspect runs in the Actions tab.

Local testing tip: use `act` for quick iterations; for final verification run on GitHub-hosted runners.
