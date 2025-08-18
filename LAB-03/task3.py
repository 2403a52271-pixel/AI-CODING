# Program: Calculate power bill (slab-wise)
# Default slabs (units, rate per unit):
#  - First 50 units @ 0.50
#  - Next 100 units @ 0.75
#  - Next 100 units @ 1.20
#  - Remaining units @ 1.50

from typing import List, Tuple

Slab = Tuple[float, float]  # (units_in_slab, rate_per_unit); use float('inf') for unlimited

def calculate_power_bill(units: float, slabs: List[Slab]) -> Tuple[float, List[Tuple[float, float, float]]]:
    """
    Calculate total bill for the given units using provided slabs.
    Returns total and a breakdown list of (units_charged, rate, amount).
    """
    remaining = units
    total = 0.0
    breakdown: List[Tuple[float, float, float]] = []

    for slab_units, rate in slabs:
        if remaining <= 0:
            break
        if slab_units == float('inf'):
            used = remaining
        else:
            used = min(remaining, slab_units)
        amount = used * rate
        total += amount
        breakdown.append((used, rate, amount))
        remaining -= used

    return total, breakdown

if __name__ == "__main__":
    try:
        raw = input("Enter total units consumed: ").strip()
        units = float(raw)
        if units < 0:
            print("Units cannot be negative.")
        else:
            default_slabs: List[Slab] = [
                (50, 0.50),
                (100, 0.75),
                (100, 1.20),
                (float('inf'), 1.50),
            ]
            total, details = calculate_power_bill(units, default_slabs)
            print("Breakdown:")
            for used, rate, amount in details:
                if used > 0:
                    print(f"  {used:.0f} unit(s) @ {rate:.2f} = {amount:.2f}")
            print(f"Total bill: {total:.2f}")
    except ValueError:
        print("Invalid input. Please enter a numeric value for units.")
