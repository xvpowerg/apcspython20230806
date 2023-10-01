def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()

def matrixAdd(A,B):
    n = len(A)
    m = len(A[0])
    C = [[None]*m for r in range(n)]
    for i in range(n):
        for k in range(m):
            C[i][k] = A[i][k] + B[i][k]
    return C

matrixA = [[1,3,5], [7,9,11], [13,15,17]]
matrixB = [[9,8,7], [6,5,4], [3,2,1]]

C =  matrixAdd(matrixA,matrixB)
printMatrix(C)
