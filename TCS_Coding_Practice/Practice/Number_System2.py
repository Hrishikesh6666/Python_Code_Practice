## print all prime factorial of the given number

def prime_fact(num):
    if num <=0:
        return False
    total = 1
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            total += i
            if i != num // i:
                total  += num //i
    return total == num
num = 60
print(prime_fact(num))

'''Check if a number is a Strong Number or not
Problem Statement: Given an integer Print “YES” if it is a strong number else print “NO”.
Note : 
When the sum of factorial of individual digits of a number is equal to the original number
the number is called a strong number. 
Strong number is also known as Krishnamurthi number/Peterson Number.'''
import math

def strong_num(n):
    if n <= 0:
        return "NO"
    temp = n
    total = 0
    
    while temp > 0:
        digit = temp % 10
        total += math.factorial(digit)
        temp //= 10
    
    if total == n:
        return "YES"
    else:
        return "NO"

# Test
print(strong_num(145))  # Output: YES
print(strong_num(123))  # Output: NO

## gretest commen deviser GCD

def gcd(a,b):
    while b != 0:
        a,b = b,a%b
    return a
print(gcd(12,18))

##  LCM of the number 

def gcd(a,b):
    while b != 0:
        a,b = b,a%b
    return a
def lcm(a,b):
    return (a*b) // gcd(a,b)

a,b = map(int,input("Enter num: ").split( ))
print(lcm(a,b))  

## Give a number keep adding digits until only one digit  remains:
'''ex = 529 = 5+2+9 = 16 ---> 1+6 = 7 output = 7 '''

def sum_of_digits(num):
    while num >=10:
        total = 0
        while num > 0:
            total += num % 10
            num //=10
        num = total
    return num
num = 529
print(sum_of_digits(num))


## Area of circle

r = int(input())

def area_circle(r):
    area = 3.14 *r*r
    print(round(area))

print(area_circle(r))