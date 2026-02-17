# Stander method to find Fibonacci series
num = int(input("Enter the number of terms: "))
a, b = 0,1
print ("Fibonacci series: ", end="")
for i in range (2, num):
    c = a+b
    a=b
    b=c
    print (c, end=" ")
print()

# using recursion method to find Fibonacci series

def fib(n):
    if n == 0:
        return 0
    elif n ==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
n= 10
fib_series = [fib(i) for i in range(n)]
# fib_series = [fib(i)]
print(fib_series)
        
        
# Using Iteration (Loop)

def fib_iterative(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

fib_series_iterative = fib_iterative(10)
print("Fibonacci series (Iterative):", fib_series_iterative)
            
