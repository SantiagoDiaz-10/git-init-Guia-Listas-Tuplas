def sumar_matrices(A, B):
    resultado = []
    for i in range(len(A)):  # recorre filas
        fila_suma = []
        for j in range(len(A[0])):  # recorre columnas
            fila_suma.append(A[i][j] + B[i][j])
        resultado.append(fila_suma)
    return resultado

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

print(sumar_matrices(A, B))