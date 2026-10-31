# Launch Kit

Use this when sharing AgentTrust OS publicly.

## One-Line Hook

I built an open-source flight recorder and preflight safety checklist for AI agents.

## Short Description

AgentTrust OS scans an AI agent manifest, maps tools and permissions, checks human approval rules, and generates a trust report before the agent touches real business systems.

## LinkedIn Launch Post

Hook:

AI agents are moving from "answer this" to "do this."

Post:

That changes the risk profile.

If an agent can send emails, update a CRM, read customer notes, or trigger automations, the question is no longer just "does it work?"

The question is:

- What tools can it access?
- What data can it see?
- Which actions require human approval?
- Can we replay what happened?
- Can we catch risky behavior before launch?

So I started building AgentTrust OS: an open-source flight recorder and preflight safety checklist for AI agents.

The first version is simple:

- `agenttrust.yaml` manifest
- permission and data-access scan
- human approval checks
- Markdown trust report
- starter prompt-injection and approval-bypass scenarios

It is early, but useful already.

My goal is to make AI agents more inspectable before they act on behalf of real businesses.

Repo: https://github.com/aredwan-xyz/agenttrust-os

CTA:

If you are building agents with tool access, I would appreciate feedback on the manifest format and the first trust report.

Suggested visual:

Screenshot of `reports/trust-report.md` or terminal output from `agenttrust scan`.

Target audience:

AI builders, automation consultants, startup founders, security-minded developers.

Why this builds trust:

It shows a working artifact, a specific risk, and a responsible framing without claiming the tool solves all AI safety.

Risk or claim to verify:

Do not claim production-grade safety yet. Say "early", "starter", or "first version."

## X / Threads Post

AI agents need a preflight checklist before they touch real tools.

I started AgentTrust OS: an open-source manifest scanner and trust-report generator for AI agents.

It checks tools, permissions, sensitive data, approval rules, and risky access.

Repo: https://github.com/aredwan-xyz/agenttrust-os

## Hacker News Title Ideas

- Show HN: AgentTrust OS - a preflight safety checklist for AI agents
- Show HN: I built a manifest scanner and trust report for AI agents
- Show HN: AgentTrust OS - inspect agent tools, permissions, and approval rules

## Reddit / Community Post

Title:

I built a small open-source tool to inspect AI agent permissions before deployment

Body:

I have been thinking about a problem that keeps showing up with agentic workflows: once an agent can call tools, the hard part is not only prompt quality. It is visibility.

I started AgentTrust OS as a local-first CLI that scans an `agenttrust.yaml` manifest and generates a Markdown trust report.

It currently checks:

- declared tools
- read/write permissions
- critical write actions
- sensitive fields
- human approval rules
- prompt-injection blocked patterns
- denied-action logging

It is early, but I would love feedback from people building agents with tool access.

Repo: https://github.com/aredwan-xyz/agenttrust-os

## Product Hunt Tagline

Preflight safety checks and trust reports for AI agents.

## 7-Day Launch Sequence

Day 1:

- Post the LinkedIn launch note.
- Ask 5 AI builders for feedback on the manifest format.

Day 2:

- Share a screenshot of the generated trust report.

Day 3:

- Publish a short build log: why passing checks can still leave overall risk high.

Day 4:

- Open 5 good-first issues.

Day 5:

- Share a short demo clip or terminal GIF.

Day 6:

- Post a technical breakdown of the `agenttrust.yaml` format.

Day 7:

- Ask for scenario contributions: prompt injection, data leak, tool misuse, approval bypass.

---

# Launch Kit v2: the version built for skeptics

The first kit leads with a passing report. A reader who only ever sees `7/7 passed`
will assume the tool rubber-stamps everything. Lead with the failure instead.

## The demo that earns trust: make it say no

```bash
git clone https://github.com/aredwan-xyz/agenttrust-os.git
cd agenttrust-os

# a careful agent: passes, but overall risk stays High because it can write
PYTHONPATH=src python3 -m agenttrust scan agenttrust.example.yaml

# a reckless agent: sends email and issues refunds with nobody approving
PYTHONPATH=src python3 -m agenttrust scan examples/unsafe-agent/agenttrust.yaml
```

The second command prints `Overall risk: Critical` and `Checks: 2/7 passed`, and exits
with code `1`, so it can gate a CI step today. See
[reports/unsafe-agent-report.md](../reports/unsafe-agent-report.md).

