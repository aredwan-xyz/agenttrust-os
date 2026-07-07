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
