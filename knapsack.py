def knapsack_01_greedy(weights, values, capacity):
    n = len(values)
    value_per_weight = [(values[i]/weights[i], i) for i in range(n)]
    value_per_weight.sort(reverse=True)
    total_value = 0
    total_weight = 0
    selected = [0]*n
    for vpw, i in value_per_weight:
        if total_weight + weights[i] <= capacity:
            selected[i] = 1
            total_value += values[i]
            total_weight += weights[i]
    return total_value, selected

def fractional_knapsack(weights, values, capacity):
    n = len(values)
    value_per_weight = [(values[i]/weights[i], i) for i in range(n)]
    value_per_weight.sort(reverse=True)
    total_value = 0
    fractions = [0]*n
    for vpw, i in value_per_weight:
        if weights[i] <= capacity:
            fractions[i] = 1
            total_value += values[i]
            capacity -= weights[i]
        else:
            fractions[i] = capacity / weights[i]
            total_value += values[i] * fractions[i]
            break
    return total_value, fractions

if __name__ == "__main__":
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50
    print("0/1 Knapsack (Greedy):")
    value_01, selected_01 = knapsack_01_greedy(weights, values, capacity)
    print(f"Total value: {value_01}")
    print(f"Selected items: {selected_01}")

    print("\nFractional Knapsack:")
    value_frac, fractions = fractional_knapsack(weights, values, capacity)
    print(f"Total value: {value_frac}")
    print(f"Fractions taken: {fractions}")
