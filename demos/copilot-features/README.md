# 🔄 Globex ➜ Chroma Bulk‑Rename Demo  
*A GitHub Copilot Fundamentals Lab*

---

## 🎯 What You’ll Accomplish
By the end of this lab you will:

1. **Plan** a repo‑wide rename from `globex_` → `chroma_` after a fictional acquisition.  
2. **Generate** a fully‑working Python CLI that traverses the codebase and rewrites identifiers, file names, and config keys—all with Copilot *Ask* & *Edit*.  
3. **Automate** the change: unit tests, commit, PR creation, and review with Copilot Agent, PR Summaries, and Code Review.  
4. **Ship** the refactor in < 10 minutes—turning a common task into a repeatable workflow.

<details>
<summary><strong>Why this matters</strong></summary>

*Brand mergers, framework upgrades, and domain‑driven restructures force mass renames more often than we would like.  
Doing it by hand is error‑prone and kills velocity. Copilot collapses days of grunt work into minutes and leaves an auditable trail.*
</details>

---

## 🗂️ Repository Layout

```
globex_rename_demo/
├── app/        ← core business logic (150 LoC ea.)
├── cli/        ← Python CLIs including the rename tool
├── configs/    ← YAML configs with `globex_` keys
├── tests/      ← Pytest suite for safety nets
└── docs/       ← Project docs (Markdown)
```

Each file contains **~150 lines** peppered with `globex_` identifiers to give Copilot plenty of context.

---

## 🛠️ Prerequisites

| Tool | Version | Why |
|------|---------|-----|
| **Python** | 3.8 + | Runs the generated CLI & tests |
| **VS Code** (or JetBrains, Neovim) | Latest | IDE with GitHub Copilot & Chat |
| **GitHub Copilot** | Business / Enterprise seat | Ask, Edit, Agent, Workspaces |
| **Git** | Any | So we can open the agent‑driven PR |

> ℹ️ **Tip:** Confirm Copilot Chat works by typing `Hello Copilot` in the sidebar before you begin.

---

## 🚦 Five‑Phase Walk‑Through

| Phase | Copilot Features | Action Steps |
|-------|------------------|--------------|
| **1 Planning** | Chat, Spaces, Custom Instructions | *Scope impact* → `List files containing "globex_"`<br>*Draft 5‑step plan* → save to **Copilot Space**<br>*Add repo instruction* → forbid magic numbers |
| **2 Code Creation** | Ask, Edit, Workspaces, Model Picker | Open Issue → **Workspace** proposes tasks<br>Use **Ask** to create `rename.py`<br>Switch to *Claude 3 Sonnet* for fast tests<br>Refine with **Edit** (`skip node_modules`) |
| **3 Reviews** | Coding Agent, PR Summaries, Code Review | `@agent run rename.py & open PR`<br>Read **AI summary** & automated **review comments** |
| **4 Testing** | Chat commands, Code completions | `@copilot run pytest -q`<br>Ask Chat: *Edge cases we missed?* |
| **5 Deployment** | Chat in GitHub.com | Merge PR → `@copilot create follow‑up Issue` |

---

## 🧑‍💻 Quick‑Start Commands

```bash
# Clone & open
git clone https://github.com/ps-copilot-sandbox/copilot-fundamentals-training
cd demos/copilot-features/
code .

# Optional: run the (pre‑rename) tests
python -m pytest -q
```

Now follow the phase table above or use the detailed speaker‑note script in `docs/Globex_Rename_Speaker_Notes.md`.

## ⏱️ Phase 0 · Environment Prep (1 min)

```bash
git clone https://github.com/ps-copilot-sandbox/copilot-fundamentals-training
cd demos/copilot-features
code .
python -m pytest -q      # sanity check – should pass
```

1. **Enable Copilot Chat** → _VS Code › View › Copilot Chat_.  
2. Type `print("globex")` – ensure 💡 suggestions appear.

---

## 🔍 Phase 1 · Plan (≤ 5 min)

| Action | Exact prompt / click |
|--------|----------------------|
| **Scope** | `List all files containing "globex_"` |
| **Draft plan** | `Draft a 5‑step plan to rename "globex_" → "chroma_" with backup, tests, CI gate, rollback.` |
| **Save internally or save to Space** | ⋮ → **Save as Doc** → _Chroma‑Rename_ |
| **Repo rule** | Create `.github/copilot-instructions.md`:<br>`- Disallow magic numbers; use named constants.` → `git add & commit` |

---

## 🛠️ Phase 2 · Code (≤ 7 min)

1. **Workspace** – on GitHub, new Issue **“Rename globex_ to chroma_”** → **Open in Copilot Workspace**.  
  - You can also use Copilot Chat, Copilot agent mode or any other method you like to accomplish phase 2's coding portion. You can use the prompt below the same. 
2. **Ask (generate CLI)**  
   - Create a new file in the cli directory named rename.py
   - Enter the following prompt at the top as a comment:  
   ```
   # Generate a Python script that recursively renames any file or symbol
   starting with "globex_" to "chroma_", skip .git & node_modules, print summary.
   ```
   - Accept the suggestion that makes sense to you.  
3. **Model Picker** – select **Claude 3 Sonnet** → ensure that you are in Edit mode → enter the following prompt:  
   ```
   Add pytest tests covering rename, binary‑skip, and --check dry‑run.
   ```
4. **Edit (refine)** – Select `rename.py` → **Edit** prompt:  
   ```
   Replace print with logger, add --check flag (dry‑run).
   ```
---

## 🤖 Phase 3 · Review & PR (≤ 4 min)

| Step | Prompt |
|------|--------|
| Dry‑run | `@agent run python cli/rename.py --path . --check` |
| Open PR | `@agent commit all, open PR "chore: globex → chroma bulk rename"` |
| PR summary & review | In PR comment box → `@copilot review` → **Apply patch** if happy |

- For the dry run, it should report 0 files modified because its a dry run.
- If it fails, copilot chat can help fix it! 
---

## ✅ Phase 4 · Test (2 min)

```text
@copilot run pytest -q
```

Then ask:  
```
List any edge cases still unhandled.
```

---

## 🚀 OPTIONAL - Phase 5 · Ship (1 min)

1. **Merge PR** → _Squash & merge_.  
2. Post‑merge comment:  
   ```
   @copilot create issue "Communicate 'chroma_' rename" with migration date,
   rollback steps, and link to PR.
   ```

---  

### 🎉 Done

You’ve renamed a multi‑folder codebase safely with Copilot’s full toolbelt—no manual grep, no missed edge cases.

---

## 🚀 Stretch Goals

1. **Dry‑run flag** — add `--check` to print files that *would* change.  
2. **Rollback plan** — ask Copilot to write a `revert.py` that restores `globex_`.  
3. **Binary‑safe update** — extend the script to rewrite identifiers in JSON/YAML too.  
4. **CI workflow** — generate a GitHub Actions job to run tests on every rename PR.

---

## 🙋 FAQ

| Q | A |
|---|---|
| “Why Python?” | Easy to read, modify, and unit‑test live in the session. |
| “Do I need to rename docs manually?” | The CLI also updates `.md`, `.yaml`, `.py`—feel free to widen patterns. |
| “What if Copilot proposes dangerous changes?” | Use PR diff + Copilot Review to catch unintended logic edits before merge. |

---

## 💜 Credits & License

Sample code is MIT‑licensed.  
Demo authored by the GitHub Copilot Enablement Team—use, fork, and remix for internal enablement sessions.

