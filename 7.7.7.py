def lista_nombre(lista_tuplas):
    Resultado=[]
    for persona in lista_tuplas: 
        apellido= persona[0]
        Nombre= persona[1]
        Inicial=persona[2]
        cadena= Nombre + " " + Inicial + ". " + apellido
        Resultado.append(cadena)
    return Resultado

Personas= [("Diaz", "Santiago" , "B"), ("Ruiz","Mario","F"), ("Martinez", "Carlos", "M")]
print(lista_nombre(Personas))
