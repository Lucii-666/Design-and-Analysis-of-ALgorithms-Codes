MAXN = 10   # max number of items
MAXW = 50   # max capacity


def knapsack(n, W, wt, val):
    """0/1 Knapsack using dynamic programming"""
    dp = [[0] * (W + 1) for _ in range(MAXN + 1)]
    
    # Build table dp[][] bottom up
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif wt[i - 1] <= w:
                dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][W]


def main():
    n = 4
    W = 7
    wt = [1, 3, 4, 5] + [0] * (MAXN - 4)
    val = [1, 4, 5, 7] + [0] * (MAXN - 4)
    
    print("Items (value, weight):")
    for i in range(n):
        print(f"Item {i + 1}: value={val[i]} weight={wt[i]}")
    print(f"Knapsack capacity = {W}")
    
    max_value = knapsack(n, W, wt, val)
    print(f"\nMaximum value in knapsack = {max_value}")


if __name__ == "__main__":
    main()
