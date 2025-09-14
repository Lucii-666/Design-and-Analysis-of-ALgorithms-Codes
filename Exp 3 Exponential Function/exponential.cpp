#include <iostream>
using namespace std;

int exponential(int x, int n)
{
    if(n == 0) return 1;
    int res = x;
    for (int i = 1; i < n; i++) res *= x;
    return res;
}

int exponential_n_DC(int x, int n)
{
    if(n == 0) return 1;
    else return x * exponential_n_DC(x, n-1);
}

int exponential_logn_DC(int x, int n)
{
    if(n == 0) return 1;
    int half = n / 2;
    int left = exponential_n_DC(x, half);
    int right = exponential_n_DC(x, (n % 2 == 0 ? half : half + 1));
    return left * right;
}

int main()
{
    int base, exp, func;
    
    cout << "Enter the base: ";
    cin >> base;

    cout << "Enter the exponent: ";
    cin >> exp;

    cout << endl;
    cout << "1. Exponential Function using Iterative (Naive) Approach" << endl;
    cout << "2. Exponential Function with O(N) using Divide and Conquer Approach" << endl;
    cout << "3. Exponential Function with O(logN) using Divide and Conquer Approach" << endl;
    cout << "Choose the function you want to use (1, 2 or 3): ";
    cin >> func;

    cout << endl;
    switch (func)
    {
        case 1: 
            cout << "The exponential of " << base << " power " << exp 
            << " using Iterative Approach is " << exponential(base,exp) << endl;
            break;
        
        case 2: 
            cout << "The exponential of " << base << " power " << exp 
            << " using Divide and Conquer Approach with O(N) is " << exponential_n_DC(base,exp) << endl;
            break;

        case 3: 
            cout << "The exponential of " << base << " power " << exp 
            << " using Divide and Conquer Approach with O(logN) is " << exponential_logn_DC(base,exp) << endl;
            break;

        default: 
            cout << "Please enter a valid choice.";
            break;
    }

    return 0;
}