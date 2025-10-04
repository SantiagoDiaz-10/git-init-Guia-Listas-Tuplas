def encajan(cadena):
    
    ficha1, ficha2 = cadena.split()
   
    a, b = ficha1.split('-')
    c, d = ficha2.split('-')

    if a == c or a == d or b == c or b == d:
        return True
    else:
        return False
    
print("3-4 2-5 →", encajan("3-4 2-5"))  
print("3-4 4-6 →", encajan("3-4 4-6"))  
print("6-6 1-6 →", encajan("6-6 1-6"))  
print("2-3 5-2 →", encajan("2-3 5-2")) 