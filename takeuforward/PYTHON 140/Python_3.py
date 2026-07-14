## Write a Python Program to Find the Sum of Natural Numbers

def Natural(num):
    sum = 0
    
    for i in range(0,num+1):
        sum +=i
        
    return sum

print(Natural(num=10))

## Write a Python Program to Find LCM.

def LCM(x,y):
    if x > y:
        greater = x
    else:
        greater = y
    while(True):
        if((greater % x ==0) and (greater % y ==0)):
            lcm = greater
            break
        greater += 1
    return lcm
num1 = int(input('Enter the number: '))
num2 = int(input('Enter the number: '))
print("The L.C.M. is",LCM(num1, num2))


def lcm_loop(x, y):
    greater = max(x, y)
    while True:
        if greater % x == 0 and greater % y == 0:
            return greater
        greater += 1

num1 = 12
num2 = 15
print("LCM (Loop):", lcm_loop(num1, num2))

## Write a Python Program to Find HCF.

def HCF(x ,y):
    if x > y :
        smaller = y
    else:
        smaller = x
    for i in range(1,smaller + 1):
        if((x % i ==0) and (y % i ==0)):
            hcf = i
    return hcf
num1 = int(input('Enter the number: '))
num2 = int(input('Enter the number: '))
print("The H.C.F. is", HCF(num1, num2))

## Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal.
# How can we manually convert a decimal number to binary, octal and hexadecimal?

Number = int(input("Enter the Number: "))

print(bin(Number)[2:])
print(oct(Number)[2:])
print(hex(Number)[2:].upper())

## Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations.

def add(n1,n2):
    return n1 +n2

def sub(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

'''Write a Python Program to calculate your Body Mass Index.
Body Mass Index (BMI) is a measure of body fat based on an individual's weight and
height. It is commonly used as a screening tool to categorize individuals into different weight
status categories, such as underweight, normal weight, overweight, and obesity.
The BMI is calculated using the following formula:
Alternatively, in the imperial system:
BMI provides a general indication of body fatness but does not directly measure body fat or
distribution. It is widely used in public health and clinical settings as a quick and simple tool
to assess potential health risks associated with weight. Different BMI ranges are associated
with different health categories, but it's important to note that BMI has limitations and does
not account for factors such as muscle mass or distribution of fat.
BMI =
Weight (kg)
Height (m'''

def BMI(hight,weight):
    return round((weight/hight**2),2)

h = float(input("Enter your height in meters: "))
w = float(input("Enter your weight in kg: "))
bmi = BMI(h, w)

print(bmi(h,w))
if bmi <= 18.5:
    print("You are underweight.")
elif 18.5 < bmi <= 24.9:
    print("Your weight is normal.")
elif 25 < bmi <= 29.29:
    print("You are overweight.")
else:
    print("You are obese.")
    
## Write a Python Program to calculate the natural logarithm of any number.

import math

number = float(input("Enter a number: "))

if number <= 0:
    print("enter the positive number only")
else:
    log_value = math.log(number)
    print(f"The natural logarithm of {number} is {log_value}")

## Write a Python Program for cube sum of first n natural numbers?

def cube_sum(n):
    if n < 1:
        return 0
    return sum(i**3 for i in range(1, n + 1))

n = int(input("Enter a positive integer: "))
if n < 1:
    print("Please enter a positive integer.")
else:
    result = cube_sum(n)
    print(f"The sum of cubes of the first {n} natural numbers is: {result}")
    
## Write a Python Program to find sum of array.

def sum_of_array(arr):
    sum = 0
    for num in arr:
        sum += num
    return sum
print(sum_of_array([1, 2, 3, 4, 5]))  # Example usage