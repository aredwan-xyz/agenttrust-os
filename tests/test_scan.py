from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from agenttrust.cli import run_scan
from agenttrust.manifest import parse_simple_yaml


class ManifestParserTests(unittest.TestCase):
    def test_parse_example_manifest_shape(self) -> None:
        manifest = parse_simple_yaml(
            """
agent:
  name: "Client Email Agent"
  owner: "CodeBeez"
tools:
  - name: gmail.send
    permission: write
    risk: critical
    requires_approval: true
data:
  sensitive_fields:
    - email
policies:
  log_denied_actions: true
"""
        )

        self.assertEqual(manifest["agent"]["name"], "Client Email Agent")
        self.assertEqual(manifest["tools"][0]["name"], "gmail.send")
        self.assertTrue(manifest["tools"][0]["requires_approval"])
        self.assertEqual(manifest["data"]["sensitive_fields"], ["email"])


class ScanCommandTests(unittest.TestCase):
    def test_scan_writes_report(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            manifest_path = root / "agenttrust.yaml"
            report_path = root / "reports" / "trust-report.md"
            manifest_path.write_text(
                """
agent:
  name: "Client Email Agent"
  owner: "CodeBeez"
tools:
  - name: gmail.send
    permission: write
    risk: critical
    requires_approval: true
data:
  sensitive_fields:
    - email
policies:
  log_denied_actions: true
  require_human_approval_for:
    - email_send
  blocked_patterns:
    - "ignore previous instructions"
""",
                encoding="utf-8",
            )

            exit_code = run_scan(manifest_path, report_path)

            self.assertEqual(exit_code, 0)
            report = report_path.read_text(encoding="utf-8")
            self.assertIn("# AgentTrust Report", report)
            self.assertIn("Overall Risk:", report)
            self.assertIn("Client Email Agent", report)


if __name__ == "__main__":
    unittest.main()
