def maximize_chocolate_profit():
    max_profit = -1
    best_a = 0
    best_b = 0
    # Constraints:
    # a = units of A to produce, b = units of B to produce
    # Each A requires 1 Milk, 3 Choco
    # Each B requires 1 Milk, 2 Choco
    # Max Milk = 5, Max Choco = 12
    for a in range(0, 5 + 1):  # max 5 units can be made with milk constraint
        for b in range(0, 5 + 1):  # also cannot produce more than 5 on milk
            milk_used = a * 1 + b * 1
            choco_used = a * 3 + b * 2
            if milk_used <= 5 and choco_used <= 12:
                profit = a * 6 + b * 5
                if profit > max_profit:
                    max_profit = profit
                    best_a, best_b = a, b
    print(f"Maximum profit: Rs {max_profit}")
    print(f"Units of A to produce: {best_a}")
    print(f"Units of B to produce: {best_b}")

if __name__ == "__main__":
    maximize_chocolate_profit()
