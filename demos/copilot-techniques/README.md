# 🧑‍🏫 MyCorp-Auth MCP Lab

This workshop turns learners into MCP pros by having **Copilot generate the missing pieces** of a Model Context Protocol server. When finished, Copilot Chat will answer questions like "*Explain the token flow in 3 steps*" using **local Markdown docs** that Bing can't see.

---

## 🛠️ Prerequisites

| Tool | Version | Why |
|------|---------|-----|
| Python | 3.11+ | Runs the MCP server |
| VS Code | latest | IDE with Copilot Chat + MCP support |
| GitHub Copilot Chat | enabled | Verify 💡 suggestions appear |

---

## 🚀 Quick Setup

```bash
git clone https://github.com/ps-copilot-sandbox/copilot-fundamentals-training
cd demos/copilot-techniques
code .
```

---

## 📦 Folder Structure

```
copilot-techniques/
├── mycorp-auth-docs/           # your "private" KB
│   ├── overview.md
│   ├── token_flow.md
│   └── troubleshooting.md
├── mcp_auth_docs.py            # ← starter file with 💡 prompts
└── README.md
```

---

## 🎯 What You'll Build

You'll create a custom Model Context Protocol (MCP) server that gives Copilot Chat access to your private documentation. This is like giving Copilot a "private search engine" for your company's internal docs.

**What happens:** 
1. Copilot generates the missing code pieces in a starter MCP server
2. VS Code connects to your local MCP server  
3. You can ask Copilot Chat questions like "*How does token validation work?*" and it will search through your local Markdown files to answer
4. This demonstrates how to extend Copilot with private knowledge that isn't available on the internet

**Why this matters:** MCP is the new standard for connecting AI assistants to private data sources. This lab shows you how to build one from scratch using Copilot itself!

---

## 🏃‍♂️ Step-by-Step Walkthrough

### Step 1: Open the Starter File (2 min)

1. Open `mcp_auth_docs.py` in VS Code
2. You'll see function stubs with `pass` statements and detailed comment prompts for Copilot
3. Each `pass` block has a comment above it explaining what code should go there

### Step 2: Generate Code with Copilot (5-7 min)

**Using the starter file with `pass` blocks:**

| Location | What to do | What Copilot will generate |
|----------|------------|---------------------------|
| **Import section** | Place cursor after existing imports → <kbd>Tab</kbd> | Additional imports like `json, sys, asyncio` |
| **MCP protocol handlers** | Replace `pass` in function stubs → <kbd>Tab</kbd> | MCP request/response handling code |
| **`find_auth_docs()` function** | Replace `pass` → <kbd>Tab</kbd> | File search logic with regex patterns |
| **Main server loop** | Replace `pass` → <kbd>Tab</kbd> | stdin/stdout MCP communication |

**Alternative: Starting from scratch**  
If you prefer, delete everything and use this comprehensive prompt:
```
Create a Model Context Protocol server that searches markdown files in mycorp-auth-docs/ 
folder for authentication documentation. Include tool registration, document search, 
and proper MCP stdin/stdout communication.
```

> 💡 **Trainer Note:** Pause here for questions: "*Why use stdin/stdout instead of HTTP?*" "*How does MCP differ from REST APIs?*"

### Step 3: Test the MCP Server (1 min)

```bash
python3 mcp_auth_docs.py test
# Expected output: "Found 3 documents mentioning 'token'" or similar
```

The server will run automatically when VS Code connects to it via MCP—no need to keep a terminal open.

### Step 4: Configure VS Code MCP Connection (2 min)

1. Open VS Code settings (Cmd/Ctrl + ,)
2. Search for "MCP" or go to Extensions → GitHub Copilot → MCP Servers
3. Add your server configuration:
   ```json
   {
     "name": "authDocs",
     "command": "python3",
     "args": ["mcp_auth_docs.py"],
     "cwd": "./demos/copilot-techniques"
   }
   ```
4. Reload VS Code to activate the MCP connection

### Step 5: Test with Copilot Chat (2 min)

1. Open Copilot Chat sidebar
2. Try these example queries:
   - `@authDocs What is the token flow?`
   - `@authDocs How do I troubleshoot authentication errors?`
   - `@authDocs Explain the authentication overview`
3. Watch Copilot search through your local docs and provide answers!

> 🎉 **Success!** You've just created a custom MCP server that extends Copilot with private knowledge

---

## ✅ Success Criteria

- [ ] All six `pass` blocks replaced or an equivalent script is created.  
- [ ] MCP server responds to test mode correctly.  
- [ ] Copilot lists `authDocs` in *list tools*.  
- [ ] Sample prompts return excerpts from your Markdown docs.

---

## 🚀 Next Steps

After completing this demo, consider:

- **Add more document types**: Extend to search JSON, YAML, or code files
- **Enhance search logic**: Add fuzzy matching or semantic search  
- **Multi-repo support**: Point to multiple knowledge bases
- **Production deployment**: Package as a proper MCP server
