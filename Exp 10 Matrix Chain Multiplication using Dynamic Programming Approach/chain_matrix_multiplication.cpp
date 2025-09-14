#include <iostream>
using namespace std;

const int MAXN = 10; // maximum number of matrices

// print optimal parenthesization using split table s
void printParens(int s[][MAXN], int i, int j) {
    if (i == j) {
        cout << "A" << i;
        return;
    }
    cout << "(";
    printParens(s, i, s[i][j]);
    printParens(s, s[i][j] + 1, j);
    cout << ")";
}

// matrix chain order: p has length n+1 (p[0..n])
// returns minimal cost and fills s with split points
long long matrixChainOrder(int p[], int n, long long m[][MAXN], int s[][MAXN]) {
    // m[i][j] will hold minimal cost for multiplying Ai..Aj (1-based indices)
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= n; ++j) {
            if (i == j) m[i][j] = 0;
            else m[i][j] = (long long)1e18; // INF
            s[i][j] = 0;
        }
    }

    // L is chain length
    for (int L = 2; L <= n; ++L) {
        for (int i = 1; i <= n - L + 1; ++i) {
            int j = i + L - 1;
            // try all splits
            for (int k = i; k <= j - 1; ++k) {
                long long q = m[i][k] + m[k + 1][j] + (long long)p[i - 1] * p[k] * p[j];
                if (q < m[i][j]) {
                    m[i][j] = q;
                    s[i][j] = k;
                }
            }
        }
    }

    return m[1][n];
}

int main() {
    int n;
    cout << "Enter number of matrices (n, max " << MAXN-1 << "): ";
    cin >> n;
    if (n <= 0 || n >= MAXN) {
        cout << "Invalid n (1.." << (MAXN-1) << ")\n";
        return 0;
    }

    int p[MAXN];
    cout << "Enter " << (n + 1) << " dimensions p0..p" << n << " (space separated):\n";
    for (int i = 0; i <= n; ++i) cin >> p[i];

    long long m[MAXN][MAXN];
    int s[MAXN][MAXN];

    long long minCost = matrixChainOrder(p, n, m, s);

    cout << "\nMinimum number of scalar multiplications = " << minCost << "\n";
    cout << "Optimal parenthesization: ";
    printParens(s, 1, n);
    cout << "\n";

    return 0;
}
