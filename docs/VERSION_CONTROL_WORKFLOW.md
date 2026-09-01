# Version Control Workflow — MLOps Iris Classifier

## 1. Overview

This document describes the Git-based version control workflow used for this Machine Learning project as part of MLOps Lab Experiment 2.

- **Repository:** https://github.com/harshalpatil67518-code/DS_A_T3_52
- **Primary language:** Python
- **Maintainer:** Harshal Patil

## 2. Branching Strategy

| Branch | Purpose |
|---|---|
| `main` | Stable, deployable code |
| `develop` | Integration branch for development |
| `feature/*` | Individual feature development |
| `conflict-demo-*` | Demonstration branches for conflict resolution |

No direct commits should be made to `main`.

Normal workflow:

`feature/* → Pull Request → develop → main`

## 3. Commit Convention

Commits follow the format:

`type: short description`

Types used:

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `chore:` Configuration or maintenance
- `refactor:` Code restructuring
- `test:` Adding or fixing tests

Example:

`feat: add classification report to training script`

## 4. Standard Workflow

```bash
git switch develop
git pull origin develop
git switch -c feature/short-description

# Make changes

git add <files>
git commit -m "feat: description"
git push -u origin feature/short-description

# Create Pull Request into develop
# Review and merge the Pull Request