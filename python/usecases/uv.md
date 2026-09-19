---
title: "⚡️ Usecase: Supercharging Your Workflow with `uv`"
aliases:
  - "⚡️ Usecase: Supercharging Your Workflow with `uv`"
---

# ⚡️ Usecase: Supercharging Your Workflow with `uv`

> “Waiting for `pip install` is the modern equivalent of watching paint dry, but with more dependency conflicts.”

If you’ve ever waited for a CI pipeline to install `pandas` while your soul quietly left the building, or if you have 14 versions of Python installed and no idea which one is the “real” one, then **`uv` is here to save you**.

---

## 🧭 Workshop framing

You are not reading a reference doc. You are joining a hands-on lab.

This guide is designed to move Python developers from **Zero → Hero** in modern packaging using `uv`, using a sequence of short, teachable modules, live terminal checks, and troubleshooting exercises.

The rule for every module is simple:

1. Learn the idea
2. Run the command
3. Verify the output
4. Explain what changed
5. Solve the failure case

Do not skip the checkpoints.

---

## 🧐 What is `uv`?

Think of `uv` as the **Formula 1 pit crew** for Python projects.

It is an extremely fast, all-in-one package and project manager written in **Rust**. It consolidates the responsibilities of:

- `pip`
- `virtualenv`
- `pip-tools`
- `pyenv`
- project dependency management
- package build orchestration

### Why should you care?

- It is dramatically faster than legacy tooling
- It solves dependency resolution efficiently
- It creates reproducible environments with lock files
- It can manage Python versions and project state cleanly
- It fits directly into modern `pyproject.toml` workflows

---

## 🚀 Quick start: the “just get me moving” path

### 1. Install `uv`

```bash
# macOS / Linux / WSL
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
irm https://astral.sh/uv/install.ps1 | iex
```

### 2. Create a virtual environment

```bash
uv venv
```

### 3. Install packages

```bash
uv pip install fastapi pandas numpy
```

### 4. Run a command without activating the venv

```bash
uv run python --version
```

> Tip: you do not need to activate the environment for most `uv` workflows. `uv run` handles the execution environment for you.

---

## 🛠️ Project-manager workflow

For an actual application or library, use a proper project workflow:

```bash
uv init my-awesome-project
cd my-awesome-project
uv add requests
uv add --group dev pytest
uv run pytest
```

This creates a modern project structure and keeps dependencies managed by the project itself.

---

## 🆚 Old way vs modern way

| Task | Legacy approach | `uv` approach |
| :--- | :--- | :--- |
| Create venv | `python -m venv .venv` | `uv venv` |
| Install package | `pip install pandas` | `uv pip install pandas` |
| Lock dependencies | `pip-compile` | `uv lock` |
| Sync environment | `pip-sync` | `uv sync` |
| Run script | `source .venv/bin/activate && python app.py` | `uv run app.py` |

---

## 💡 Pro tip: script runner mode

You do not always need a full project for a dependency-based script.

Create a file like `script.py`:

```python
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "requests",
#   "rich",
# ]
# ///

import requests
from rich import print

print(requests.get("https://httpbin.org/json").json())
```

Then run:

```bash
uv run script.py
```

`uv` creates a temporary environment, installs the dependencies, runs the script, and cleans up. That is a powerful developer workflow.

---

# 🧪 `uv` workshop: zero → hero in modern Python packaging

> This is not a static cheat sheet. It is a hands-on lab intended to guide developers from initial confusion to packaging confidence.

---

## 🎯 Workshop objectives

By the end of this session, participants should be able to:

- explain the modern packaging stack
- create a project with `uv`
- manage Python versions and environments
- add runtime and development dependencies correctly
- use `uv.lock` for reproducibility
- build a package artifact
- publish to TestPyPI / PyPI
- handle Git-based versioning and monorepo workspaces
- troubleshoot common dependency and install failures

---

## 🧭 The learning model

This workshop moves in small stages.

### Every module includes:

- a concept to understand
- a command to run
- an output check
- a Why it matters explanation
- a troubleshooting prompt

### The trainer rhythm

1. Explain the idea
2. Run the command
3. Confirm the output
4. Ask: “what changed?”
5. Resolve the edge case

If a command fails, that is not a bad thing. It is usually the learning moment.

---

## 🧱 Module 0 — understand the packaging stack

### Why modern packaging changed

