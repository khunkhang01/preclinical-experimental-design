#!/usr/bin/env python3
"""Calculate a direct C1V1=C2V2 dilution without silently converting units."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def calculate(stock_concentration: float, target_concentration: float, final_volume: float, concentration_unit: str, volume_unit: str) -> dict[str, object]:
    if stock_concentration <= 0 or target_concentration <= 0 or final_volume <= 0:
        raise ValueError("stock concentration, target concentration, and final volume must be > 0")
    if target_concentration > stock_concentration:
        raise ValueError("target concentration cannot exceed stock concentration for a direct dilution")
    stock_volume = target_concentration * final_volume / stock_concentration
    vehicle_volume = final_volume - stock_volume
    return {
        "method": "C1V1=C2V2 direct dilution",
        "inputs": {
            "stock_concentration": stock_concentration,
            "target_concentration": target_concentration,
            "final_volume": final_volume,
            "concentration_unit": concentration_unit,
            "volume_unit": volume_unit,
        },
        "outputs": {
            "stock_volume": stock_volume,
            "vehicle_volume_to_make_up": vehicle_volume,
            "stock_volume_unit": volume_unit,
            "vehicle_volume_unit": volume_unit,
        },
        "assumptions": [
            "Concentration bases are compatible.",
            "Final volume is made up to the stated total after stock addition.",
            "No potency, density, overage, adsorption, or stability correction was applied.",
        ],
        "verification_required": ["identity/potency", "vehicle compatibility", "stability", "label/storage/disposal"],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stock-concentration", type=float, required=True)
    parser.add_argument("--target-concentration", type=float, required=True)
    parser.add_argument("--final-volume", type=float, required=True)
    parser.add_argument("--concentration-unit", required=True)
    parser.add_argument("--volume-unit", required=True)
    parser.add_argument("--output")
    args = parser.parse_args()
    result = calculate(args.stock_concentration, args.target_concentration, args.final_volume, args.concentration_unit, args.volume_unit)
    rendered = json.dumps(result, indent=2)
    print(rendered)
    if args.output:
        Path(args.output).write_text(rendered + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
