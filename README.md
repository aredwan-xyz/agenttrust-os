# AgentTrust OS

The open-source flight recorder and safety checklist for AI agents.

AgentTrust OS helps builders inspect AI agents before they touch real tools, private data, customers, CRMs, inboxes, calendars, files, payments, or production systems.

## Why

AI agents are starting to act, not just answer. That means builders need more than a nice demo. They need to know:

- what tools the agent can access
- what data it can see
- whether write actions require approval
- whether prompt-injection attacks work
- whether sensitive data can leak
- what the agent actually did during a run
- how to replay and explain failures

AgentTrust OS gives every agent a manifest, risk scan, adversarial test suite, tool-call timeline, and exportable trust report.

## What It Does

- Scans an `agenttrust.yaml` manifest
- Maps tools, data access, approval rules, and risky permissions
- Runs prompt-injection, data-leak, tool-misuse, and approval-bypass scenarios
- Records tool calls and agent actions
- Generates a trust report with pass/fail checks and recommended fixes
- Provides a local dashboard for replaying agent behavior

## Quick Demo

```bash
git clone https://github.com/aredwan-xyz/agenttrust-os.git
cd agenttrust-os

# Run from source without installing
PYTHONPATH=src python3 -m agenttrust scan agenttrust.example.yaml

# Or install the local CLI
python3 -m pip install -e .
agenttrust scan agenttrust.example.yaml
```

## Example Manifest

```yaml
agent:
  name: "Client Email Agent"
  owner: "CodeBeez"
  description: "Drafts and classifies client emails."

tools:
  - name: gmail.search
    permission: read
    risk: high
    requires_approval: false
  - name: gmail.send
    permission: write
    risk: critical
    requires_approval: true
  - name: hubspot.update_contact
    permission: write
    risk: high
    requires_approval: true

data:
  sensitive_fields:
    - email
    - phone
    - client_notes
    - invoice_status

policies:
  allow_external_send: false
  require_human_approval_for:
    - email_send
    - payment_action
    - crm_write
```

## Sample Trust Report

```text
Agent: Client Email Agent
Overall Risk: High

Checks:
- Manifest present: PASS
- Critical write tools require approval: PASS
- Sensitive fields declared: PASS
- Prompt-injection scenario: FAIL
- Data exfiltration scenario: PASS
- Approval bypass scenario: FAIL

Recommended fixes:
1. Add refusal rule for external-send requests.
2. Block CRM write actions unless approved by a human.
3. Log every attempted write action, including denied actions.
```

## Architecture

```mermaid
flowchart LR
  A["agenttrust.yaml"] --> B["Manifest Scanner"]
  C["Scenario Pack"] --> D["Test Runner"]
  E["Agent / Mock Agent"] --> D
  D --> F["Tool Call Recorder"]
  B --> G["Risk Analyzer"]
  F --> G
  G --> H["Trust Report"]
  G --> I["Dashboard"]
```

## Roadmap

- v0.1: CLI manifest scanner and Markdown trust report
- v0.2: scenario runner with mock agents
- v0.3: local dashboard and replay timeline
- v0.4: n8n workflow parser
- v0.5: LangChain and OpenAI Agents SDK adapters
- v0.6: CI check for agent trust reports

## Use Cases

- AI agencies proving client workflows are safe before launch
- developers testing prompt-injection resistance
- teams reviewing agent permissions before deployment
- founders comparing agent versions
- educators teaching responsible AI automation

## What This Is Not

AgentTrust OS is not a guarantee that an AI system is safe, secure, compliant, or medically/legally reliable. It is a practical development and review tool that helps builders find risks earlier, document behavior, and add human approval gates where they matter.

## Contributing

Useful first contributions:

- Add a new attack scenario
- Improve the risk scoring model
- Add a sample agent
- Add an adapter for a popular agent framework
- Improve report design
- Add documentation examples

## License

MIT
