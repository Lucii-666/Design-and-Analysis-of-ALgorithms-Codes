def exponential(x, n):
    """Exponential function using iterative (naive) approach"""
    if n == 0:
        return 1
    res = x
    for i in range(1, n):
        res *= x
    return res


def exponential_n_DC(x, n):
    """Exponential function with O(N) using Divide and Conquer approach"""
    if n == 0:
        return 1
    else:
        return x * exponential_n_DC(x, n - 1)


def exponential_logn_DC(x, n):
    """Exponential function with O(logN) using Divide and Conquer approach"""
    if n == 0:
        return 1
    half = n // 2
    left = exponential_n_DC(x, half)
    right = exponential_n_DC(x, half if n % 2 == 0 else half + 1)
    return left * right


def main():
    base = int(input("Enter the base: "))
    exp = int(input("Enter the exponent: "))
    
    print()
    print("1. Exponential Function using Iterative (Naive) Approach")
    print("2. Exponential Function with O(N) using Divide and Conquer Approach")
    print("3. Exponential Function with O(logN) using Divide and Conquer Approach")
    func = int(input("Choose the function you want to use (1, 2 or 3): "))
    
    print()
    if func == 1:
        print(f"The exponential of {base} power {exp} using Iterative Approach is {exponential(base, exp)}")
    elif func == 2:
        print(f"The exponential of {base} power {exp} using Divide and Conquer Approach with O(N) is {exponential_n_DC(base, exp)}")
    elif func == 3:
        print(f"The exponential of {base} power {exp} using Divide and Conquer Approach with O(logN) is {exponential_logn_DC(base, exp)}")
    else:
        print("Please enter a valid choice.")


if __name__ == "__main__":
    main()
