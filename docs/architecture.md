# Architecture

AgentTrust OS has five initial layers.

## 1. Manifest Scanner

Reads `agenttrust.yaml` and extracts:

- agent identity
- tools
- permissions
- approval requirements
- sensitive data fields
- blocked patterns
- declared data sources

## 2. Scenario Runner

Runs repeatable safety and reliability scenarios against an agent or mock agent.

Initial scenario categories:

- prompt injection
- data leak
- approval bypass
- tool misuse
- hallucinated action
- unsafe autonomy

## 3. Tool-Call Recorder

Captures a timeline of requested and completed tool calls:

- timestamp
- tool name
- arguments
- approval state
- result
- risk tags

## 4. Risk Analyzer

Combines manifest data, scenario results, and tool-call logs into a practical trust score.

The first version should prioritize explainability over perfect scoring.

## 5. Trust Report

Exports findings as Markdown or HTML:

- overall risk
- pass/fail checks
- risky permissions
- failed scenarios
- replay timeline
- recommended fixes
