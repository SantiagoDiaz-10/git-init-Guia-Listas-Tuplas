def producto_escalar(v1,v2):
    if len(v1) != len(v2):
        return "Error"
    
    Resultado=0 
    for i in range(len(v1)):
        Resultado += v1[i] * v2[i]
    return Resultado

vect1=[5,6]
vect2=[2,3]
print("El producto escalar es: ", producto_escalar(vect1,vect2) )
