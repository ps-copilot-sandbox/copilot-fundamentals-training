
# 🔑 Duplicate Keybindings Checker Demo  
*A GitHub Copilot Fundamentals Lab (on **microsoft/terminal**)*

---

## 🚀 What You’ll Build
Use **GitHub Copilot** to add a tiny helper that finds **duplicate keybindings** in a Windows Terminal `settings.json` file.  
You’ll practice two core techniques:

- **Task Decomposition** — do **one small step** at a time and verify.  
- **GAR loop** — **Generate → Analyze (tests) → Repair** using a targeted prompt.

> We edit a small folder only; you don’t need to build Windows Terminal.

---

## 🗂️ Repository Layout (after you finish)
| Path | Purpose |
|------|---------|
| `tools/keybinding-dupes/dupes.py` | CLI + `find_duplicates(settings_path)` implementation. |
| `tools/keybinding-dupes/test_dupes.py` | Minimal **pytest** suite (starts **red** by design). |
| `tools/keybinding-dupes/samples/settings_with_dupes.json` | Sample settings with an intentional duplicate. |
| `tools/keybinding-dupes/samples/settings_clean.json` | *(Optional)* Clean sample (no duplicates). |

---

## 🛠️ Prerequisites
| Tool | Version | Notes |
|------|---------|-------|
| Python | 3.10+ | For the tiny CLI and tests |
| Pytest | latest | `pip install pytest` |
| VS Code + Copilot | latest | Copilot Chat signed in and working |

---

## 🧭 Workflow Map
**Step 1 — Create the tool (Copilot Chat)** →  
**Step 2 — Add failing test + sample (Copilot Chat)** →  
**Step 3 — Run tests (Terminal) ⇒ red** →  
**Step 4 — GAR repair (Copilot Chat)** →  
**Step 5 — Re‑run tests (Terminal) ⇒ green** →  
**Step 6 — *(Optional)* Add clean sample + test (Copilot Chat) ⇒ green**

Each step below says **where to type**, gives a **copy‑paste prompt/command**, and includes an **explanation of the prompt** + the **prompt‑engineering techniques** it uses.

---

## Pre-work - Clone & Open (💻 Terminal)
```bash
git clone https://github.com/microsoft/terminal.git
cd terminal
code .
```

---

## Pre-work 2 - Create the Working Folder (💻 Terminal)
```bash
mkdir -p tools/keybinding-dupes/samples
```

---

## Step 1 — Create the Tool Skeleton (🗨️ Copilot Chat)

**Prompt (paste into Copilot Chat):**
```
Step 1 only: Implement tools/keybinding-dupes/dupes.py.
Requirements:
- Provide find_duplicates(settings_path: str) -> list[dict] that returns a list of duplicates,
  where a duplicate means two entries share both "keys" and "command".
- Search in either "actions" or "keybindings" (support both names).
- Add a small CLI: python dupes.py --path path/to/settings.json that prints duplicates clearly.
Output code only.
```

**What this means / why we enter it**
- We are asking Copilot to **create just the core tool** that we’ll build on.  
- The CLI gives us an **end‑to‑end path** to try the tool quickly.  
- Calling out `"actions"` or `"keybindings"` keeps it robust across schema variants.

**Prompt‑engineering techniques used**
- **Task Decomposition:** “**Step 1 only**” limits scope to a single, bite‑sized step.  
- **Specific constraints:** function name + return type + duplicate definition → fewer hallucinations.  
- **Format constraint:** “**Output code only**” keeps responses clean and pasteable.

**Outcome:** a `dupes.py` file with a minimal `find_duplicates()` and CLI.

---

## Step 2 — Add a Failing Test + Sample (🗨️ Copilot Chat)

**Prompt (paste into Copilot Chat):**
```
Step 2 only: Create tools/keybinding-dupes/test_dupes.py with a single failing test:
- test_detects_duplicate_keybindings: use samples/settings_with_dupes.json containing two
  entries with the same "keys" and "command"; expect find_duplicates() to return at least one duplicate.
Also create samples/settings_with_dupes.json with a minimal structure containing those duplicates.
Output code only.
```

