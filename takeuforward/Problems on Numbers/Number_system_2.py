## Calculate the Power of the number (Binary Exponentiation)

def power(a,b):
    result = 1
    while b > 0:
        if b % 2 == 1:
            result *= a
        a *= a
        b //= 2
    return result
# Input
a = int(input("Enter base: "))
b = int(input("Enter exponent: "))

# Output
print("Result:", power(a, b))

## Factors of a Given Number
'''
Problem Statement: Find all factors of a number or find all distinct divisors of a natural number.
Examples
Input: n = 6
Output: [1, 2, 3, 6]  
Explanation: 6 is divisible by 1,2,3,6.
Input: n = 9
Output: [1, 3, 9] 
Explanation: 9 is divisible by 1,3,9. '''

def factors(n):
    result =[]
    for i in range(1 ,n+1):
        if n % i == 0:
            result.append(i)
    return result
# Input
n = int(input("Enter a number: "))
# Output
print("Factors of", n, "are:", factors(n))

## ---------------- Another Approach ------------------

# Find factors of a number (Optimal)
import math

n = int(input("Enter a number: "))
factors = []

for i in range(1, int(math.sqrt(n)) + 1):
    if n % i == 0:
        factors.append(i)
        if i != n // i:   # avoid duplicate for perfect squares
            factors.append(n // i)

factors.sort()
print("Factors:", factors)

# -------------------------------- VIMP -----------------------
## Print all Prime Factors of the given number
'''
Problem Statement: Given an integer N, print all of its prime factors.
Examples
Input: N = 60
Output: 2, 3, 5  
Explanation: All factors/divisors of 60 include: 1, 2, 3, 4, 5, 6, 10, 12, 18, 20, 30, 60. Out of these only 2, 3 and 5 are prime.
Input: N = 35
Output: 5, 7
Explanation: All factors/divisors of 35 include: 1, 5, 7, 35. Out of these, only 5 and 7 are prime.'''

def print_prime_factors(n):
    factors = []

    # Check for factor 2
    if n % 2 == 0:
        factors.append(2)
        while n % 2 == 0:
            n //= 2

    # Check odd factors
    i = 3
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            while n % i == 0:
                n //= i
        i += 2

    # If remaining n is a prime number > 2
    if n > 2:
        factors.append(n)

    print(*factors, sep=", ")

# Input
n = int(input())
print_prime_factors(n)

## Find GCD of two numbers

'''
Problem Statement: Given two integers N1 and N2, find their greatest common divisor.
Examples
Example 1:
Input: N1 = 9, N2 = 12

Output: 3
Explanation:
Factors of 9: 1, 3, 9
Factors of 12: 1, 2, 3, 4, 6, 12
Common Factors: 1, 3
Greatest common factor: 3 (GCD)

Example 2:
Input: N1 = 20, N2 = 15

Output: 5
Explanation:
Factors of 20: 1, 2, 4, 5, 10, 20
Factors of 15: 1, 3, 5, 15
Common Factors: 1, 5
Greatest common factor: 5 (GCD)'''

def gcd(a,b):
    while b != 0:
        a, b = b , a%b
    return a
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
print("GCD of", n1, "and", n2, "is:", gcd(n1, n2))

## ------------------- Another Approach ------------------


def gcd(a,b):
    gcd = 1
    for i in range(1, min(a,b)+ 1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd
n1 = int(input("Enter first number: ")) 
n2 = int(input("Enter second number: "))
print("GCD of", n1, "and", n2, "is:", gcd(n1, n2))


## Find LCM of two numbers
'''
Problem Statement: Find the LCM of two numbers.

Examples
Example 1:
Input:
 num1 = 4,num2 = 8
Output:
 8

Example 2:
Input:
 num1 = 3,num2 = 6
Output:
 6
 '''
 
def gcd(a,b):
    while b != 0:
        a ,b = b ,a%b
    return a

def lcm(a,b):
    return (a * b) // gcd(a, b)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("LCM of", num1, "and", num2, "is:", lcm(num1, num2))


## Check if the given number is Harshad(Or Niven) Number
'''
Problem Statement: Check if the number is a Harshad(or Niven) number or not.

Examples
Example 1:
Input: 378
Output: Yes it is a Harshad number.
Explanation: 3+7+8=18. 378 is divisible by 18. Therefore 378 is a harshad number.

Example 2:
Input: 379
Output: No
 it is not a Harshad number.
Explanation: 3+7+9=19. 379 is not divisible by 19. Therefore 379 is a harshad number.'''

num = int(input("Enter a number: "))
s = str(num)
sum = 0

for char in s:
    sum += int(char)

if num % sum == 0:
    print("Yes, it is a Harshad number.")
else:
    print("No, it is not a Harshad number.")
    
## Check if the number is an abundant number or not
'''
Example 1:
Input: 18
Output: Abundant Number
Explanation: Divisors of 18 are 1,2,3,6,9. 1+2+3+6+9=21, Since 21 is greater than 18, 18 is an abundant number.

Example 2:
Input: 21
Output: Not Abundant Number
Explanation:Divisors of 21 are 1,3,7. 1+3+7=11, Since 11 is smaller than 21, 11 is not an abundant number.
'''

n = int(input("Enter a number: "))
def is_abundant(n):
    divisors_sum = 0
    for i in range(1,n):
        if n % i == 0:
            divisors_sum += i
    
    if divisors_sum > n:
        return "Abundant Number"
    else:
        return "Not Abundant Number"
    
print(is_abundant(n))


