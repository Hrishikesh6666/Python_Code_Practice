## check the number is pailndrom or not
n= int(input("Enter : "))

def is_palindrome_brute(n):
    s = str(n)
    return s == s[::-1]
print (is_palindrome_brute(n))
#==========OR===========
n= int(input("Enter : "))
def is_palindrome(n):
    if n < 0:
        return False
    original = n
    rev = 0
    
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n //10
    return original == rev
print(is_palindrome(n))

## in the range

def is_palindrome(n):
    if n < 0:
        return False
    original = n
    rev = 0
    
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n //10
    return original == rev

def palindrome_inRange(low,high):
    result =[]
    
    for i in range(low,high+1):
        if is_palindrome(i):
            result.append(i)
    return result

low,high = map(int,input("Enter Low ,High: ").split( ))
result = palindrome_inRange(low,high)
print(result)

## check the number is prime nas not prime
n= int(input("Enter : "))

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n % i ==0:
            return False
    return True
print(is_prime(n))
## PRIME NUM in the range


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
    
n= int(input("Enter : "))
def is_Armstrong(n):
    digit = len(str(n))
    total = 0
    
    for d in str(n):
        total += int(d)** digit
    return total == n
print(is_Armstrong(n))
#=====================OR ================

def is_Armstrong(n):
    if n < 0:
        return False
    temp = n
    d = 0
    
    #count digits
    while temp > 0:
        d +=1
        temp //= 10
        
    # compute Armstrong
    temp = n
    total = 0
    while temp> 0:
        digit = temp % 10
        total += digit ** d
        temp //=10
    return total == n 
def find_Armstrong(low,high):
    result=[]
    for i in range(low,high+1):
        if is_Armstrong(i):
            result.append(i)
    return result

low,high = map(int,input("Enter low,high:").split( ))
print(find_Armstrong(low,high))

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
n= int(input("Enter : "))
def is_purferct(n):
    if n <= 0:
        return False
    total = 0
    
    for i in range(1,n):  
        if n % i == 0:
            total += i
    return total == n
print(is_purferct(n))

#==============OR==============

def is_perfect(n):
    if n <= 1:
        return False
    total = 1
    i =2
    while i*i <= n:
        if  n % i == 0:
            total += i
            if i != n//i:
                total += n //i
        i += 1
    return total == n
n =int(input())
print(is_purferct(n))

## Perfect number in the range

def perfect_num(n):
    if n <= 0:
        return 0
    total = 0
    
    for i in range(1,n):
        if n % i == 0:
            total += i
    return total == n

def PerfectNum_range(low,high):
    result = []
    for i in range(low,high+1):
        if perfect_num(i):
            result.append(i)
    return result

low,high = map(int,input("Enter low,high:").split( ))
print(PerfectNum_range(low,high))

## check the given number is even or odd
n= int(input("Enter : "))
def check_even_odd(n):
    if(n//2)*2 == n:
        return "Even"
    else:
        return "Odd"
print(check_even_odd(n))
    
#===========Bit-wise ===================

def check_bit_wise(n):
    if (n & 1) == 0 :
        return "Even"
    else:
        return "Odd"
print(check_bit_wise(n))

## check the number is positive or negative
n= int(input("Enter : "))
def positive_negative(n):
    if(n >>31) == 0:
        print(f"{n} is positive")
    else:
        print(f"{n} is negetive num")
        
print(positive_negative(n))

# sum of the first N natural number 
n = 14
def sum_NaturalNum(n):
    total = 0
    for i in range(1,n):
        total += i
    return total
print (sum_NaturalNum(n))

def sum_range(low,high):
    result = []
    total = 0
    for i in range(low,high+1):
        #result.append(i*(i+1)//2)
        total += i
        result.append(total)
    return result
low,high = map(int,input("Enter low,high:").split( ))
print(sum_range(low,high))

## find sum of AP series IMP 
n = 4
a = 2
d = 2
def sum_of_AP(n,a,d):
    sum = 0
    for i in range(1,n+1):
        sum += a
        a += d
    return sum
print(sum_of_AP(n,a,d))

##  check the leap Year in the years
def Leap_year(y):
    if  y %  400  == 0:
        return True
    if y % 100 == 0:
        return False
    if y % 4 == 0:
        return True
    else:
        return False
    
print(Leap_year(y=2004))

def leap_year(y):
    return(y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
def find_leapYear(low,high):
    result = []
    for y in range(low,high+1):
        if leap_year(y):
            result.append(y)
    return result
low,high = map(int,input("Enter low,high:").split( ))
print("Leap Years: ",find_leapYear(low,high))

## reverse the digit in the number 
n = 123456
def reverse_num(n):
    rev = 0
    while n > 0:  
        rev = rev * 10 + (n%10)
        n = n//10
    return rev
print(reverse_num(n))

## febonacchi number series 

def fib(n):
    if n == 0:
        return 0
    result =[]
    a,b = 0,1
    for _ in range(n):
        result.append(a)
        a , b = b , a+b
    return result
n = 9
print(fib(n))

# ========== USING RECURSION ==============

def fibonacchi(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacchi(n-1) + fibonacchi(n-2)
def fibonacci_brute(n):
    for i in range(n):
        if fibonacchi(i):
            print(fibonacchi(i),end=" ")
n = 9
print(fibonacci_brute(n))   

## factorial of the number 

def facto(x):
    if x == 0 or x == 1:   # base case
        return 1
    else:
        return x * facto(x - 1)

# Example usage
print(facto(9))   # 362880
   
def factorial(x):
    if x ==0 and x ==1:
        return 1
    result = 1
    for i in range(2,x+1):
        result *= i
    return result
print(factorial(9))   
