#include <iostream>
using namespace std;

int knapsnak(int capacity, int wt[], int val[], int n)
{
    if (n == 0 || capacity == 0) return 0;

    if (wt[n - 1] > capacity) return knapsnak(capacity, wt, val, n - 1);
    
    int include_item = val[n - 1] + knapsnak(capacity - wt[n - 1], wt, val, n - 1);
    int exclude_item = knapsnak(capacity, wt, val, n - 1);
    
    if (include_item > exclude_item) cout << wt[n - 1] << " " << val[n - 1] << " " << n - 1 << endl;
    
    return max(include_item, exclude_item);
}

int main()
{
    int wt[] = {2, 3, 1, 4, 3, 2};
    int val[] = {10, 5, 3, 2, 8, 7};
    int capacity = 7;
    cout << knapsnak(capacity, wt, val, 6);
    return 0;
}