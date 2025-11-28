# Karatsuba Algorithm for Large Integer Multiplication using Divide and Conquer

def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y

    # Calculates the size of the numbers
    n = max(len(str(x)), len(str(y)))
    m = n // 2

    # Split x and y
    high1 = x // 10**m
    low1 = x % 10**m
    high2 = y // 10**m
    low2 = y % 10**m

    # 3 recursive calls
    z0 = karatsuba(low1, low2)
    z1 = karatsuba((low1 + high1), (low2 + high2))
    z2 = karatsuba(high1, high2)

    return (z2 * 10**(2*m)) + ((z1 - z2 - z0) * 10**m) + z0

# Example usage
if __name__ == "__main__":
    x = 12345678
    y = 87654321
    print(f"Multiplying {x} and {y} using Karatsuba Algorithm:")
    result = karatsuba(x, y)
    print(f"Result: {result}")
    print(f"Expected: {x * y}")
