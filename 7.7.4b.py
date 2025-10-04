def son_ortogonales(v1, v2):
    # calculamos el producto escalar
    producto = sum(a*b for a, b in zip(v1, v2))
    
    if producto == 0:
        return True
    else:
        return False

v1 = (2, 3)
v2 = (-3, 2)

print(son_ortogonales(v1, v2))