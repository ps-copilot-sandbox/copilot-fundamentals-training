# Copilot Agents Demo

Use the following 3 files to setup your Copilot Agents demo. 
Paste the ISSUE.md file into a new issue in that repository. 

## What this demo shows
- Assign an issue to Copilot to start an agent task
- Monitor progress in AgentHQ
- Re-steer mid-session with a new requirement
- Review the resulting PR like a teammate’s work

## Demo files
- `ISSUE.md` contains the exact issue text to copy/paste into GitHub
- `STEER.md` contains the mid-session requirement change to paste while the agent is working

## Quick demo steps
1. Create a new GitHub Issue by copying the Title and Body from `ISSUE.md`
2. Assign the issue to Copilot to start the agent task
3. Open AgentHQ to monitor progress
4. Paste `STEER.md` into the agent session to re-steer the work
5. Review the PR diff for clarity, completeness, and constraints.
6. Verify the PR edited the README.md file by adding priority levels plus the steered examples. 

---

## Ticket Triage Policy (Current)

Severity measures impact; Priority (P0–P3) sets handling order. Review tickets daily and work highest priority first.

| Severity | Impact | Default priority |
|---|---|---|
| High | Blocks key workflows or causes data loss | P1 |
| Medium | Meaningful impact, but a workaround exists | P2 |
| Low | Minor annoyance with an easy workaround | P3 |

| Priority | Meaning / handling |
|---|---|
| P0 | Active widespread outage or ongoing severe data loss; respond immediately. Escalate from any severity. |
| P1 | Urgent key-workflow blocker or data loss; address first, same day. |
| P2 | Meaningful but contained impact; schedule ahead of low-priority work. |
| P3 | Minor impact; handle as capacity allows. |

### Triage in 60 seconds
1. **0–15s:** Identify affected users, workflows, and whether impact is ongoing or widespread.
2. **15–30s:** Confirm severity and whether a workaround exists; note any data loss.
3. **30–45s:** Set the mapped priority; use P0 for an active widespread outage or ongoing severe data loss.
4. **45–60s:** Record the impact, severity, priority, and next action on the ticket.
