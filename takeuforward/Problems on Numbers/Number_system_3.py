## Sum Of Digits of A Number

'''
Input: num = 529
Output:7
Explanation: In first iteration the digits sum will be = 5 + 2 + 9 => 16
In second iteration the digits sum will be 1 + 6 => 7.
Now single digit is remaining , so we return it. 

Input:num = 101
Output: 2
Explanation: In first iteration the digits sum will be = 1 + 0 + 1 => 2
Now single digit is remaining , so we return it. 
'''

def sum_of_digits(num):
    while num >= 10:
        sum = 0
        while num > 0:
            sum += num % 10
            num //= 10
        num = sum
    return num
num = int(input("Enter a number: "))
print("Sum of digits of", num, "is:", sum_of_digits(num))


## Find the sum of numbers in the given range
'''
Problem Statement: Find the sum of numbers in the given range.

Examples
Example 1:
Input:
 l = 2, r = 7  
Output:
 27  
Explanation:
  The sum of numbers from 2 to 7 is: 2 + 3 + 4 + 5 + 6 + 7 = 27.  
Therefore, the result is 27.

Example 2:
Input:
 l = 5, r = 9  
Output:
 35  
Explanation:
The sum of numbers from 5 to 9 is: 5 + 6 + 7 + 8 + 9 = 35.  
Therefore, the result is 35.'''

def sum_of_range(l, r):
    total_sum = 0
    
    for i in range(l, r + 1):
        total_sum += i
    return total_sum

l = int(input("Enter the lower bound of the range: "))
r = int(input("Enter the upper bound of the range: "))
print("Sum of numbers from", l, "to", r, "is:", sum_of_range(l, r)) 


## Program to Add two fractions
'''
Problem Statement: Given numerator and denominator of two fractional numbers, return the sum of two fractional numbers.

Examples
Input: Numerator1 = 3, Denominator1 = 4, Numerator2 = 1, Denominator2 = 7
Output: Numerator = 25, Denominator = 28 
Explanation: 3/4 + 1/7 = 25/28
Input: Numerator1 = 5, Denominator1 = 2, Numerator2 = 1, Denominator2 = 2
Output: Numerator = 3, Denominator = 1
Explanation: 5/2 + 1/2 = 6/2 = 3


'''

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n1 = int(input())
d1 = int(input())
n2 = int(input())
d2 = int(input())

numerator = n1 * d2 + n2 * d1
denominator = d1 * d2

g = gcd(numerator, denominator)

numerator //= g
denominator //= g

print("Numerator =", numerator)
print("Denominator =", denominator)


## Replace all the 0’s with 1 in a given integer
'''
Problem Statement: You are given an integer. Your task is to replace all the zeros in the integer with ones.

Examples
Input N = 102003 
Output 112113 
Explanation The 2nd, 4th, and 5th positions from the left contain 0. These 0s are replaced with 1s, resulting in 112113.

Input N = 204 
Output 214
Explanation The 2nd position from the left contains 0. That 0 is replaced with 1, giving 214.'''

num = int(input("Enter an integer: "))
result = str(num).replace('0', '1')
print("Result after replacing 0's with 1's:", result)

# ------------------- Alternative approach without converting to string ---------------------
def replace_zero(n):
    if n == 0:
        return 1

    result = 0
    place = 1

    while n > 0:
        digit = n % 10

        if digit == 0:
            digit = 1

        result += digit * place
        place *= 10
        n //= 10

    return result

n = int(input())
print(replace_zero(n)) 

## Calculate the area of the circle
r = int(input("Enter the redius: "))
def Area_circle(r):
    area = 3.14 * r * r
    print("Area of the circle: ", area)
Area_circle(r)