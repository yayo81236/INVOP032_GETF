caras = 20

# Generar todas las combinaciones posibles de tres dados
combinaciones = [(d1, d2, d3) for d1 in range(1, caras + 1) 
                              for d2 in range(1, caras + 1) 
                              for d3 in range(1, caras + 1)]

# Guardar las combinaciones en un archivo de texto
with open("combinaciones_dados.txt", "w") as archivo:
    for combinacion in combinaciones:
        archivo.write(f"{combinacion}\n")

print("¡Combinaciones generadas y guardadas en 'combinaciones_dados.txt'!")