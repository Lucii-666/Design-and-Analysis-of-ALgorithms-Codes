#include <iostream>
#include <math.h>
using namespace std;


// Function to find min and max
int karatsuba(int num1, int num2)
{
    if (num1 < 10 && num2 < 10) return num1 * num2;
    
    int m = max(to_string(num1).size(), to_string(num2).size());
    
    long long m2 = m / 2;
    long long power = pow(10,m2);

    long long a = num1 / power;
    long long b = num1 % power;
    long long c = num2 / power;
    long long d = num2 % power;

    long long ac = karatsuba(a,c);
    long long bd = karatsuba(b,d);
    long long ad_bc = karatsuba(a+b,c+d) - ac - bd;

    return (ac * pow(10,m) + ad_bc * pow(10,m2) + bd);
}



int main(){
    // Creating the array
    int num1, num2;
    cout << "Enter first number: ";
    cin >> num1;
    cout << "Enter second number: ";
    cin >> num2;

    // Perfom karatsuba multiplication
    cout << "Product of first and second number using Karatsuba method: " << karatsuba(num1, num2) << endl;

    return 0;
}