Record this as a 15 second terminal GIF (two commands, no narration) and put it at the
top of the README. It is the single highest-leverage asset.

## Show HN

**Title** (pick one, under 80 chars, no superlatives):

- `Show HN: AgentTrust, a preflight check for what your AI agent is allowed to do`
- `Show HN: A zero-dependency CLI that fails CI when an agent can act unapproved`

**URL:** https://github.com/aredwan-xyz/agenttrust-os

**First comment** (post it yourself the moment the submission is up):

> Hi HN. I build automation workflows for small businesses, and the same worry kept
> recurring: once an agent can send email or touch a CRM, "does it work?" stops being
> the main question. "What is it allowed to do, and who approves it?" is.
>
> AgentTrust is a small local CLI. You describe an agent in an `agenttrust.yaml`
> manifest (tools, read/write permission, risk, sensitive fields, approval policy), and
> `agenttrust scan` produces a Markdown trust report. It exits non-zero when checks
> fail, so you can put it in CI.
>
> What it does NOT do, so you don't have to ask: it checks the manifest, not the running
> agent. It cannot tell you whether your agent actually honors the policy you wrote. It
> is a review checklist that forces the permissions to be written down and diffable, not
> a sandbox or a guarantee. The scenario runner (prompt injection, approval bypass, data
> leak) is the next milestone; the scenario files exist but nothing executes them yet.
>
> Python 3.9+, no runtime dependencies, MIT. The part I would most like feedback on is
> the manifest format: is it expressive enough for the agents you actually run?

Why this framing works: it answers the obvious objection ("it only reads your own
YAML") before anyone has to raise it, which is what keeps the top comment from being a
takedown.

## FAQ: answers for the hard questions

**"It only checks what you declare. A lying manifest passes."**
Correct, and the README says so. The value of v0.1 is a reviewable, version-controlled
record of agent permissions plus a CI gate on it, the same way a lockfile makes
dependencies reviewable without proving the dependencies are safe. Runtime enforcement
is the roadmap, not a claim.

**"How is this different from guardrails libraries?"**
Those sit inside the agent's runtime and filter inputs/outputs. This sits outside it
and reviews what the agent is permitted to touch, before deployment. They compose.

**"Why a custom YAML parser?"**
Zero dependencies for v0.1 so it runs anywhere with Python. The parser supports a small
subset on purpose. If the manifest outgrows it, switching to PyYAML is a small change.

**"Is `Overall risk: High` on a 7/7 pass a bug?"**
No. Passing controls do not remove the exposure of a write-capable tool. Risk reflects
what the agent can do; checks reflect whether the safeguards are declared.

## Where to post, in order

| Day | Channel | Angle |
|---|---|---|
| 1, Tue to Thu, ~8am US Eastern | Show HN | Use the post above. Stay in the thread for 3 hours. |
| 1 | LinkedIn | Existing post; add the unsafe-agent screenshot. |
| 2 | r/LocalLLaMA, r/AI_Agents | "Open-sourced a CI gate for agent permissions" with the GIF. |
| 3 | X / Threads | The unsafe-agent report as an image: `Critical, 2/7`. |
| 4 | OpenAI Agents SDK, LangChain, n8n communities | Link the matching adapter issue and ask for the manifest of a real agent. |
| 5+ | Awesome-lists for AI agent safety/security | Open a PR once there are a few stars and a GIF. |

Do not post to every channel on the same day: the point is to be present in each
thread, not to maximise surface area.

## Before you post: checklist

- [ ] GIF of the two-command demo is at the top of the README
- [ ] Repo description and 5+ topics set (`ai-agents`, `ai-safety`, `llm-security`, `cli`, `python`)
- [ ] Social preview image uploaded (Settings -> Social preview)
- [ ] `v0.1.0` release tagged so there is something to link
- [ ] Five good-first-issues open and labelled (two already are)
- [ ] You can reply within minutes for the first three hours

## Claims you can and cannot make

| Can say | Cannot say |
|---|---|
| "Fails CI (exit 1) when critical write tools lack approval" | "Makes agents safe" |
| "Zero runtime dependencies" | "Detects prompt injection" (the scenarios are not run yet) |
| "Local-first, no data leaves your machine" | "Production-grade" or "enterprise-ready" |
| "Early, v0.1, feedback wanted" | "Compliance" or "certified" of any kind |
