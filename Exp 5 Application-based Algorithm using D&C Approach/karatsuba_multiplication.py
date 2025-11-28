def karatsuba(num1, num2):
    """Function to perform Karatsuba multiplication"""
    if num1 < 10 and num2 < 10:
        return num1 * num2
    
    m = max(len(str(num1)), len(str(num2)))
    
    m2 = m // 2
    power = 10 ** m2
    
    a = num1 // power
    b = num1 % power
    c = num2 // power
    d = num2 % power
    
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba(a + b, c + d) - ac - bd
    
    return int(ac * (10 ** m) + ad_bc * (10 ** m2) + bd)


def main():
    # Creating the array
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    # Perform karatsuba multiplication
    print(f"Product of first and second number using Karatsuba method: {karatsuba(num1, num2)}")


if __name__ == "__main__":
    main()
