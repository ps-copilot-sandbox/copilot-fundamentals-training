# 🧑‍🏫 MyCorp‑Auth MCP Lab · **Fill‑in‑the‑Blanks Edition**

This workshop turns learners into MCP pros by having **Copilot generate the missing pieces** of a tiny Flask server.  
When finished, Copilot Chat will answer questions like “*Explain the token flow in 3 steps*” using **local Markdown docs** that Bing can’t see.

---

## 📦 Folder Structure

```
copilot-techniques/
├── mycorp-auth-docs/           # your “private” KB
│   ├── overview.md
│   ├── token_flow.md
│   └── troubleshooting.md
├── mcp_auth_docs.py            # ← starter file with   💡  prompts
└── README.md
```

---

## 🛠 Prerequisites

| Tool | Version | Why |
|------|---------|-----|
| Python | 3.8 + | Runs the Flask server |
| pip | latest | `pip install flask` |
| VS Code | latest | IDE with Copilot Chat + MCP support |
| GitHub Copilot Chat | enabled | verify 💡 suggestions appear |

---

## 🚀 Walkthrough

### 0 · Clone & Install (1 min)

```bash
git clone <repo-url> mycorp_auth_kb_demo
cd mycorp_auth_kb_demo
pip install flask
code .
```

### 1 · Explore the Starter Server (2 min)

Open **`mcp_auth_docs.py`**.  
You’ll see six labelled blocks with `pass` and a **💡 Copilot prompt** above each.

> **Goal:** accept Copilot’s suggestion for every `pass`, turning the skeleton into a working service.

### 2 · Generate Code with Copilot (5 min)

For each block:

| Block | What to do |
|-------|------------|
| **Imports** | Place cursor on the prompt comment → <kbd>Tab</kbd> → Copilot inserts `import flask, pathlib, re`. |
| **Flask app** | Accept suggestion for `app = flask.Flask(__name__)`. |
| **DOCS list** | Accept code that builds `DOCS = list(Path("mycorp-auth-docs").rglob("*.md"))`. |
| **`search()` helper** | Read the generated function aloud; highlight regex & list‑comp. |
| **POST `/authdoc` route** | Accept; note how Copilot uses `flask.request.json`. |
| **`__main__` guard** | Accept; runs `app.run(port=8000)`. |

*(Pause for questions: “Why limit to first `k` hits?” “Could we sort by length?”)*

### 3 · Run the Server (30 sec)

```bash
python mcp_auth_docs.py
# Running on http://127.0.0.1:8000
```

Leave terminal open.

### 4 · Register the Tool with Copilot (30 sec)

Ask GitHub Copilot Chat to help create a new MCP.json file:


```
Create a new file .vscode/mcp.json that registers an MCP tool named authDocs.
The JSON should use \"version\": 1, set \"type\": \"http\", point \"url\" to http://localhost:8000/authdoc, and add the description \"Search MyCorp‑Auth KB\".
Format the JSON with two‑space indentation.
```
If you would like to grab a completed one, find a working version here:
```json
{
  "version": 1,
  "tools": {
    "authDocs": {
      "type": "http",
      "url": "http://localhost:8000/authdoc",
      "description": "Search MyCorp‑Auth KB"
    }
  }
}
```

Reload VS Code (`Cmd/Ctrl+Shift+P → Reload Window`).  
Look for the **🔌 authDocs** indicator in the chat sidebar.

### 5 · Ask Live Queries (5 min)

| Prompt | Expected result |
|--------|-----------------|
| `list available tools` | Copilot confirms it can use `authDocs`. |
| `Use authDocs to explain the token flow in 3 steps.` | Bullet list pulled from *token_flow.md*. |
| `Use authDocs to show JWT claims as a markdown table.` | Nicely formatted table. |
| `Use authDocs to troubleshoot "signature is invalid".` | Solution excerpt from *troubleshooting.md*. |

### 6 · Stretch Goals (optional)

1. **Pagination** – modify `search()` to accept `offset` arg, ask Copilot: “list next 2 matches”.  
2. **File filter** – add `file` query param (`/authdoc?file=overview`).  
3. **Auth header** – enforce `Authorization: Bearer DEMO` to show secure MCP patterns.

---

## 🧩 How It Works Recap

1. **mcp.json** registers a tool → extension sends definition to Copilot backend.  
2. **Prompt** mentions `authDocs` → backend issues a *tool call*.  
3. Extension POSTs to `http://localhost:8000/authdoc` → gets JSON back.  
4. Copilot merges data into a human answer.

No internet needed; everything stays on localhost.

---

## ✅ Quick Checklist

- [ ] All six `pass` blocks replaced.  
- [ ] Flask server runs on port 8000.  
- [ ] Copilot lists `authDocs` in *list tools*.  
- [ ] Sample prompts return excerpts from your Markdown docs.  

If any step fails, restart VS Code or ensure the server is still running.

---

🎉 **You just built a personal knowledge‑base plugin for Copilot—using Copilot!**
