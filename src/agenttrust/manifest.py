from __future__ import annotations

from pathlib import Path
from typing import Any


class ManifestError(Exception):
    """Raised when an AgentTrust manifest cannot be loaded."""


def load_manifest(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise ManifestError(f"manifest not found: {path}")
    if not path.is_file():
        raise ManifestError(f"manifest path is not a file: {path}")

    text = path.read_text(encoding="utf-8")
    manifest = parse_simple_yaml(text)
    if not isinstance(manifest, dict):
        raise ManifestError("manifest did not parse into an object")
    return manifest


def parse_simple_yaml(text: str) -> dict[str, Any]:
    """Parse the small YAML subset used by AgentTrust manifests.

    This intentionally avoids external dependencies for v0.1. It supports the
    current manifest and scenario shape: top-level sections, nested key/value
    pairs, lists of strings, and lists of objects.
    """

    data: dict[str, Any] = {}
    section_name: str | None = None
    current_list_key: str | None = None
    current_list_item: dict[str, Any] | None = None

    for raw_line in text.splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue

        indent = len(raw_line) - len(raw_line.lstrip(" "))
        line = raw_line.strip()

        if indent == 0:
            key, value = split_key_value(line)
            section_name = key
            current_list_key = None
            current_list_item = None

            if value is None:
                data[key] = [] if key in {"tools"} else {}
            else:
                data[key] = parse_scalar(value)
            continue

        if section_name is None:
            raise ManifestError(f"nested line without a section: {line}")

        section = data[section_name]

        if indent == 2 and line.startswith("- "):
            if not isinstance(section, list):
                raise ManifestError(f"list item in non-list section: {section_name}")
            item_text = line[2:].strip()
            key, value = split_key_value(item_text)
            current_list_item = {key: parse_scalar(value or "")}
            section.append(current_list_item)
            continue

        if indent == 2:
            if not isinstance(section, dict):
                raise ManifestError(f"mapping item in non-mapping section: {section_name}")
            key, value = split_key_value(line)
            if value is None:
                section[key] = []
                current_list_key = key
            else:
                section[key] = parse_scalar(value)
                current_list_key = None
            current_list_item = None
            continue

        if indent == 4 and line.startswith("- "):
            if not isinstance(section, dict) or current_list_key is None:
                raise ManifestError(f"list item without a parent list: {line}")
            section[current_list_key].append(parse_scalar(line[2:].strip()))
            continue

        if indent == 4:
            if current_list_item is None:
                raise ManifestError(f"nested mapping without a list object: {line}")
            key, value = split_key_value(line)
            current_list_item[key] = parse_scalar(value or "")
            continue

        raise ManifestError(f"unsupported YAML line: {raw_line}")

    return data


def split_key_value(line: str) -> tuple[str, str | None]:
    if ":" not in line:
        raise ManifestError(f"expected key/value line: {line}")
    key, value = line.split(":", 1)
    key = key.strip()
    value = value.strip()
    return key, value if value else None


def parse_scalar(value: str) -> Any:
    stripped = value.strip()
    if stripped in {"true", "True"}:
        return True
    if stripped in {"false", "False"}:
        return False
    if stripped in {"null", "None"}:
        return None
    if (
        len(stripped) >= 2
        and stripped[0] == stripped[-1]
        and stripped[0] in {"'", '"'}
    ):
        return stripped[1:-1]
    return stripped
