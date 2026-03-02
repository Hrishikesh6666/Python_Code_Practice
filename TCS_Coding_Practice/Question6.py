# Transpose of a matrix

def transpose(matrix):
    n = len(matrix)        # number of rows
    m = len(matrix[0])     # number of columns
    
    result = [[0] * n for _ in range(m)]
    
    for i in range(n):
        for j in range(m):
            result[j][i] = matrix[i][j]
    
    return result

# Example usage
matrix = [[1, 2, 3],
          [4, 5, 6],        
          [7, 8, 9]]
transposed_matrix = transpose(matrix)
print(transposed_matrix)  # Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]