def numero_primo(lista):
    primos = []
    for n in lista:
        if n < 2:
            continue
        es_primo = True
        for i in range(2, n):
            if n % i == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(n)
    return primos

# Ejemplo
NumerosP = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print("Lista de numeros:", NumerosP)
print("Los números primos son:", numero_primo(NumerosP))