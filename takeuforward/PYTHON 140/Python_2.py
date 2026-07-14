## Write a Python Program to Check if a Number is Positive, Negative or Zero

num = int(input("enter the number:"))

def positive_negative(num):
    if num < 0:
        print("negative number")
    elif num == 0:
        print("number is zero")
    else :
        print("Positive Number")
print(positive_negative(num))

## Write a Python Program to Check if a Number is Odd or Even.

def odd_even(num):
    if num % 2 == 0:
        print("Even Number")
    elif num % 2 != 0:
        print ("odd number")   
print(odd_even(num)) 

## Write a Python Program to Check Leap Year.

def is_leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    return False

year = int(input("Enter the Year: "))

if is_leap_year(year):
    print("Leap Year")
else:
    print("Not a Leap Year")

## Write a Python Program to Check Prime Number.

num = int(input("Enter the Number: "))
def prime(num):
    if num <= 1:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    
    return True

if prime(num):
    print ("Prime Num")
else:
    print("Not Prime Number") 
    
# in the given Range 

def prime(num):
    if num <= 1:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

Start = int(input("Enter the Start num: "))
end = int(input("Enter the end num: "))

for i in range(Start,end+1):
    if prime(i):
        print(i,end=" ")

## Write a Python Program to Find the Factorial of a Number.

num = int(input("Enter the number: "))
def factorial(num):
    fact = 1
    
    for i in range(1,num+1):
        fact *= i
    
    return fact

if num < 0:
    print("Factorial does not exist for negative numbers")
else:
    print("Factorial =", factorial(num))
    
#---------- using Recursion -------------

def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num -1)
print("Factorial =", factorial(num))

## Write a Python Program to Display the multiplication Table.
num = int(input("Table of: "))
print(f"table of {num}")

for i in range(1,11):
    print(f"{num} X {i} = {num*i}")
    
## Write a Python Program to Print the Fibonacci sequence.
num =15
def fibo(num):
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    return fibo(num - 1) + fibo(num - 2)
print(fibo(num), end=" ")
for i in range(num):
    print(fibo(i), end=" ")
    
#--------- Another Method --------
num = 15
a ,b = 0 ,1

for i in range(num):
    print(a,end=" ")
    
    a , b = b , a+b
    
## Write a Python Program to Check Armstrong Number?


num = int(input("Enter a Number: "))
temp = num
digits = len(str(num))
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** digits
    temp //= 10

if total == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
    
#---------------- in the given range -------

lower = int(input("Enter the lower limit of the interval: "))
upper = int(input("Enter the upper limit of the interval: "))
for num in range(lower, upper + 1): # Iterate through the numbers i
    order = len(str(num)) # Find the number of digits in 'num'
    temp_num = num
    sum = 0
    while temp_num > 0:
        digit = temp_num % 10
        sum += digit ** order
        temp_num //= 10
 # Check if 'num' is an Armstrong number
    if num == sum:
        print(num)
               
    