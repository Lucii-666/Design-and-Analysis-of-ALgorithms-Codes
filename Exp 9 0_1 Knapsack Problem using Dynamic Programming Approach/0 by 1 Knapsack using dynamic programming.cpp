#include <iostream>
using namespace std;

const int MAXN = 10;   // max number of items
const int MAXW = 50;   // max capacity

int knapsack(int n, int W, int wt[], int val[]) {
	int dp[MAXN + 1][MAXW + 1];

	// Build table dp[][] bottom up
	for (int i = 0; i <= n; i++) {
			for (int w = 0; w <= W; w++) {
					if (i == 0 || w == 0)
							dp[i][w] = 0;
					else if (wt[i - 1] <= w)
							dp[i][w] = (val[i - 1] + dp[i - 1][w - wt[i - 1]] > dp[i - 1][w])
									? (val[i - 1] + dp[i - 1][w - wt[i - 1]])
									: dp[i - 1][w];
					else
							dp[i][w] = dp[i - 1][w];
			}
	}

	return dp[n][W];
}

int main() {
	int n = 4;
	int W = 7;
	int wt[MAXN] = {1, 3, 4, 5};
	int val[MAXN] = {1, 4, 5, 7};

	cout << "Items (value, weight):\n";
	for (int i = 0; i < n; i++) {
			cout << "Item " << (i + 1) << ": value=" << val[i]
			<< " weight=" << wt[i] << "\n";
	}
	cout << "Knapsack capacity = " << W << "\n";

	int maxValue = knapsack(n, W, wt, val);
	cout << "\nMaximum value in knapsack = " << maxValue << "\n";

	return 0;
}
