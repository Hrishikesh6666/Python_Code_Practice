'''Question 2: Problem Statement:
You are given a range of integers from M to N (inclusive), where:

M is the lower limit
N is the upper limit
Your task is to find all palindrome numbers in the range and return the count of such numbers.

Input Format:
Enter M : <lower limit integer> Enter N : <upper limit integer> 

Output Format:
<number of palindrome numbers> 

Definition:
A palindrome number is a number that reads the same backward as forward.
Example: 121, 131, 11, 9

Example Input:

Enter M : 10 Enter N : 20 

Example Output:
1 
Explanation:
Only one palindrome exists between 10 and 20 → 11'''
def is_palindrome(num):
    return str(num) == str(num)[::-1]

def palindrome_num(M, N):
    count = 0
    for i in range(M, N+1):  # include N
        if is_palindrome(i):
            count += 1
    return count

# Take integer inputs
M = int(input("Enter M: "))
N = int(input("Enter N: "))

print(palindrome_num(M, N))


def is_palindrome(num):
    original = num
    rev = 0
    while num > 0:
        rev = rev * 10 + (num % 10)
        num //= 10
        
    return original == rev
def palindrome_num(M, N):
    count = 0
    for i in range(M, N+1):  # include N
        if is_palindrome(i):
            count += 1
    return count
print(palindrome_num(M,N))

        