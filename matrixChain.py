# Matrix Chain Multiplication using Dynamic Programming

def matrix_chain_order(p):
    n = len(p) - 1  # Number of matrices
    m = [[0 for _ in range(n)] for _ in range(n)]
    s = [[0 for _ in range(n)] for _ in range(n)]

    for l in range(2, n + 1):  # l is chain length
        for i in range(n - l + 1):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return m, s

def print_optimal_parens(s, i, j):
    if i == j:
        print(f"A{i+1}", end="")
    else:
        print("(", end="")
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j] + 1, j)
        print(")", end="")

# Example usage
if __name__ == "__main__":
    p = [30, 35, 15, 5, 10, 20, 25]
    m, s = matrix_chain_order(p)
    n = len(p) - 1
    print(f"Minimum number of multiplications: {m[0][n-1]}")
    print("Optimal Parenthesization:", end=" ")
    print_optimal_parens(s, 0, n-1)
    print()
