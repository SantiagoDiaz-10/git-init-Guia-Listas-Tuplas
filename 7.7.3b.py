def campaña_n(nombres, posicion, cantidad):
# Verificar que la posición sea válida
    if posicion < 0 or posicion >= len(nombres):
        print("Error: Posición inválida")
        return
    
    # Calcular el final
    fin = min(posicion + cantidad, len(nombres))
    
    # Imprimir mensajes para el rango seleccionado
    for i in range(posicion, fin):
        print(f"Estimado {nombres[i]}, vote por mí.")

nombres = ("Pablo", "Messi", "Oscar", "Matias", "Lionel")
campaña_n(nombres, 1, 3)  # Desde Messi, 3 personas
