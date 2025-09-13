# 0/1 Knapsack Problem using Dynamic Programming

def knapsack_01_dp(weights, values, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build table dp[][] in bottom up manner
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    # To find which items are included
    res = dp[n][capacity]
    w = capacity
    selected = [0] * n
    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == dp[i - 1][w]:
            continue
        else:
            selected[i - 1] = 1
            res -= values[i - 1]
            w -= weights[i - 1]

    return dp[n][capacity], selected

# Example usage
if __name__ == "__main__":
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50
    max_value, selected = knapsack_01_dp(weights, values, capacity)
    print(f"Maximum value: {max_value}")
    print(f"Selected items: {selected}")
