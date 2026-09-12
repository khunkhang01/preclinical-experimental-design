#!/usr/bin/env python3
"""Optional evidence-matrix visualization using pandas and matplotlib."""

from __future__ import annotations

import argparse
from pathlib import Path


def evidence_heatmap(input_csv: Path, output_png: Path) -> None:
    try:
        import matplotlib.pyplot as plt
        import pandas as pd
    except ImportError as exc:  # pragma: no cover - environment dependent
        raise RuntimeError("evidence heatmaps require pandas and matplotlib") from exc

    frame = pd.read_csv(input_csv)
    required = {"parameter_name", "confidence"}
    missing = required.difference(frame.columns)
    if missing:
        raise ValueError(f"CSV is missing columns: {', '.join(sorted(missing))}")
    table = pd.crosstab(frame["parameter_name"].fillna("(unlabelled)"), frame["confidence"].fillna("(ungraded)"))
    order = [column for column in ["HIGH", "MODERATE", "LOW", "INSUFFICIENT", "(ungraded)"] if column in table.columns]
    table = table[order] if order else table
    output_png.parent.mkdir(parents=True, exist_ok=True)
    figure, axis = plt.subplots(figsize=(max(7, len(table.columns) * 1.2), max(4, len(table) * 0.35)))
    image = axis.imshow(table.to_numpy(), aspect="auto", cmap="Blues")
    axis.set_xticks(range(len(table.columns)), table.columns, rotation=30, ha="right")
    axis.set_yticks(range(len(table.index)), table.index)
    axis.set_xlabel("Confidence grade")
    axis.set_ylabel("Parameter")
    axis.set_title("Evidence-matrix row counts by parameter and confidence")
    figure.colorbar(image, ax=axis, label="Rows")
    figure.tight_layout()
    figure.savefig(output_png, dpi=180)
    plt.close(figure)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    evidence_heatmap(args.input, args.output)
    print(f"wrote {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
