import math
def norma(v):
    (x, y) = v
    resultado = math.sqrt(x**2 + y**2)
    return resultado

# Ejemplo
print("la norma del vector es igual a: ", norma((3, 4)))  