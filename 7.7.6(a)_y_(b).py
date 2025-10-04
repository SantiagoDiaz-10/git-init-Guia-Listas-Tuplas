#EJERCICIO A
def numeros_k(lista, k):
    menores = []
    mayores = []
    iguales = []
    
    for n in lista:
        if n < k:
            menores.append(n)
        elif n > k:
            mayores.append(n)
        else:
            iguales.append(n)
    
    return menores, mayores, iguales

# Ejemplo
numeros = [3, 7, 2, 5, 7, 10, 5]
k = 5
menores, mayores, iguales = numeros_k(numeros, k)

print("Menores:", menores)
print("Mayores:", mayores)
print("Iguales:", iguales)

#EJERCICIO B
def multiplos_de_k(lista, k):
    multiplos = []
    for n in lista:
        if n % k == 0:  # si n es divisible por k
            multiplos.append(n)
    return multiplos

# Ejemplo
numeros = [3, 7, 2, 5, 10, 15, 20]
k = 5
print("Múltiplos de", k, ":", multiplos_de_k(numeros, k))