# 🛡️ Emergency Log Triage Demo

## 🚀 What You’ll Build
In this short lab you’ll use **GitHub Copilot** to transform a bare‑bones skeleton into a working Python utility that:

1. Streams either plain or gzipped access‑log files.  
2. Filters entries from the **last *N* minutes**.  
3. Tallies `(HTTP‑status, endpoint)` pairs.  
4. Prints a compact Markdown‑style histogram.  

The goal isn’t perfect code—it’s to **see Copilot’s UI and autocompletion magic in action**. You’ll prompt Copilot from comment blocks, accept (or finesse) its suggestions, and watch it generate production‑style boilerplate in seconds. 🪄

---

## 🗂️ Repository Layout

| Path | Purpose |
|------|---------|
| `triage.py` | The starter script with **function stubs** and embedded Copilot prompts. |
| `sample_access.log.gz` | A 1 000‑line gzipped access‑log spanning the last hour, containing a mix of 2xx/4xx/5xx, plus custom `499` and `321` errors for testing. |
| `README.md` | The instructions for this demo. |

---

## 🛠️ Prerequisites

| Tool | Version | Notes |
|------|---------|-------|
| Python | 3.8 + | Standard library only—no external packages required. |
| VS Code | Latest | Any IDE that supports GitHub Copilot will work, but the steps below assume VS Code. |
| GitHub Copilot | Enabled | Make sure the extension is signed‑in and working (check for 💡 suggestions). |

---

## 🧑‍💻 Hands‑On Walkthrough

### 1 . Clone & Open
```bash
git clone https://github.com/ps-copilot-sandbox/copilot-fundamentals-training.git
cd demos/copilot-essentials/
code .
```

### 2 . Explore the Skeleton
Open **`triage.py`**. Every function body is just `pass` and is preceded by a short **Copilot prompt** (triple‑quoted).  
Example:

```python
def read_lines(file_path: Path) -> Iterable[str]:
    """Open plain or gzipped log file and yield each line (stripped)."""
    pass  # ← Copilot will fill this in
```

### 3 . Invoke Copilot ✨
1. **Highlight** the entire function (or place the cursor on `pass`).  
2. Hit **<kbd>Tab</kbd>** (or your Copilot “Accept Suggestion” shortcut).  
3. Copilot inserts a full implementation—review & accept.  
4. Repeat for each function (`parse_line`, `triage`, `render`, `main`).  

> 💡 **Tip:** You are encouraged to **read Copilot’s diff**; ask *“Why did it choose this regex?”* or *“Where’s the error handling?”*.

### 4 . Run the Script
```bash
python triage.py --file sample_access.log.gz --minutes 15 --status 499,321 --top 10
```

Expected output (truncated):

```
Rank | Status | Path               | Hits
-----|--------|--------------------|-----
 1   | 499    | /api/v1/users      | 9
 2   | 321    | /login             | 4
 ...
```

Feel free to omit `--status` to see **all** codes, or change `--minutes` and `--top`.

### 5 . Experiment
- **Change prompts** to ask for a progress bar or CSV export—then re‑run Copilot.  
- **Break the log format** in a few lines and see if your `parse_line` gracefully skips invalid entries.  
- **Swap in real logs** from your dev stack (keep them in `.log` or `.log.gz`).  

---

## 🔍 Inside `sample_access.log.gz`

* Format: **Apache/Nginx “combined” access log** (`ip – – [timestamp] "METHOD path HTTP/x.y" status size ...`).  
* Time span: past 60 minutes, randomised per run.  
* Status codes: normal 2xx & 3xx, plus plenty of `400`, `404`, `499`, `500`, `503` and a handful of **custom `321`**.  
* Endpoints: typical REST routes (`/api/v1/*`), static assets, health checks.

> 🗒️ **Why gzipped?** Real systems rotate & compress logs; beginners learn to handle both transparently.

---

## 🎯 Learning Objectives

| ✅ Skill | Demonstrated by |
|----------|-----------------|
| Prompt‑driven code generation | Turning comment blocks into working Python functions. |
| Incremental acceptance | Reviewing, refining, or rejecting Copilot suggestions. |
| Code explanation & learning | Using Copilot Chat to understand WHY code works, not just WHAT it does. |
| Neighboring Tab Suggestions (NES) | Experiencing how Copilot learns from your patterns within the same file. |
| Error resolution | Using `/fix` command to automatically resolve coding issues. |
| Log processing patterns | Lazy file streaming, regex parsing, `collections.Counter`. |
| Basic CLI ergonomics | Using `argparse` & helpful `--help` text. |

---

## 💬 Common Questions

| Q | A |
|---|---|
| “Why not use pandas?” | The lab is designed to stay in standard lib so no installs block your flow. |
| “Does Copilot always nail it first try?” | No—guide it! Move the cursor, tighten the prompt, or type the first line yourself. |
| “How big can the log be?” | Reading line‑by‑line uses constant memory; size is limited only by disk space. |

---

## 🧩 Stretch Challenges

1. **Add a `--dry‑run` flag** that prints how many lines *would* be processed without running the regex.  
2. **Output CSV** with `status,path,hits` so analysts can import it.  
3. **Threaded version**: parallel‑parse multiple log files in a directory.  
4. **Unit tests**: stub a tiny log sample and verify counter outputs.

---

## 📚 Further Reading

* [GitHub Copilot Docs → “Prompt Tips & Tricks”](https://docs.github.com/en/copilot)  
* Python docs: [`datetime`](https://docs.python.org/3/library/datetime.html), [`re`](https://docs.python.org/3/library/re.html), [`argparse`](https://docs.python.org/3/library/argparse.html)  
* Real‑world inspiration: [Nginx Log Formats](https://nginx.org/en/docs/http/ngx_http_log_module.html)

---

### 🎉 You’re Done!

Fire up Copilot, generate the code, and impress your team with a **one‑off script** that would normally take an hour—now built in minutes. Happy triaging! 🥳
