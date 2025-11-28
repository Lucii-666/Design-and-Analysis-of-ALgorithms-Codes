def fractional_knapsack(wt, val, n, capacity):
    """Fractional Knapsack using greedy approach"""
    ratio = []
    idx = []
    
    for i in range(n):
        ratio.append(val[i] / wt[i])
        idx.append(i)
    
    # Selection sort indices by descending ratio
    for i in range(n - 1):
        best = i
        for j in range(i + 1, n):
            if ratio[j] > ratio[best]:
                best = j
        ratio[i], ratio[best] = ratio[best], ratio[i]
        idx[i], idx[best] = idx[best], idx[i]
    
    remaining = capacity
    total_value = 0.0
    
    for i in range(n):
        if remaining <= 0:
            break
        id = idx[i]
        if wt[id] <= remaining:
            # Take whole item
            total_value += val[id]
            remaining -= wt[id]
        else:
            # Take fraction
            frac = remaining / wt[id]
            add = val[id] * frac
            total_value += add
            remaining = 0
            break
    
    return total_value


def main():
    wt = [2, 3, 1, 4, 3, 2]
    val = [10, 5, 3, 2, 8, 7]
    n = 6
    capacity = 7
    
    print(f"\nTotal value is {fractional_knapsack(wt, val, n, capacity)}")


if __name__ == "__main__":
    main()
