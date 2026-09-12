#!/usr/bin/env python3
"""Transparent two-group sample-size approximations from user-supplied inputs."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from statistics import NormalDist


def _probability(name: str, value: float, allow_zero: bool = False) -> float:
    lower_ok = value >= 0 if allow_zero else value > 0
    if not lower_ok or value >= 1:
        bound = "between 0 (inclusive) and 1 (exclusive)" if allow_zero else "greater than 0 and less than 1"
        raise ValueError(f"{name} must be {bound}")
    return value


def _z_for_tail(probability: float) -> float:
    return NormalDist().inv_cdf(probability)


def continuous_two_group(sd: float, delta: float, alpha: float, power: float, attrition: float = 0.0) -> dict[str, object]:
    if sd <= 0 or delta == 0:
        raise ValueError("sd must be > 0 and delta must be non-zero")
    _probability("alpha", alpha)
    _probability("power", power)
    _probability("attrition", attrition, allow_zero=True)
    z_alpha = _z_for_tail(1 - alpha / 2)
    z_power = _z_for_tail(power)
    n_analyzable = math.ceil(2 * (z_alpha + z_power) ** 2 * sd**2 / delta**2)
    n_enrolled = math.ceil(n_analyzable / (1 - attrition))
    return {
        "method": "two-group continuous normal approximation",
        "inputs": {"sd": sd, "delta": delta, "alpha": alpha, "power": power, "attrition": attrition},
        "n_analyzable_per_group": n_analyzable,
        "n_enrolled_per_group": n_enrolled,
        "formula": "ceil(2*(z_(1-alpha/2)+z_power)^2*sd^2/delta^2)",
        "limitations": "Approximation; does not model clustering, repeated measures, multiplicity, or non-normal outcomes.",
    }


def proportion_two_group(p1: float, p2: float, alpha: float, power: float, attrition: float = 0.0) -> dict[str, object]:
    _probability("p1", p1)
    _probability("p2", p2)
    if p1 == p2:
        raise ValueError("p1 and p2 must differ")
    _probability("alpha", alpha)
    _probability("power", power)
    _probability("attrition", attrition, allow_zero=True)
    pooled = (p1 + p2) / 2
    z_alpha = _z_for_tail(1 - alpha / 2)
    z_power = _z_for_tail(power)
    numerator = z_alpha * math.sqrt(2 * pooled * (1 - pooled)) + z_power * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))
    n_analyzable = math.ceil(numerator**2 / (p1 - p2) ** 2)
    n_enrolled = math.ceil(n_analyzable / (1 - attrition))
    return {
        "method": "two-group proportion normal approximation",
        "inputs": {"p1": p1, "p2": p2, "alpha": alpha, "power": power, "attrition": attrition},
        "n_analyzable_per_group": n_analyzable,
        "n_enrolled_per_group": n_enrolled,
        "formula": "ceil((z_alpha*sqrt(2*pbar*(1-pbar))+z_power*sqrt(p1*(1-p1)+p2*(1-p2)))^2/(p1-p2)^2)",
        "limitations": "Approximation; use an appropriate exact or model-based method when assumptions are not met.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="kind", required=True)
    continuous = subparsers.add_parser("continuous")
    continuous.add_argument("--sd", type=float, required=True)
    continuous.add_argument("--delta", type=float, required=True)
    continuous.add_argument("--alpha", type=float, default=0.05)
    continuous.add_argument("--power", type=float, default=0.8)
    continuous.add_argument("--attrition", type=float, default=0.0)
    continuous.add_argument("--output")
    proportion = subparsers.add_parser("proportion")
    proportion.add_argument("--p1", type=float, required=True)
    proportion.add_argument("--p2", type=float, required=True)
    proportion.add_argument("--alpha", type=float, default=0.05)
    proportion.add_argument("--power", type=float, default=0.8)
    proportion.add_argument("--attrition", type=float, default=0.0)
    proportion.add_argument("--output")
    args = parser.parse_args()

    if args.kind == "continuous":
        result = continuous_two_group(args.sd, args.delta, args.alpha, args.power, args.attrition)
    else:
        result = proportion_two_group(args.p1, args.p2, args.alpha, args.power, args.attrition)
    rendered = json.dumps(result, indent=2)
    print(rendered)
    if args.output:
        Path(args.output).write_text(rendered + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
