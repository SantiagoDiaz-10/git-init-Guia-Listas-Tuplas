def linealmente_independientes_2d(vectores):
    # Solo para 2 vectores de 2D
    v1 = vectores[0]
    v2 = vectores[1]
    
    determinante = v1[0]*v2[1] - v1[1]*v2[0]
    
    if determinante != 0:
        return True
    else:
        return False
    
vectores1 = [[1, 0], [0, 1]]
print("¿El vector",vectores1, "es linealmente independiente?: ", linealmente_independientes_2d(vectores1)) 

vectores2 = [[1, 2], [2, 4]]
print("¿El vector",vectores2, "es linealmente independiente?: ", linealmente_independientes_2d(vectores2))  