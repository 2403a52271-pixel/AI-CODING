def f(x):
    # f(x) = 2x^3 + 4x + 5
    return 2 * x**3 + 4 * x + 5

def derivative_f(x):
    # f'(x) = derivative: 6x^2 + 4
    return 6 * x**2 + 4

def second_derivative_f(x):
    # f''(x) = 12x
    return 12 * x

# Find critical points: solve f'(x) = 0
# 6x^2 + 4 = 0 => x^2 = -2/3, no real solutions (since x^2 cannot be negative over reals)
# That means the function has no stationary points in real numbers.
# Let's check the behavior at infinity:
# For large x, 2x^3 dominates:
# - As x→+∞, f(x) → +∞
# - As x→-∞, f(x) → -∞

# Therefore, f(x) is strictly decreasing for x<0, and strictly increasing for x>0,
# but since leading term is x^3, there is no real minimum or maximum; it goes to -infinity as x→-infinity.

print("The function f(x) = 2x^3 + 4x + 5 does not have a minimum value for real x;")
print("It decreases without bound as x → -infinity (f(x) → -infinity).")