**What this means / why we enter it**
- We’re asking Copilot to generate **one simple failing test** and the **sample data** it needs.  
- The failure gives us an **objective target** for the next step (GAR).  
- The sample file makes the lab **repeatable** and avoids environment differences.

**Prompt‑engineering techniques used**
- **Task Decomposition:** “**Step 2 only**” progresses one step without scope drift.  
- **Ground truth creation:** intentional **failing test** sets clear pass/fail criteria for the model.  
- **Format constraint:** “**Output code only**” avoids extra prose.

**Outcome:** a test file + a sample settings file. The test should **fail** at first.

---

## Step 3 - Run Tests and check our Script (💻 Terminal)
```bash
pytest -q
python3 dupes.py --path samples/setings_with_dupes.json
```
**Expect:** **red**. That failure is your **ground truth** for the next step.
- It’s red by design. Now we do a GAR loop - fix exactly what failed.

---

## Step 4 — GAR Repair (🗨️ Copilot Chat)

**Prompt (paste into Copilot Chat with the real failure text):**
```
Fix this failing test:

<PASTE the exact pytest failure text>

Keep find_duplicates() signature and CLI intact.
Output a unified diff only.
```

**What this means / why we enter it**
- We give Copilot the **exact error message** so it focuses on the real problem.  
- We lock the **public API** (function & CLI) to prevent breaking changes.  
- We ask for a **unified diff** so the output is reviewable and minimal.

**Prompt‑engineering techniques used**
- **GAR loop:** test output → **Analyze** → target the **Repair**.  
- **High‑specificity instruction:** pasting the **failure text** removes ambiguity.  
- **Format constraint:** “**unified diff only**” enforces concise patches.

**Goal:** Copilot returns a small diff that addresses the specific failure.

---

## Step 5 - Re‑run Tests (💻 Terminal)
```bash
pytest -q
python3 dupes.py --path samples/setings_with_dupes.json
```
- Still **red**? Paste the new failure into Copilot Chat and repeat **Step 3**.  
- **Green?** You’re done with the core loop.

---

## Step 6 - (Optional) — Add a Clean Sample + Passing Test (🗨️ Copilot Chat)

**Prompt (paste into Copilot Chat):**
```
Add samples/settings_clean.json with no duplicates and a test
test_returns_empty_when_no_duplicates. Output code only.
```
or 
- Change the keys in the sample file to whatever you would like and re-run the tests. 

**What this means / why we enter it**
- We add a **positive case** to prove the tool reports **no issues** when the file is clean.  
- This guards against false positives and documents intended behavior.

**Prompt‑engineering techniques used**
- **Coverage expansion:** positive + negative tests reduce drift in future edits.  
- **Format constraint:** “**Output code only**.”

Re‑run:
```bash
pytest -q
```

---

## ▶️ Try the CLI (💻 Terminal)
Point the tool at the sample with dupes:
```bash
python tools/keybinding-dupes/dupes.py --path tools/keybinding-dupes/samples/settings_with_dupes.json
```
You should see a clear summary identifying at least one duplicate `(keys, command)` pair.

---

## 🧰 Guardrails You Can Reuse
- **Keep scope tight:** “**Step X only**. **Output code only.**”  
- **Constrain output:** “**Output a unified diff only.**”  
- **Target the fix:** paste the **exact failing test output** (no summaries).

---

## 💬 Common Questions
| Q | A |
|---|---|
| Do I need to build Windows Terminal? | No—this demo only adds files under `tools/keybinding-dupes/`. |
| Can I use my own settings.json? | Yes. After tests are green, point the CLI to your file. |
| Why start with a failing test? | It reduces hallucinations and gives Copilot a concrete target for the **GAR** fix. |
| Copilot output is too long—help? | Add **“Output a unified diff only.”** |

---

## 🎯 Learning Objectives
| ✅ Skill | Demonstrated by |
|---------|------------------|
| Prompt‑driven coding | Turning short prompts into working code |
| Task Decomposition | One step at a time with explicit verification |
| GAR loop | Using failing tests as ground truth for targeted fixes |
| Output control | Diff‑only responses for clean reviews |

---

### 🎉 You’re Done!
You shipped a practical helper in minutes and saw how **Task Decomposition** + **GAR** keep Copilot focused and fast.

