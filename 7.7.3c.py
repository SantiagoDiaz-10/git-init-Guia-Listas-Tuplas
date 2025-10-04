def votar(tupla_nombres): 
    tupla_nombres=tuple(tupla_nombres)
    
    for  nombre, genero in tupla_nombres: 
        if genero=='M' : 
            print("Estimado", nombre , ", vote por mi")
        else: 
            genero=='F'
            print("Estimada", nombre , ", vote por mi")


tupla1= (
    ('alvaro',  'M'), 
    ('santiago' , 'M'), 
    ('Maria' ,'F')
    ) 
    
    
print(votar(tupla1))