Legacy Python packaging was fragmented:

- `pip` installed packages
- `virtualenv` created environments
- `requirements.txt` tracked some dependencies
- `setup.py` handled metadata
- `pip-tools` managed lock files
- `pyenv` handled interpreter versioning

This led to drift, hidden dependency conflicts, and inconsistent environments.

Modern packaging consolidates those concerns into a clearer flow:

```text
Developer
   │
   ▼
uv / pip
   │
   ▼
pyproject.toml
   │
   ▼
build backend
(hatchling / uv_build / flit-core)
   │
   ▼
artifacts (.whl, .tar.gz)
   │
   ▼
PyPI / private index
```

The key standards are:

```text
PEP 517 → build-system interface
PEP 518 → build-system configuration
PEP 621 → package metadata in pyproject.toml
```

A modern project often looks like this:

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "my-package"
version = "0.1.0"
description = "My Python package"
requires-python = ">=3.11"
dependencies = []
```

### Exercise

Open a `pyproject.toml` and answer:

- What is the package name?
- What Python version does it require?
- Where do runtime dependencies live?
- Is this a modern project or a legacy one?

---

## 🚀 Module 1 — initialize a real project

### Step 1: create the project

```bash
uv init --package --python 3.11 --build-backend hatchling
```

If you want the default, simplified version:

```bash
uv init --package
```

### Step 2: inspect the structure

```bash
ls -la
find . -maxdepth 2 -type f | sort
```

Typical layout:

```text
my-project/
├── pyproject.toml
├── README.md
├── src/
│   └── my_package/
│       ├── __init__.py
│       └── main.py
├── tests/
└── .venv/
```

### Why `src/` matters

```text
my-project/
├── pyproject.toml
├── src/
│   └── my_package/
│       └── __init__.py
└── tests/
```

This avoids accidental imports from the repo root and makes the package behave more like it will when installed.

> Rule of thumb: for distributable libraries, prefer the `src/` layout.

### Verification step

```bash
uv run python --version
```

If this works, the project environment is initialized correctly.

### Troubleshooting checklist

If it fails:

- confirm `uv` is installed with `uv --version`
- verify you are in the project folder
- recreate the environment with `uv venv`

---

## 🐍 Module 2 — manage Python versions properly

### List available Python versions

```bash
uv python list
```

### Install a version

```bash
uv python install 3.11
uv python install 3.12
```

### Pin the project to a version

```bash
uv python pin 3.11
```

This creates a `.python-version` file.

### Create a virtual environment explicitly

```bash
uv venv
```

Or:

```bash
uv venv --python 3.11
```

### Activation paths

PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Bash/Zsh:

```bash
source .venv/bin/activate
```

But most projects can skip activation entirely:

```bash
uv run python
uv run pytest
```

### Lab prompt

Run:

```bash
uv python pin 3.11
uv run python --version
```

Then explain what the output tells you.

### Common problem

The shell is using a different interpreter than the project expects.

Check:

- `which python` or `Get-Command python`
- `uv python list`
- `.python-version`
- whether you are in the correct project directory

---

## 📦 Module 3 — dependency lifecycle with `uv add`

### Add a runtime dependency

```bash
uv add requests
```

### Add a version constraint

```bash
uv add "requests>=2.32"
```

### Add an exact version

```bash
uv add "requests==2.32.3"
```

### Remove a dependency

```bash
uv remove requests
```

### Add development tooling

```bash
uv add --group dev pytest
uv add --group dev ruff
uv add --group dev mypy
```

### Add documentation tooling

```bash
uv add --group docs mkdocs
```

This yields a structure like:

```toml
[dependency-groups]
dev = [
    "pytest>=8.0",
    "ruff>=0.8",
    "mypy>=1.0",
]
```

### Why groups matter

It keeps the project clean by separating:

- runtime dependencies
- toolchain/dev dependencies
- documentation dependencies

### Exercise

Add three things:

```bash
uv add rich
uv add --group dev pytest
uv add --group docs mkdocs
```

Then inspect `pyproject.toml` and explain what was added and why.

---

## 🔒 Module 4 — `uv.lock` and reproducibility

### The lock file is the safety net

Run:

```bash
uv lock
```

Then sync:

```bash
uv sync
```

### The idea

```text
pyproject.toml = what the project asks for
uv.lock        = what was actually resolved
```

This avoids the classic “works on my machine” problem.

### Useful commands

```bash
uv tree
uv tree --invert
uv lock --check
```

### Lab prompt

If a dependency is missing or a version conflict appears:

```bash
uv tree
uv tree --invert
```

Ask:

- What am I directly depending on?
- What packages depend on this package?

### Troubleshooting pattern

When resolution fails:

1. inspect the resolver error
2. run `uv tree`
3. check version constraints
4. edit `pyproject.toml`
5. rerun `uv lock` and `uv sync`

---

## 🧩 Module 5 — `src/` layout and import correctness

### Why this matters

A project may work from the repository root but fail when installed as a package.

The `src/` layout reduces import mistakes and keeps packaging behavior closer to real usage.

### Good structure

```text
my_project/
├── pyproject.toml
├── README.md
├── src/
│   └── my_project/
│       ├── __init__.py
│       └── core.py
├── tests/
└── docs/
```

### Exercise

Create a package under `src/` and test it:

```bash
uv run python -c "import my_project; print(my_project)"
```

### Common failure pattern

```text
ModuleNotFoundError: No module named 'my_project'
```

Check:

- package is under `src/`
- project metadata is correct
- you ran `uv sync`
- the environment is active and refreshed

---

## 🛠️ Module 6 — build the artifact, not just the code

### Build command

```bash
uv build
```

This creates files in `dist/`:

```text
dist/
├── my_package-1.0.0.tar.gz
└── my_package-1.0.0-py3-none-any.whl
```

### What is what's being built?

- `.tar.gz` = source distribution
- `.whl` = built wheel for installation

### Why build before publish?

It validates the project metadata and the actual artifact layout before you release anything.

### Verification exercise

```bash
uv build
ls -l dist/
python -m zipfile -l dist/*.whl
```

You want to see the expected package files in the wheel.

### Troubleshooting checklist

If the build fails, inspect:

- `pyproject.toml`
- package name and metadata
- `src/` directory layout
- build backend installation
- missing `hatchling` or similar backend dependency

---

## 🏷️ Module 7 — versioning like a pro

### Why dynamic versioning matters

Hardcoded versions drift. Git tags are the more trustworthy source of truth.

```text
Git tag: v1.4.0
   ↓
Package version: 1.4.0
```

### Configure dynamic versioning

```bash
uv add --group dev hatch-vcs
```

Then add this to `pyproject.toml`:

```toml
[build-system]
requires = [
    "hatchling",
    "hatch-vcs",
]
build-backend = "hatchling.build"

[project]
name = "my-package"
dynamic = ["version"]

[tool.hatch.version]
source = "vcs"
```

### Tag the release

```bash
git tag v1.0.0
git push origin v1.0.0
```

Then build again:

```bash
uv build
```

### Debug path

If it fails:

```bash
git status
git tag
git describe --tags
git describe --tags --always
```

Common causes:

- repo not initialized
- shallow clone without tags
- missing `hatch-vcs`
- incorrect metadata
- build isolation issue

CI fix:

```bash
git fetch --tags
```

---

## 📚 Module 8 — docs and dev tooling as first-class workflow

### Add docs dependencies

```bash
uv add --group docs mkdocs
```

Serve docs:

```bash
uv run --group docs mkdocs serve
```

Build them:

```bash
uv run --group docs mkdocs build
```

For Sphinx:

```bash
uv add --group docs sphinx
uv run --group docs sphinx-build docs docs/_build
```

### Best practice

Keep project tools separated:

- runtime dependencies for the package
- dev dependencies for testing/linting
- docs dependencies for documentation builds

This keeps production installs lean and avoids unnecessary coupling.

---

## 🚀 Module 9 — publish to TestPyPI and PyPI

### Publish to TestPyPI

```bash
uv publish --publish-url https://test.pypi.org/legacy/
```

Validate installation:

```bash
uv pip install \
  --index-url https://test.pypi.org/simple/ \
  my-package
```

### Publish to PyPI

```bash
uv publish
```

### Real release flow

```text
Code
 ↓
Git tag
 ↓
uv build
 ↓
Test artifact
 ↓
TestPyPI
 ↓
Validate
 ↓
PyPI
```

### Trusted publishing / OIDC

Modern release systems use OIDC instead of long-lived tokens:

```text
GitHub Actions
      │
      │ OIDC
      ▼
   PyPI
      │
      ▼
Package release
```

This is safer because it avoids storing long-lived credentials in GitHub secrets.

---

## 🏢 Module 10 — workspaces and monorepos

`uv` supports multi-package repositories well.

Example structure:

```text
company/
├── pyproject.toml
├── uv.lock
└── packages/
    ├── core/
    │   └── pyproject.toml
    ├── api/
    │   └── pyproject.toml
    └── cli/
        └── pyproject.toml
```

Root config:

```toml
[tool.uv.workspace]
members = [
    "packages/core",
    "packages/api",
    "packages/cli",
]
```

Workspace source example:

```toml
[tool.uv.sources]
my-core = { workspace = true }
```

### Why this matters

Large teams often need multiple packages with shared tooling and a common release flow. Workspaces make that manageable.

---

## 🔍 Module 11 — real troubleshooting playbook

### 1. `ModuleNotFoundError`

```text
ModuleNotFoundError: No module named 'my_project'
```

Typical fixes:

```bash
uv sync
uv run python -c "import my_project"
```

### 2. Dependency conflict

Symptoms:

- resolver errors
- incompatible versions
- cryptic metadata errors

Fix:

```bash
uv tree
uv tree --invert
uv lock
```

### 3. Version detection issues

```bash
git describe --tags --always
git fetch --tags
```

### 4. Windows file lock issues

If you see:

```text
PermissionError
File is being used by another process
```

try:

- close Python processes
- stop IDE terminals
- close test runners
- retry

### 5. Shell differences

PowerShell:

```powershell
Remove-Item -Recurse -Force .venv
```

Bash:

```bash
rm -rf .venv
```

---

## 🧪 Module 12 — capstone challenge

### Scenario

You inherit a legacy project with:

- `setup.py`
- `requirements.txt`
- flat package layout
- no lock file
- manual versioning
- no separate dev/docs groups
- inconsistent build behavior

### Mission

Refactor it into a modern `uv` workflow:

1. initialize a package with `uv`
2. pin Python using `.python-version`
3. move runtime dependencies into `pyproject.toml`
4. add dev and docs groups
5. generate and sync `uv.lock`
6. move code into `src/`
7. build a proper package artifact
8. tag the project using Git
9. validate installation from the built wheel
10. publish to TestPyPI and then PyPI

### Target state

```text
legacy-app/
├── pyproject.toml
├── uv.lock
├── .python-version
├── README.md
├── src/
│   └── legacy_app/
│       ├── __init__.py
│       └── main.py
├── tests/
├── docs/
└── .git/
```

---

## 🔥 Day-to-day command card

```bash
# project lifecycle
uv init --package
uv add PACKAGE
uv remove PACKAGE
uv lock
uv sync
uv run python

# Python management
uv python list
uv python install 3.11
uv python pin 3.11

# dependency diagnostics
uv tree
uv tree --invert
uv lock --check

# quality and testing
uv run pytest
uv run ruff check .
uv run ruff format .

# build and publish
uv build
uv publish --publish-url https://test.pypi.org/legacy/
uv publish
```

---

## 🧠 Final workshop reflection

The core shift is this:

- `uv` is not just a faster `pip`
- it is a modern Python development workflow
- `pyproject.toml` declares intent
- `uv.lock` captures resolution
- the build backend creates the actual artifact
- the release process should be reproducible, verifiable, and secure

That is the difference between “I can install a package” and “I can run a reliable packaging pipeline.”

---

## ⚠️ Gotchas

> [!WARNING]
> You will still type `pip install` out of habit. That is normal. Use `uv` intentionally until the workflow becomes automatic.

> [!NOTE]
> `uv` works for the overwhelming majority of Python projects, but specialized build systems may still need careful troubleshooting. That is part of the real world of packaging.

---

## 🏁 Graduation checklist

You are ready for Zero → Hero when you can do all of the following without looking up syntax:

- explain the modern packaging stack
- initialize a project with `uv`
- manage Python versions with `uv python`
- use dependency groups cleanly
- create and sync environments
- understand `uv.lock`
- build wheels and sdists
- work with `src/` layout properly
- diagnose import issues and dependency conflicts
- work with Git tags and dynamic versioning
- publish to TestPyPI and PyPI
- operate in a monorepo or workspace

If you want the next step, we can move from this conceptual workshop into a full hands-on lab where we build a minimal package, add tests, docs, and release automation as a real working example.



