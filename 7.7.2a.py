def encajar_ficha(ficha1, ficha2):

    if( ficha1 [0] == ficha2[0]or
        ficha1 [0] == ficha2[1]or
        ficha1 [1] == ficha2[0]or
        ficha1 [1] == ficha2[1]):
        return "las fichas encajan"
    else:
        return "las fichas no encajan"
    
ficha1="3,4"
ficha2="4,5"

print(encajar_ficha(ficha1, ficha2))
print(encajar_ficha((2,4), (5,10)))
print(encajar_ficha([5,9], [0,9]))
