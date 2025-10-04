def empaquetar(lista):
    resultado=[]
    contador = 1  # contamos repeticiones
    for i in range(1, len(lista)):
        if lista[i] == lista[i-1]:
            contador += 1
        else:
            resultado.append((lista[i-1], contador))
            contador = 1
    resultado.append((lista[-1], contador)) 
    return resultado

listaNum= ([1,1,1,1,1,2,2,2,3,3,8,8,8,8,8,5,4,4])
print(empaquetar(listaNum))
