#!/usr/bin/env python3
"""Generate a reproducible simple allocation from explicit user inputs."""

from __future__ import annotations

import argparse
import csv
import random
from pathlib import Path


def generate(groups: list[str], n_per_group: int, seed: int, prefix: str = "unit") -> list[dict[str, object]]:
    if len(groups) < 2 or any(not group.strip() for group in groups):
        raise ValueError("provide at least two non-empty group labels")
    if n_per_group <= 0:
        raise ValueError("n_per_group must be > 0")
    assignments = [group.strip() for group in groups for _ in range(n_per_group)]
    rng = random.Random(seed)
    rng.shuffle(assignments)
    return [{"unit_id": f"{prefix}-{index:04d}", "group": group, "stratum": "", "seed": seed} for index, group in enumerate(assignments, start=1)]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--groups", required=True, help="comma-separated group labels")
    parser.add_argument("--n-per-group", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--prefix", default="unit")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows = generate(args.groups.split(","), args.n_per_group, args.seed, args.prefix)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["unit_id", "group", "stratum", "seed"])
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {len(rows)} allocations to {args.output}")
    print("record the seed, allocation owner, concealment, blinding, and deviations in the audit trail")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
