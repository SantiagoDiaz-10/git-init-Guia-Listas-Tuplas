def triangular_superior(A):
    n = len(A)
    
    for i in range(n):
        for j in range(i+1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
                if A[j][k] == int(A[j][k]):
                    A[j][k] = int(A[j][k])
                else:
                    A[j][k] = round(A[j][k], 2)  
    return A
A = [[2, 1, -1],
     [-3, -1, 2],
     [-2, 1, 2]]

resultado = triangular_superior(A)
for fila in resultado:
    print(fila)
