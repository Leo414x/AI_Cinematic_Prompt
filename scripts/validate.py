#!/usr/bin/env python3
"""Static regression checks for the public cinematic prompt skill."""

from pathlib import Path
import json
import re
import sys


ROOT = Path(__file__).resolve().parents[1]


def read(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def require(text: str, token: str, label: str, errors: list[str]) -> None:
    if token not in text:
        errors.append(f"{label}: missing required contract: {token}")


def forbid(text: str, token: str, label: str, errors: list[str]) -> None:
    if token in text:
        errors.append(f"{label}: forbidden regression token remains: {token}")


def main() -> int:
    errors: list[str] = []
    skill = read("SKILL.md")
    adapter = read("adapters/general.md")
    params = read("references/params.md")
    presets = read("references/presets.md")
    anti_slop = read("anti-slop-system.md")
    changelog = read("CHANGELOG.md")
    cases = json.loads(read("tests/depth-cases.json"))

    version_match = re.search(r"^\s+version:\s*([0-9]+\.[0-9]+\.[0-9]+)$", skill, re.M)
    if not version_match:
        errors.append("SKILL.md: missing semantic version")
    elif f"## {version_match.group(1)}" not in changelog:
        errors.append("CHANGELOG.md: current SKILL.md version has no entry")

    require(skill, "choose exactly one primary fallback", "SKILL.md", errors)
    require(skill, "Treat preset `foreground` values as candidates", "SKILL.md", errors)
    require(skill, "plausible medium", "SKILL.md", errors)
    require(skill, "space never receives atmospheric haze", "SKILL.md", errors)
    require(skill, "subject remains the highest-priority signal", "SKILL.md", errors)
    forbid(skill, "前后景层次分离，空气透视带来大气纵深。", "SKILL.md", errors)

    require(adapter, "## Depth And Atmosphere Fuse Terms", "adapters/general.md", errors)
    require(adapter, "Do not add atmospheric haze or particulate shafts", "adapters/general.md", errors)
    require(adapter, "Require both a plausible medium and a motivated light source", "adapters/general.md", errors)
    require(params, "smoke_haze | 烟雾/薄雾（条件）", "references/params.md", errors)
    require(params, "do not add fog by default", "references/params.md", errors)
    require(anti_slop, "volumetric light only with a plausible medium", "anti-slop-system.md", errors)
    forbid(anti_slop, "keep filmic highlight rolloff + practical atmospheric haze", "anti-slop-system.md", errors)

    smoke_haze_rows = [
        line for line in presets.splitlines() if "| foreground | smoke_haze |" in line
    ]
    if not smoke_haze_rows:
        errors.append("references/presets.md: no smoke_haze rows found")
    for row in smoke_haze_rows:
        if "条件候选" not in row:
            errors.append(f"references/presets.md: unconditional smoke_haze preset: {row}")

    required_case_ids = {
        "foggy-forest-motivated",
        "desert-clear-air",
        "vacuum-orbital-ruin",
        "dusty-hangar-shaft",
        "clean-sealed-corridor",
        "multi-subject-city-distance",
    }
    actual_case_ids = {case.get("id") for case in cases}
    if len(actual_case_ids) != len(cases):
        errors.append("tests/depth-cases.json: case IDs must be unique")
    missing_cases = required_case_ids - actual_case_ids
    if missing_cases:
        errors.append(f"tests/depth-cases.json: missing regression axes: {sorted(missing_cases)}")
    for case in cases:
        for field in ("id", "scene", "expected_depth", "must_preserve", "must_avoid"):
            if not case.get(field):
                errors.append(f"tests/depth-cases.json: {case.get('id', '<unknown>')} missing {field}")

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Validation passed: version, depth discipline, atmosphere gating, and G2 safeguards are present.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
