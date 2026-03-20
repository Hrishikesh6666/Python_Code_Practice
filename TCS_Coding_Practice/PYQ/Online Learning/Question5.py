
def rotate_matrix(matrix,N):
    for i in range(N):
        for j in range(N):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
            
    
    for i in range (N):
        matrix[i].reverse()
    return matrix

N = int(input("Enter size:"))
matrix =[]
for _ in range(N):
    row =list(map(int,input("Enter: ").split( )))
    matrix.append(row)

result = rotate_matrix(matrix,N)
print(*result)