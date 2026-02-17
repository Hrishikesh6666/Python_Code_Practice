""" 
A perfect number is a positive integer that is equal to the sum of its proper divisors, excluding the number itself. 
Example: Is 28 a perfect number?
The divisors of 28 are 1, 2, 4, 7, 14.
Sum of divisors: 1 + 2 + 4 + 7 + 14 = 28, so 28 is a perfect number.

"""

n = int(input("Enter a number: "))
sump= 0
for i in range(1, n):
    if(n % i == 0):
        sump= sump + i
if (sump == n):
    print("The number is a Perfect number")
else:
    print("The number is not a Perfect number")