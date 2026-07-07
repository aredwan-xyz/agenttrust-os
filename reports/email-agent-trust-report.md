# AgentTrust Report

Agent: Client Email Agent
Owner: CodeBeez
Date: 2026-07-07
Overall Risk: High

## Summary

This agent declares 4 tools, including 3 write-capable tools. 7/7 checks passed.

## Checks

| Check | Result | Notes |
|---|---|---|
| Agent identity declared | PASS | Manifest should include agent name and owner. |
| Tools declared | PASS | At least one tool should be listed so permissions can be reviewed. |
| Critical write tools require approval | PASS | All critical write tools require approval. |
| Sensitive fields declared | PASS | Declare private or sensitive fields the agent can access. |
| Human approval policy declared | PASS | Declare actions that require human approval. |
| Prompt-injection blocked patterns declared | PASS | Declare blocked instruction patterns for initial regression tests. |
| Denied actions are logged | PASS | Denied actions should be logged for replay and review. |

## Tools

| Tool | Permission | Risk | Approval Required |
|---|---|---|---|
| gmail.search | read | high | no |
| gmail.draft | write | high | no |
| gmail.send | write | critical | yes |
| hubspot.update_contact | write | high | yes |

## Sensitive Data

- email
- phone
- client_notes
- invoice_status

## Human Approval Policy

- email_send
- payment_action
- crm_write

## Recommended Fixes

1. Add scenario tests next: prompt injection, data leak, and approval bypass.
