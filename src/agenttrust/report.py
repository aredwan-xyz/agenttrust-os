from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Any


RISK_SCORE = {
    "low": 1,
    "medium": 2,
    "high": 3,
    "critical": 4,
}


@dataclass(frozen=True)
class Check:
    name: str
    passed: bool
    notes: str


@dataclass(frozen=True)
class Analysis:
    overall_risk: str
    checks: list[Check]
    recommendations: list[str]

    @property
    def passed_checks(self) -> int:
        return sum(1 for check in self.checks if check.passed)

    @property
    def failed_checks(self) -> int:
        return len(self.checks) - self.passed_checks


def analyze_manifest(manifest: dict[str, Any]) -> Analysis:
    agent = manifest.get("agent", {})
    tools = manifest.get("tools", [])
    data = manifest.get("data", {})
    policies = manifest.get("policies", {})

    if not isinstance(agent, dict):
        agent = {}
    if not isinstance(tools, list):
        tools = []
    if not isinstance(data, dict):
        data = {}
    if not isinstance(policies, dict):
        policies = {}

    critical_write_tools = [
        tool
        for tool in tools
        if str(tool.get("permission", "")).lower() == "write"
        and str(tool.get("risk", "")).lower() == "critical"
    ]
    unapproved_critical_tools = [
        tool for tool in critical_write_tools if not tool.get("requires_approval", False)
    ]
    sensitive_fields = data.get("sensitive_fields", [])
    approval_categories = policies.get("require_human_approval_for", [])
    blocked_patterns = policies.get("blocked_patterns", [])

    checks = [
        Check(
            "Agent identity declared",
            bool(agent.get("name") and agent.get("owner")),
            "Manifest should include agent name and owner.",
        ),
        Check(
            "Tools declared",
            bool(tools),
            "At least one tool should be listed so permissions can be reviewed.",
        ),
        Check(
            "Critical write tools require approval",
            not unapproved_critical_tools,
            format_tool_names(unapproved_critical_tools)
            if unapproved_critical_tools
            else "All critical write tools require approval.",
        ),
        Check(
            "Sensitive fields declared",
            bool(sensitive_fields),
            "Declare private or sensitive fields the agent can access.",
        ),
        Check(
            "Human approval policy declared",
            bool(approval_categories),
            "Declare actions that require human approval.",
        ),
        Check(
            "Prompt-injection blocked patterns declared",
            bool(blocked_patterns),
            "Declare blocked instruction patterns for initial regression tests.",
        ),
        Check(
            "Denied actions are logged",
            policies.get("log_denied_actions") is True,
            "Denied actions should be logged for replay and review.",
        ),
    ]

    recommendations = build_recommendations(checks, tools, policies)
    overall_risk = calculate_overall_risk(tools, checks)
    return Analysis(overall_risk=overall_risk, checks=checks, recommendations=recommendations)


def build_recommendations(
    checks: list[Check],
    tools: list[dict[str, Any]],
    policies: dict[str, Any],
) -> list[str]:
    recommendations: list[str] = []

    for check in checks:
        if not check.passed:
            recommendations.append(check.notes)

    write_tools = [
        tool.get("name", "unknown")
        for tool in tools
        if str(tool.get("permission", "")).lower() == "write"
    ]
    if write_tools and "crm_write" not in policies.get("require_human_approval_for", []):
        recommendations.append("Add explicit approval categories for write-capable tools.")

    if not recommendations:
        recommendations.append("Add scenario tests next: prompt injection, data leak, and approval bypass.")

    return dedupe(recommendations)


def calculate_overall_risk(tools: list[dict[str, Any]], checks: list[Check]) -> str:
    max_tool_score = 0
    for tool in tools:
        risk = str(tool.get("risk", "")).lower()
        max_tool_score = max(max_tool_score, RISK_SCORE.get(risk, 0))

    failed_checks = sum(1 for check in checks if not check.passed)
    score = max_tool_score + min(failed_checks, 3)

    if score >= 6:
        return "Critical"
    if score >= 4:
        return "High"
    if score >= 2:
        return "Medium"
    return "Low"


def render_markdown_report(manifest: dict[str, Any], analysis: Analysis) -> str:
    agent = manifest.get("agent", {})
    tools = manifest.get("tools", [])
    data = manifest.get("data", {})
    policies = manifest.get("policies", {})

    lines = [
        "# AgentTrust Report",
        "",
        f"Agent: {agent.get('name', 'Unknown')}",
        f"Owner: {agent.get('owner', 'Unknown')}",
        f"Date: {date.today().isoformat()}",
        f"Overall Risk: {analysis.overall_risk}",
        "",
        "## Summary",
        "",
        summary_sentence(tools, analysis),
        "",
        "## Checks",
        "",
        "| Check | Result | Notes |",
        "|---|---|---|",
    ]

    for check in analysis.checks:
        result = "PASS" if check.passed else "FAIL"
        lines.append(f"| {check.name} | {result} | {check.notes} |")

    lines.extend(["", "## Tools", "", "| Tool | Permission | Risk | Approval Required |", "|---|---|---|---|"])
    for tool in tools:
        lines.append(
            "| {name} | {permission} | {risk} | {approval} |".format(
                name=tool.get("name", "unknown"),
                permission=tool.get("permission", "unknown"),
                risk=tool.get("risk", "unknown"),
                approval="yes" if tool.get("requires_approval") else "no",
            )
        )

    lines.extend(["", "## Sensitive Data", ""])
    sensitive_fields = data.get("sensitive_fields", []) if isinstance(data, dict) else []
    if sensitive_fields:
        for field in sensitive_fields:
            lines.append(f"- {field}")
    else:
        lines.append("- No sensitive fields declared.")

    lines.extend(["", "## Human Approval Policy", ""])
    approvals = policies.get("require_human_approval_for", []) if isinstance(policies, dict) else []
    if approvals:
        for approval in approvals:
            lines.append(f"- {approval}")
    else:
        lines.append("- No explicit approval categories declared.")

    lines.extend(["", "## Recommended Fixes", ""])
    for index, recommendation in enumerate(analysis.recommendations, start=1):
        lines.append(f"{index}. {recommendation}")

    lines.append("")
    return "\n".join(lines)


def summary_sentence(tools: list[dict[str, Any]], analysis: Analysis) -> str:
    write_count = sum(1 for tool in tools if str(tool.get("permission", "")).lower() == "write")
    return (
        f"This agent declares {len(tools)} tools, including {write_count} write-capable tools. "
        f"{analysis.passed_checks}/{len(analysis.checks)} checks passed."
    )


def format_tool_names(tools: list[dict[str, Any]]) -> str:
    return ", ".join(str(tool.get("name", "unknown")) for tool in tools)


def dedupe(items: list[str]) -> list[str]:
    seen: set[str] = set()
    output: list[str] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            output.append(item)
    return output
