def producto_matrices(A, B):
    resultado = []
    for i in range(len(A)):  # recorre filas de A
        fila_producto = []
        for j in range(len(B[0])):  # recorre columnas de B
            suma = 0
            for k in range(len(A[0])):  # recorre elementos de la fila de A y columna de B
                suma += A[i][k] * B[k][j]
            fila_producto.append(suma)
        resultado.append(fila_producto)
    return resultado

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

print(producto_matrices(A, B))