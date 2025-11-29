# ⚡️ Usecase: Supercharging Your Workflow with `uv`

> "Waiting for `pip install` is the modern equivalent of watching paint dry, but with more dependency conflicts."

If you've ever felt your soul leave your body while waiting for a CI pipeline to install `pandas`, or if you have 14 different versions of Python installed and don't know which one is "real" anymore... **`uv` is here to save you.**

---

## 🧐 What is `uv`?

Think of `uv` as the **Formula 1 pit crew** for your Python projects.

It's an extremely fast, all-in-one package and project manager written in **Rust**. It replaces `pip`, `pip-tools`, `virtualenv`, `poetry`, and even `pyenv` in one single binary.

### 🏎️ Why should you care? (The Hook)
*   **It is absurdly fast.** We're talking 10-100x faster than `pip`. It resolves dependencies before you can blink.
*   **It saves disk space.** It uses a global cache, so you don't have 50 copies of `numpy` eating your SSD.
*   **It's a drop-in replacement.** You don't need to learn a whole new language. It speaks `pip`.

---

## 🚀 Quick Start (TL;DR)

Stop reading and start zooming.

### 1. Install `uv`

```bash
# macOS / Linux / WSL
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
irm https://astral.sh/uv/install.ps1 | iex
```

### 2. The "I just want a fast pip" Workflow

You can use `uv` exactly like `pip`, but without the nap time.

```bash
# Create a virtual environment (instant)
uv venv

# Activate it (standard procedure)
# Windows: .venv\Scripts\activate
# Linux/Mac: source .venv/bin/activate

# Install stuff (ZOOM!)
uv pip install fastapi pandas numpy
```

> [!TIP]
> **Pro Tip:** You don't even need to activate the venv if you don't want to. `uv pip install` automatically detects a `.venv` in the current directory.

---

## 🛠️ The "Project Manager" Workflow (Poetry Style)

If you're building a proper application and want a `pyproject.toml` without the headache, `uv` has your back.

### 1. Initialize a Project
```bash
uv init my-awesome-project
cd my-awesome-project
```

### 2. Add Dependencies
This adds it to `pyproject.toml` AND installs it.
```bash
uv add requests
uv add pytest --dev
```

### 3. Run Commands
No need to activate anything. Just run it.
```bash
uv run pytest
uv run python main.py
```

---

## 🆚 Old Way vs. New Way

| Task | The Old Way 🐢 | The `uv` Way 🐇 |
| :--- | :--- | :--- |
| **Create Venv** | `python -m venv .venv` | `uv venv` |
| **Install Pkg** | `pip install pandas` | `uv pip install pandas` |
| **Lock Deps** | `pip-compile requirements.in` | `uv pip compile requirements.in -o requirements.txt` |
| **Sync Deps** | `pip-sync requirements.txt` | `uv pip sync requirements.txt` |
| **Run Script** | `source .venv/bin/activate && python app.py` | `uv run app.py` |

---

## 💡 Pro Tips for the Power User

### 1. Python Version Management
Forget `pyenv`. `uv` can manage Python versions for you.
```bash
# Install Python 3.12
uv python install 3.12

# Create a venv with specific python version
uv venv --python 3.12
```

### 2. The "Script" Runner
Got a single-file script that needs dependencies? You don't need a whole project.
Add this magic comment to the top of `script.py`:
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
Now just run it:
```bash
uv run script.py
```
`uv` will create a temporary environment, install `requests` and `rich`, run the script, and clean up. **Magic.**

---

## ⚠️ Gotchas

> [!WARNING]
> **Muscle Memory:** You will keep typing `pip install` for a few weeks. It's okay. We all do it.

> [!NOTE]
> **Compatibility:** `uv` is very compatible, but some edge-case packages with weird build scripts might still need standard `pip`. But for 99% of cases, `uv` is the way.
