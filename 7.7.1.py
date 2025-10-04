def menor_a_mayor(tupla):
    for i in range(len(tupla) - 1):
        if tupla[i] > tupla[i+1]:
            return False
    return True

print(f"Tupla (1, 5, 5, 9): {menor_a_mayor((1, 5, 5, 9))}")  # True
print(f"Tupla (8, 5, 12, 2): {menor_a_mayor((8, 5, 12, 2))}")  # False
