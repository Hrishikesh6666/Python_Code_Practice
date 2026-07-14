## ----------------------- problem 1 ------------
print("hello world")
##------------------------ problem 2 -------------------

num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))

def add(num_1, num_2):
    return num_1 + num_2

def divide(num_1, num_2):
    if num_2 == 0:
        return "Error: Division by zero is not allowed."
    return num_1 / num_2

print(f"{num_1} + {num_2} = {add(num_1, num_2)}")
print(f"{num_1} / {num_2} = {divide(num_1, num_2)}")

## Write a Python program to find the area of a triangle

base = float(input("enter the base: "))
height = float(input("enter the hight: "))

def area_triangel(base,height):
    return 0.5 * base * height

len = float(input("enter the length: "))
breadth = float(input("enter the breadth: "))

def area_rectangel(len,breadth):
    return len * breadth

print(f"The area of the triangle is: {area_triangel(base,height)}")
print(f"The area of the triangle is: {area_rectangel(len,breadth)}")

## Write a Python program to swap two variables.

a = int(input("enter the a: "))
b = int(input("enter the b: "))

print(f"original num a :{a} and b:{b}")

temp = a
a = b
b = temp
print(f"swap num a :{a} and b:{b}")

## Write a Python program to swap two variables without temp variable.

a = 5
b = 10
# Swapping without a temporary variable
a, b = b, a
print("After swapping:")
print("a =", a)
print("b =", b)

## Write a Python program to generate a random number.
import random
print(f"random num : {random.randint(1,100)}")


## Write a Python program to convert Celsius to Fahrenheit.
kilometers = float(input("enter the Kilometers: "))
# Conversion factor: 1 kilometer = 0.621371 miles
conversion_factror = 0.621371

def miles(kilometers):
    return kilometers * conversion_factror

print(f"{kilometers} kilometers is equal to {miles(kilometers)} miles")

## Write a Python program to convert kilometers to miles
celsius = float(input("Enter the Celsius: "))
# Conversion formula: Fahrenheit = (Celsius * 9/5) + 32
def Fahrenheit(celsius):
    return (celsius * 9/5) + 32
print(f"{celsius} degrees Celsius is equal to {Fahrenheit(celsius)} degrees Fahrenheit")

## Write a Python program to display calendar.
import calendar

year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))

def show_calendar(year, month):
    return calendar.month(year, month)

print(show_calendar(year, month))

