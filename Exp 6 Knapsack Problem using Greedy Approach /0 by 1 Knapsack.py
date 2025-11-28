def knapsack(capacity, wt, val, n):
    """0/1 Knapsack using greedy approach (recursive)"""
    if n == 0 or capacity == 0:
        return 0
    
    if wt[n - 1] > capacity:
        return knapsack(capacity, wt, val, n - 1)
    
    include_item = val[n - 1] + knapsack(capacity - wt[n - 1], wt, val, n - 1)
    exclude_item = knapsack(capacity, wt, val, n - 1)
    
    if include_item > exclude_item:
        print(wt[n - 1], val[n - 1], n - 1)
    
    return max(include_item, exclude_item)


def main():
    wt = [2, 3, 1, 4, 3, 2]
    val = [10, 5, 3, 2, 8, 7]
    capacity = 7
    print(knapsack(capacity, wt, val, 6))


if __name__ == "__main__":
    main()
