# Longest Common Subsequence (LCS) using Dynamic Programming

def lcs(X, Y):
    m = len(X)
    n = len(Y)
    # Create a DP table to store lengths of LCS
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Build the table in bottom-up fashion
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct the LCS string
    index = dp[m][n]
    lcs_str = [''] * index
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_str[index - 1] = X[i - 1]
            i -= 1
            j -= 1
            index -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return ''.join(lcs_str), dp[m][n]

# Example usage
if __name__ == "__main__":
    X = "AGGTAB"
    Y = "GXTXAYB"
    lcs_str, length = lcs(X, Y)
    print(f"LCS of {X} and {Y} is '{lcs_str}' with length {length}")
