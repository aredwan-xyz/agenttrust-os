# Good First Issues

These are intentionally scoped so contributors can help without understanding the whole project.

## Scenario Packs

1. Add `scenarios/data-leak.yaml`
   - Test whether an agent tries to export sensitive data.

2. Add `scenarios/tool-misuse.yaml`
   - Test whether an agent calls a write tool for a read-only task.

3. Add `scenarios/hallucinated-action.yaml`
   - Test whether an agent claims it completed an action without a tool-call record.

## Example Agents

4. Add `examples/calendar-agent/agenttrust.yaml`
   - Include calendar read, event draft, and event create tools.

5. Add `examples/crm-agent/agenttrust.yaml`
   - Include lead search, note creation, and contact update tools.

6. Add `examples/file-agent/agenttrust.yaml`
   - Include file read, file write, and export tools.

## Core Checks

7. Warn when write tools exist but no approval policy exists.

8. Warn when sensitive fields exist but no blocked patterns exist.

9. Add a report section for missing recommended scenarios.

## Integrations

10. Prototype an n8n workflow parser.

11. Prototype a Dify app parser.

12. Prototype an OpenAI Agents SDK adapter.
