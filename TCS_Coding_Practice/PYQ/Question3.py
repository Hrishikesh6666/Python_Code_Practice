'''Q1. Find all numbers in range [L, R] 
Step 1: Understand the problem and constraints 
The task is to find all integers $x$ in the range $[L, R]$ that satisfy three conditions: 

Given a range [L, R], find all numbers x such that:
x % 7 == 0 → Divisible by 7
x % 5 != 0 → Not divisible by 5
x is NOT a palindrome. 

The example uses an input range of $L=10$ and $R=100$. 
Step 2: Identify numbers divisible by 7 in the range 
The numbers are: $14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98$. 
Step 3: Filter out numbers divisible by 5 
The numbers divisible by 5 in the list are $35, 70$. The remaining numbers are: $14, 21, 28, 42, 49, 56, 63, 77, 84, 91, 98$. 
Step 4: Filter out palindromes 
A palindrome reads the same forwards and backwards. In this range, the number $77$ is a palindrome. The remaining numbers are: $14, 21, 28, 42, 49, 56, 63, 84, 91, 98$. 
Answer: 
The numbers that satisfy all conditions for the given example range are: 14 21 28 42 49 56 63 84 91 98 

AI responses may include mistakes.'''


## Left rotate an array by d positions

def find_numbers(L,R):
    result =[]
    
    for x in range(L,R+1):
        if x%7 != 0:
            continue
        if x%5 == 0:
            continue
        if str(x) == str(x)[::-1]: # Check for palindrome
            continue
        result.append(x)
    return result

# Example usage
L = 10
R = 100
print("Numbers in range [L, R] that satisfy the conditions:", find_numbers(L,R))
            
def find_num(L,R):
    result=[]
    
    for x in range(L,R):
        if x%7 == 0 and x%5 !=0 and str(x) != str(x)[::-1]:
            result.append(x)
    return result
# Example usage
L = 10
R = 100
print("Numbers in range [L, R] that satisfy the conditions:", find_num(L,R))



'''
1️⃣ Problem Understanding
Restating the Problem
You are given:

N → number of students

M → number of subjects

A matrix of size N × M representing marks

You must:

Compute average marks for each student.
Count how many students have average strictly greater than 50.
Print that count.

Constraints

1 ≤ N ≤ 1000
1 ≤ M ≤ 20
0 ≤ Marks ≤ 100

Maximum total values processed = 1000 × 20 = 20,000 → small.

Input Format (Typical)
N M
marks_row_1
marks_row_2
...
marks_row_N
'''


def count_students():
    N, M = map(int, input().split())
    
    matrix = []
    for _ in range(N):
        row = list(map(int, input().split()))
        matrix.append(row)
    
    count = 0
    
    for row in matrix:
        total = sum(row)
        average = total / M
        
        if average > 50:
            count += 1
    
    print(count)
    
# ================Another approach====================
    
def count_students():
    N,M = map(int, input().split())
    matrix = []
    for _ in range(N):
        
        row = list(map(int,input().split()))
        avg = sum(row)/M
        if avg > 50:
            count += 1
    print(count)


    


