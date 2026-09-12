#!/usr/bin/env python3
"""Artifact-level checks for a generated preclinical design project."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

BASE_FILES = {
    "01_research_question.md",
    "02_literature_review.md",
    "03_search_saturation_log.md",
    "04_evidence_matrix.csv",
    "05_quality_appraisal.csv",
    "06_source_manifest.csv",
    "16_audit_trail.md",
    "17_gate_status.md",
}
MODE_FILES = {
    "review": set(),
    "roadmap": {"07_experimental_roadmap.md"},
    "protocol": {
        "07_experimental_roadmap.md",
        "09_reagent_preparation.md",
        "10_materials_equipment.csv",
        "11_statistical_plan.md",
        "12_protocol_flowchart.mmd",
    },
    "audit": {"15_protocol_audit.md"},
}


def validate_project(root: Path, mode: str) -> dict[str, object]:
    required = sorted(BASE_FILES | MODE_FILES[mode])
    present = [name for name in required if (root / name).is_file()]
    missing = [name for name in required if name not in present]
    if mode == "protocol":
        protocol_files = sorted(root.glob("08_phase_*_protocol.md"))
        if protocol_files:
            present.append(protocol_files[0].name)
        else:
            missing.append("08_phase_<name>_protocol.md")
    gate_text = (root / "17_gate_status.md").read_text(encoding="utf-8") if (root / "17_gate_status.md").is_file() else ""
    gate_keywords = ["PASS", "PASS-WITH-BLOCKERS", "BLOCKED"]
    return {
        "schema": "preclinical-experimental-design/artifact-check/v1",
        "root": str(root),
        "mode": mode,
        "required": required,
        "present": present,
        "missing": missing,
        "gate_status_file_contains_status": any(keyword in gate_text for keyword in gate_keywords),
        "valid_artifact_structure": not missing,
        "note": "Artifact structure checks do not establish scientific validity, safety, ethics approval, or citation integrity.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--mode", choices=sorted(MODE_FILES), required=True)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    report = validate_project(args.root, args.mode)
    rendered = json.dumps(report, indent=2)
    print(rendered)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(rendered + "\n", encoding="utf-8")
    return 0 if report["valid_artifact_structure"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
