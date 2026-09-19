---
title: "Git"
aliases:
  - "Git"
---
# 🐙 Git: The Time Machine for Your Code

> [!NOTE]
> **The Hook:** Imagine you're tuning an engine. You tweak the fuel injection, and suddenly the car won't start. Without Git, you're guessing what you changed. With Git, you just snap your fingers (or type `git restore`), and you're back to a purring engine. It's not just a tool; it's your career insurance policy.

## � Related topics

- [Integration](../integration/integration.md) — the broader delivery and automation workflow around Git
- [GitHub Actions](../github_actions/github_actions.md) — pull-request and deployment automation on top of git-based workflows
- [Jenkins](../jenkins/jenkins.md) — alternative pipeline automation for version-controlled projects
- [Testing](../testing/testing.md) — validation gates and regression checks in the delivery lifecycle
- [SDLC](../sdlc/sdlc.md) — how version control integrates with the full software lifecycle

## �🛠️ Phase 0: The Setup (Do This Once)

Before you touch any code, you need to tell Git who you are and how to talk to the server.

### 1. Identity Crisis (`git config`)
Tell Git your name so your teammates know who broke the build.

```bash
# Set your name (Global = for all projects on this machine)
git config --global user.name "Antigravity Engineer"

# Set your email (Must match your GitHub/GitLab email)
git config --global user.email "engineer@automotive-corp.com"

# Verify it stuck
git config --list
```

### 2. The Secret Handshake (`ssh-keygen`)
Stop typing your password every time you push. Use SSH keys.

```bash
# 1. Generate a new SSH key (Press Enter for defaults)
ssh-keygen -t ed25519 -C "engineer@automotive-corp.com"

# 2. Start the ssh-agent in the background
eval "$(ssh-agent -s)"

# 3. Add your SSH private key to the ssh-agent
ssh-add ~/.ssh/id_ed25519

# 4. Copy the public key to your clipboard (to paste into GitHub/GitLab settings)
cat ~/.ssh/id_ed25519.pub
# (Copy the output starting with "ssh-ed25519...")
```

## 🌿 Phase 2: Branching (The Multiverse)

Don't mess with `main`. Create your own universe.

### 1. Managing Branches
```bash
# List all local branches
git branch

# Create a new branch AND switch to it
git switch -c feature/regenerative-braking

# Switch to an existing branch
git switch main

# Delete a branch (after you merged it)
git branch -d feature/regenerative-braking
```

### 2. Merging (Combining Universes)
Bring your feature back into the main code.

```bash
# 1. Go to the target branch (usually main or develop)
git switch main

# 2. Pull latest changes first!
git pull origin main

# 3. Merge your feature in
git merge feature/regenerative-braking
```

## 🕵️ Phase 4: Forensics & Debugging

Who broke the build? When did this bug appear?

### 1. The History (`git log`)
View the timeline.

```bash
# The pretty version
git log --oneline --graph --all
```

### 2. The "Who Dunnit" (`git blame`)
See who wrote each line of a file.

```bash
git blame src/battery_monitor.c
```

### 3. The "Bug Hunter" (`git bisect`)
Automated binary search to find the exact commit that introduced a bug.

```bash
# Start the hunt
git bisect start

# Tell Git the current version is bad
git bisect bad

# Tell Git a version from last week was good
git bisect good <commit-hash-from-last-week>

# Git will now jump around. Test each version and say:
# git bisect good  (if it works)
# git bisect bad   (if it fails)

# When found, reset
git bisect reset
```

> **Antigravity's Wisdom:** 
> *   **`git push --force`** is like using a flamethrower to kill a spider. Sure, it works, but you might burn the house down. Use **`git push --force-with-lease`** instead.
> *   Commit often. It's easier to squash 10 small commits than to split 1 giant one.


