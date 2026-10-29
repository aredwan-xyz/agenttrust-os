# Architecture

This is the target architecture. The current implementation reads a manifest, evaluates its declarations and writes a Markdown report. It does not execute agents or record runtime behavior.

## 1. Manifest Scanner

Reads `agenttrust.yaml` and extracts:

- agent identity
- tools
- permissions
- approval requirements
- sensitive data fields
- blocked patterns
- declared data sources

## 2. Scenario Runner (planned)

Runs repeatable safety and reliability scenarios against an agent or mock agent.

Initial scenario categories:

- prompt injection
- data leak
- approval bypass
- tool misuse
- hallucinated action
- unsafe autonomy

## 3. Tool-Call Recorder (planned)

Captures a timeline of requested and completed tool calls:

- timestamp
- tool name
- arguments
- approval state
- result
- risk tags

## 4. Risk Analyzer

Today, evaluates manifest declarations for missing controls and risky permissions. Combining actual scenario results and tool-call logs is planned.

The first version should prioritize explainability over perfect scoring.

## 5. Trust Report

Today, exports manifest findings as Markdown. HTML export, failed runtime scenarios and replay are planned:

- overall risk
- pass/fail checks
- risky permissions
- failed scenarios
- replay timeline
- recommended fixes
