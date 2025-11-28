MAXN = 10  # maximum number of matrices


def print_parens(s, i, j):
    """Print optimal parenthesization using split table s"""
    if i == j:
        print(f"A{i}", end="")
        return
    print("(", end="")
    print_parens(s, i, s[i][j])
    print_parens(s, s[i][j] + 1, j)
    print(")", end="")


def matrix_chain_order(p, n):
    """
    Matrix chain order: p has length n+1 (p[0..n])
    Returns minimal cost and fills s with split points
    """
    # m[i][j] will hold minimal cost for multiplying Ai..Aj (1-based indices)
    m = [[0] * (MAXN + 1) for _ in range(MAXN + 1)]
    s = [[0] * (MAXN + 1) for _ in range(MAXN + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                m[i][j] = 0
            else:
                m[i][j] = float('inf')  # INF
            s[i][j] = 0
    
    # L is chain length
    for L in range(2, n + 1):
        for i in range(1, n - L + 2):
            j = i + L - 1
            # Try all splits
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    
    return m[1][n], m, s


def main():
    n = int(input(f"Enter number of matrices (n, max {MAXN - 1}): "))
    if n <= 0 or n >= MAXN:
        print(f"Invalid n (1..{MAXN - 1})")
        return
    
    p = [0] * MAXN
    print(f"Enter {n + 1} dimensions p0..p{n} (space separated):")
    dimensions = list(map(int, input().split()))
    for i in range(n + 1):
        p[i] = dimensions[i]
    
    min_cost, m, s = matrix_chain_order(p, n)
    
    print(f"\nMinimum number of scalar multiplications = {min_cost}")
    print("Optimal parenthesization: ", end="")
    print_parens(s, 1, n)
    print()


if __name__ == "__main__":
    main()
