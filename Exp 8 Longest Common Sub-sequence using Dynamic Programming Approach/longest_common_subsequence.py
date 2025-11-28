# Longest Common Subsequence


def lcs(str1, str2):
    """Find longest common subsequence length"""
    m = len(str1)
    n = len(str2)
    
    l = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                l[i][j] = l[i - 1][j - 1] + 1
            else:
                l[i][j] = max(l[i][j - 1], l[i - 1][j])
    
    return l[m][n]


def main():
    str1 = input("Enter word 1: ")
    str2 = input("Enter word 2: ")
    
    print(f"LCS: {lcs(str1, str2)}")


if __name__ == "__main__":
    main()
