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
    
# Example usage
print("Enter N and M:")
count_students()