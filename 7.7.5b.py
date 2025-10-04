def suma_y_porcentaje(lista):
    total = sum(lista)
    print("Sumatoria total:", total)
    
    for n in lista:
        print(n, ":", n * 100 / total, "%") 

# Ejemplo
numeros = [10, 20, 30, 40]
suma_y_porcentaje(numeros)
