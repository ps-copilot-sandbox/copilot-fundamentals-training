# Globex ➜ Chroma Rename Demo

This directory contains **five directories** that simulate a medium-scale codebase owned by **Globex Ltd**.  
Your mission—using GitHub Copilot features—is to rename every `globex_` identifier to `chroma_` after an acquisition.

```
globex_rename_demo/
├── app/                # Core business logic
├── cli/                # Command‑line utilities
├── configs/            # YAML configs
├── tests/              # Pytest suite
└── docs/               # Project documentation
```

## Demo flow (maps to Copilot feature phases)

| Phase | Copilot features | What to show |
|-------|------------------|--------------|
| **1 Planning** | Chat, Spaces, Custom Instructions | Scope impact, draft rename plan, store rules in a Space |
| **2 Code creation** | Ask, Edit, Workspaces, Model Picker | Generate `rename.py`, refactor with Edit, iterate in Workspace |
| **3 Reviews** | Coding Agent, Code Review, PR Summaries | Agent opens PR; Copilot reviews & summarizes |
| **4 Testing** | Chat commands, Code completions | Run tests, ask for edge‑case analysis |
| **5 Deployment** | Chat on GitHub.com | Merge PR, create follow‑up Issue |

## Quick start

```bash
# 1. Clone and open in VS Code
git clone <repo-url>
code globex_rename_demo

# 2. Activate Copilot Chat & run:
#    "List files containing 'globex_'"
# 3. Follow the speaker‑note steps to complete the rename.
```

Enjoy exploring how Copilot turns a tedious bulk refactor into a 15‑minute task!
