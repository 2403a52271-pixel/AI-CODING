# develop a python program which calculates power bill and it asks whether it is commercial , residential or industrial then it prints the cost

from typing import List, Tuple, Dict

Slab = Tuple[float, float]  # (units_in_slab, rate_per_unit); float('inf') for unlimited


def calculate_power_bill(units: float, slabs: List[Slab], fixed_charge: float = 0.0):
    """Return (total, breakdown) where breakdown is a list of (units_used, rate, amount).
    Adds optional fixed_charge to the total.
    """
    remaining = units
    total = 0.0
    breakdown: List[Tuple[float, float, float]] = []

    for slab_units, rate in slabs:
        if remaining <= 0:
            break
        used = remaining if slab_units == float('inf') else min(remaining, slab_units)
        amount = used * rate
        total += amount
        breakdown.append((used, rate, amount))
        remaining -= used

    total += fixed_charge
    return total, breakdown


if __name__ == "__main__":
    # Define category-wise slabs and optional fixed charges
    categories: Dict[str, Dict[str, object]] = {
        "residential": {
            "slabs": [(50, 0.50), (100, 0.75), (100, 1.20), (float('inf'), 1.50)],
            "fixed": 0.0,
        },
        "commercial": {
            "slabs": [(100, 0.95), (200, 1.30), (float('inf'), 1.75)],
            "fixed": 100.0,
        },
        "industrial": {
            "slabs": [(200, 1.10), (300, 1.50), (float('inf'), 2.00)],
            "fixed": 250.0,
        },
    }

    raw_cat = input("Enter category (residential/commercial/industrial): ").strip().lower()

    # Normalize short forms
    aliases = {
        "r": "residential",
        "res": "residential",
        "c": "commercial",
        "com": "commercial",
        "i": "industrial",
        "ind": "industrial",
    }
    category = aliases.get(raw_cat, raw_cat)

    if category not in categories:
        print("Invalid category. Choose from: residential, commercial, industrial")
    else:
        try:
            units = float(input("Enter total units consumed: ").strip())
        except ValueError:
            print("Invalid input. Please enter a numeric value for units.")
        else:
            if units < 0:
                print("Units cannot be negative.")
            else:
                slabs = categories[category]["slabs"]  # type: ignore[index]
                fixed = categories[category]["fixed"]  # type: ignore[index]
                total, details = calculate_power_bill(units, slabs, fixed_charge=fixed)  # type: ignore[arg-type]

                print(f"Category: {category.capitalize()}")
                print("Breakdown:")
                for used, rate, amount in details:
                    if used > 0:
                        print(f"  {used:.0f} unit(s) @ {rate:.2f} = {amount:.2f}")
                if fixed and fixed > 0:
                    print(f"  Fixed charge = {fixed:.2f}")
                print(f"Total bill: {total:.2f}")


