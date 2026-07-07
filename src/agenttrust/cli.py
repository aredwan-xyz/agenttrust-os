from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

from .manifest import ManifestError, load_manifest
from .report import analyze_manifest, render_markdown_report


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="agenttrust",
        description="Scan an AI agent manifest and generate a trust report.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    scan = subparsers.add_parser(
        "scan",
        help="Scan an agenttrust.yaml manifest.",
    )
    scan.add_argument(
        "manifest",
        type=Path,
        help="Path to agenttrust.yaml or agenttrust.example.yaml.",
    )
    scan.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path("reports/trust-report.md"),
        help="Path for the generated Markdown report.",
    )
    return parser


def run_scan(manifest_path: Path, output_path: Path) -> int:
    try:
        manifest = load_manifest(manifest_path)
    except ManifestError as exc:
        print(f"agenttrust: {exc}")
        return 2

    analysis = analyze_manifest(manifest)
    report = render_markdown_report(manifest, analysis)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report, encoding="utf-8")

    print(f"AgentTrust report written to {output_path}")
    print(f"Overall risk: {analysis.overall_risk}")
    print(f"Checks: {analysis.passed_checks}/{len(analysis.checks)} passed")
    return 0 if analysis.failed_checks == 0 else 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "scan":
        return run_scan(args.manifest, args.output)

    parser.error(f"Unknown command: {args.command}")
    return 2
