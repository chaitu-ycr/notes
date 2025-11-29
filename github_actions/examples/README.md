## GitHub Actions examples

This folder contains ready-to-use workflow examples you can copy to `.github/workflows/` or point to from other repos.

Files:
- `nodejs-ci.yml` — Node.js CI (checkout, cache, test, upload artifacts)
- `python-ci.yml` — Python matrix with `actions/setup-python` and pytest
- `cpp-ci.yml` — C++ CMake build using Docker runner

Usage:

1. Copy one of the YAML files into your repo's `.github/workflows/` folder.
2. Adjust paths, test commands, and secrets as needed.
3. Commit and push; inspect runs in the Actions tab.

Local testing tip: use `act` for quick iterations; for final verification run on GitHub-hosted runners.
