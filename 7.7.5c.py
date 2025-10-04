def factorial(n):
    resultado = 1
    for i in range(1, n+1):
        resultado *= i
    return resultado

def lista_factoriales(lista):
    factoriales = []
    for n in lista:
        factoriales.append(factorial(n))
    return factoriales

# Ejemplo
numeros = [5, 3, 4]
print("Factoriales:", lista_factoriales(numeros))
