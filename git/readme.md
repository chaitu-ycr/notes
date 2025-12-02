# 🐙 Git: The Time Machine for Your Code

> [!NOTE]
> **The Hook:** Imagine you're tuning an engine. You tweak the fuel injection, and suddenly the car won't start. Without Git, you're guessing what you changed. With Git, you just snap your fingers (or type `git restore`), and you're back to a purring engine. It's not just a tool; it's your career insurance policy.

## 🛠️ Phase 0: The Setup (Do This Once)

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

---

## 🏎️ Phase 1: The Daily Drive (90% of your job)

This is the "Happy Path". Memorize these.

### 1. Getting the Code (`git clone`)
Download the repository to your machine.

```bash
# Clone via SSH (Recommended)
git clone git@github.com:automotive-corp/bms-firmware.git

# Go into the folder
cd bms-firmware
```

### 2. The "What's Happening?" Command (`git status`)
Run this constantly. It tells you what files are changed, staged, or untracked.

```bash
git status
```

### 3. Staging Changes (`git add`)
Tell Git which files you want to include in the next snapshot.

```bash
# Add a specific file
git add src/can_driver.c

# Add EVERYTHING (Use with caution)
git add .
```

### 4. Saving the Snapshot (`git commit`)
Save your staged changes to your local history.

```bash
# The -m flag lets you write the message inline
git commit -m "feat(can): Implement ISO-TP protocol handling"
```

### 5. Syncing with the World (`git pull` / `git push`)
Get updates from others and send your updates to them.

```bash
# Get latest changes from the server (and merge them into your branch)
git pull origin main

# Send your commits to the server
git push origin feature/iso-tp-implementation
```

---

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

---

## 🧰 Phase 3: Surgical Tools (Power User)

For when you need to be precise.

### 1. The "Clean Up" (`git clean`)
Remove untracked files (like build artifacts or temporary logs).

```bash
# Show me what WOULD be deleted (Dry run)
git clean -n -d

# Actually delete untracked files and directories
git clean -f -d
```

### 2. The "Save for Later" (`git stash`)
You're in the middle of a messy feature, but you need to switch branches to fix a critical bug.

```bash
# Stash your changes (reverts files to last commit, saves changes in a stack)
git stash

# ... do your other work ...

# Bring the changes back
git stash pop
```

### 3. The "Cherry Pick" (`git cherry-pick`)
You want *just that one commit* from another branch, not the whole branch.

```bash
# Apply a specific commit to your current branch
git cherry-pick <commit-hash>
```

### 4. The "Diff" (`git diff`)
See exactly what lines changed.

```bash
# Compare working directory to staging area
git diff

# Compare staged changes to last commit
git diff --staged
```

---

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

---

## 🚑 Phase 5: Emergency Room (Undo Buttons)

### 1. "I committed to the wrong branch!" (`git reset --soft`)
Undoes the commit but keeps your work.

```bash
git reset --soft HEAD~1
```

### 2. "I want to scrap everything I just did" (`git reset --hard`)
**DANGER:** Deletes all uncommitted work.

```bash
git reset --hard HEAD
```

### 3. "I pushed a bad commit!" (`git revert`)
Create a *new* commit that is the exact opposite of the bad one. Safe for public branches.

```bash
git revert <bad-commit-hash>
```

### 4. "I lost a commit!" (`git reflog`)
Git keeps a log of *every* movement of the HEAD pointer, even if you deleted the branch.

```bash
# Find the hash of the lost state
git reflog

# Jump back to it
git reset --hard <hash-from-reflog>
```

---

> **Antigravity's Wisdom:** 
> *   **`git push --force`** is like using a flamethrower to kill a spider. Sure, it works, but you might burn the house down. Use **`git push --force-with-lease`** instead.
> *   Commit often. It's easier to squash 10 small commits than to split 1 giant one.
