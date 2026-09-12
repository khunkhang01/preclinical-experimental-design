# Reagent preparation and calculation rules

## Required record

For every reagent, formulation, extract, vehicle, or delivery preparation,
record identity, source/grade, purity or marker, lot, stock concentration,
solvent/vehicle, target concentration, final volume, calculation, units,
mixing/order, pH/osmolality where relevant, filtration/sterility/endotoxin
requirements, storage, stability/expiry, temperature/light controls, aliquot,
label, discard, and safety/waste instructions.

For natural products and formulations, record authentication, batch, extraction
or manufacturing process, yield, marker/active basis, excipients, particle size
or release attributes, and between-batch comparability when relevant.

## Calculation rules

- Use an explicit dimensional equation and show all substituted inputs.
- Require compatible units; never silently convert or assume density/potency.
- Use `C1V1 = C2V2` only when both concentration bases and final-volume
  definitions are compatible.
- State whether the final volume is made up after adding stock or is the total
  dispensed volume.
- Round only at the final actionable step and record the rounding rule.
- Include an overage only when explicitly justified and labelled.
- Recalculate every dilution after changing stock, potency, volume, or vehicle.

The bundled `scripts/dilution_calculator.py` is a transparent arithmetic helper;
it does not decide a scientifically valid concentration or a safe preparation.

## Stability and feasibility

If stability, adsorption, precipitation, degradation, light sensitivity,
sterility, or compatibility is not verified for the actual material and time,
mark the relevant parameter `PILOT-REQUIRED` or `UNRESOLVED`. Do not infer shelf
life from a similar compound without stating the extrapolation.
