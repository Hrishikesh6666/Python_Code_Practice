## 1. Check if a number is palindrome or not
def is_palindrome(n):
    if  n < 0:
        return False
    original = n
    reversed_num = 0
    
    while n > 0:
        reversed_num = reversed_num *10 + n % 10
        n //=10
        
    return original == reversed_num

n = int(input("Enter the number:"))

print(is_palindrome(n))

# ========== Another way using string =================

def is_palindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return "Not Palindrome"
print (is_palindrome(n))


## Find all Palindrome numbers in a given range.
def is_palindrome(n):
    if  n < 0:
        return False
    original = n
    reversed_num = 0
    
    while n > 0:
        reversed_num = reversed_num *10 + n % 10
        n //=10
        
    return original == reversed_num

def palindrome_num(start , end):
    result = []
    
    for num in range(start,end+1):
        if is_palindrome(num):
            result.append(num)
    return result

print (palindrome_num(10,100))


## Q.3 Check if a number is prime or not

def prime_num(n):
    if n <= 1:   # 0 and 1 are not prime
        return "Not Prime"
    if n == 2:   # 2 is the only even prime
        return "Prime number"
    for i in range(2, int(n**0.5) + 1):  # check up to sqrt(n)
        if n % i == 0:
            return "Not Prime"
    return "Prime number"

# Example usage
n = int(input("ENTER NUM : "))
print(prime_num(n))

## Check the array is sorted or not 

def sorted_arr(arr):
    n = len(arr)
    
    for i in range(1,n):
        if arr[i] < arr[i-1]:
            return False
        return True
    
## give the prime number in given range

def prime_number(L,R):
    
    for num in range(L,R+1):
        
        if num < 1:
            continue
        
        is_prime = True
        
        for i in range(2,num):
            if num % i==0:
                is_prime = False
                break
        if is_prime:
            print(num,end=",")
            
print(prime_number(1,50))
        
## 5. Check if a number is armstrong number or not  
'''
Definition:
A number is called an Armstrong Number if the sum of the cubes of its digits equals the number itself (for 3-digit numbers).
Example:

153
1+125+27=153
Since the result equals the original number → Armstrong Number'''

def armstrong(num):
    original = num
    total = 0
    
    while num > 0:
        digit = num % 10
        total += digit ** 3
        num //= 10
    
    if total == original:
        return "Armstrong Number"
    else:
        return "Not Armstrong Number"

num = int(input("Enter: "))
print(armstrong(num)) 


