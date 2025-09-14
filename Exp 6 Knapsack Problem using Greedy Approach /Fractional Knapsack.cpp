#include <iostream>
using namespace std;

double fractionalKnapsack(int wt[], int val[], int n, int capacity) 
{
    double ratio[100];
    int idx[100];
    for (int i = 0; i < n; ++i) {
        ratio[i] = (double)val[i] / wt[i];
        idx[i] = i;
    }

    // selection sort indices by descending ratio
    for (int i = 0; i < n - 1; ++i) {
        int best = i;
        for (int j = i+1; j < n; ++j) if (ratio[j] > ratio[best]) best = j;
        double rt = ratio[i]; 
        ratio[i] = ratio[best]; 
        ratio[best] = rt;
        int it = idx[i]; 
        idx[i] = idx[best]; 
        idx[best] = it;
    }

    int remaining = capacity;
    double totalValue = 0.0;
    for (int i = 0; i < n && remaining > 0; ++i) {
        int id = idx[i];
        if (wt[id] <= remaining) {
            // take whole
            totalValue += val[id];
            remaining -= wt[id];
        } else {
            // take fraction
            double frac = (double)remaining / wt[id];
            double add = val[id] * frac;
            totalValue += add;
            remaining = 0;
            break;
        }
    }

    return totalValue;
}

int main() 
{
    int wt[]  = {2, 3, 1, 4, 3, 2};
    int val[] = {10,5, 3, 2, 8, 7};
    int n = 6;
    int capacity = 7;

    cout << endl << "Total value is " << fractionalKnapsack(wt, val, n, capacity) << endl;
    return 0;
}
