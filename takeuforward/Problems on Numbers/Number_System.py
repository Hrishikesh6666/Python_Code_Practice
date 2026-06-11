# Check the numer is palindrome or not

n= int(input("Enter a number: "))
def is_palindrome_brute(num):
    s = str(num)
    return s == s[::-1]  
print(is_palindrome_brute(n))

def is_palindrome(num):
    if n < 0:
        return False
    original = n
    reversed_num = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10
    return original == reversed_num
# print(is_palindrome(n))

## in the range
def palindrome_in_range(start,end):
    result = []
    for num in range(start,end +1):
        if is_palindrome(num):
            result.append(num)
    return result
low,high = map(int, input("Enter the range (low high): ").split())
print(palindrome_in_range(low,high))

## Check if the number is prime or not
def is_prime(n):
    if n<2:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n % i == 0:
            return False
    return True

def prime_in_Range(low,high):
    result =[]
    for i in range(low,high+1):
        if is_prime(i):
            result.append(i)
    return result
low,high = map(int,input("Enter low,high:").split( ))
print(prime_in_Range(low,high))

## Check if number id ARMSTRONG Num
'''
Check if a number is Armstrong Number or not
Problem Statement:Given an integer N, return true it is an Armstrong number otherwise 
return false.
An Amrstrong number is a number that is equal to the sum of its own digits each raised 
to the power of the number of digits.
Example 1:
Input:N = 153
Output:True
Explanation: 1^3+5^3+3^3 = 1 + 125 + 27 = 153                                      
Example 2:
Input:N = 371                
Output: True
Explanation: 3^3+7^3+1^3 = 27 + 343 + 1 = 371'''
n = int(input("Enter a number: "))
def is_armstrong(n):
    s = str(n)
    power = len(s)
    total = 0
    
    for digit in s:
        total += int(digit)**power
    return total == n

print(is_armstrong(n))


## Check the number is perfect Number

'''Check whether a number is Perfect Number or not
Problem Statement: Write a program to find whether a number is a perfect number or not.
A perfect number is defined as a number that is the sum of its proper divisors ( all its positive divisors 
excluding itself).

Example 1:
Input: n=6
Output: 6 is a perfect number

Example 2:
Input: n=15
Output: 15 is not a perfect number'''

def is_perfect(n):
    if n < 0:
        return False
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total == n

def perfect_in_range(low,high):
    result =[]
    for i in range(low,high+1):
        if is_perfect(i):
            result.append(i)
    return result
low,high = map(int,input("Enter low,high:").split( ))
print(perfect_in_range(low,high))


## Even or Odd
n = int(input("Enter a number: "))
def is_evenORodd(n):
    if n%2 == 0:
        return "Even"
    else:
        return "Odd"
print(is_evenORodd(n))

##===========Bit-wise ===================

def check_bit_wise(n):
    if (n & 1) == 0 :
        return "Even"
    else:
        return "Odd"
print(check_bit_wise(n))

## Check the number is positive or negative
n = int(input("Enter a number: "))
def check_positive_negative(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"
print(check_positive_negative(n))

# --------check the number is positive or negative -----
def check_positive_negative_bitwise(n):
    if n == 0:
        print(f"{n} is Zero")
    elif (n >> 31) == 0:
        print(f"{n} is Positive")
    else:
        print(f"{n} is Negative")
check_positive_negative_bitwise(n)

## Sum of the N natural numbers
n = int(input("Enter a number: "))
def sum_of_natural(n):
    total = 0
    for i in range(1,n+1):
        total += i
    return total
print(sum_of_natural(n))

def sum_range(low,high):
    total = 0
    for i in range(low,high+1):
        total += i
    return total
low,high = map(int,input("Enter low,high:").split( ))
print(sum_range(low,high))

## leap year or not
n = int(input("Enter a year: "))
def is_leap_year(y):
    if y % 400 == 0:
        return True
    if y % 100 == 0:
        return False
    if y % 4 == 0:
        return True
    return False
#print(is_leap_year(n))

def leap_year_in_range(low,high):
    result = []
    
    for y in range(low,high+ 1):
        if is_leap_year(y):
            result.append(y)
    return result
low,high = map(int,input("Enter low,high:").split( ))
print(leap_year_in_range(low,high))

## reverse the number 

n = 123456

def reverse_num(n):
    rev = 0
    while n >0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    return rev
print(reverse_num(n))

## Fibbonacci series
n = int(input("Enter a number: "))
def fibonacci(n):
    result = []
    a ,b =0,1
    for i in range(n):
        result.append(a)
        a,b = b, a+b
    return result
print(fibonacci(n))

#------------Using Recursion-----------------
n=  9
def fibonacchi_recursive(n):
    if n <=0:
        return 0
    if n == 1:
        return 1
    return fibonacchi_recursive(n-1) + fibonacchi_recursive(n-2)    
print(fibonacchi_recursive(n))

## FACTORIAL OF A NUMBER
n = int(input("Enter a number: "))
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(n))

