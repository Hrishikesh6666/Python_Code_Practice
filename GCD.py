# 3. Write code of Greatest Common Divisor
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
def gcd(a,b):
    while b != 0:
        a,b = b , a%b
    return a
print(f"Greatest Common Divisor of{a} and {b} is: {gcd(a,b)}")


# usinf recursion method to find GCD
def gcd_recursive(a,b): 
    if b == 0: 
        return a 
    else: 
        return gcd_recursive(b, a % b)
print(f"Greatest Common Divisor of{a} and {b} is using recursion: {gcd_recursive(a,b)}")

# using in built function to find GCD
import math
print(f"Greatest Common Divisor of{a} and {b} is using in built function: {math.gcd(a,b)}")