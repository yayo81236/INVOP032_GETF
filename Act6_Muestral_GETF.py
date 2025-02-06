import itertools
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from collections import defaultdict
from fractions import Fraction

# Definir el número de caras de los dados
caras = 20

# Generar todas las combinaciones posibles de tres dados
combinaciones = list(itertools.product(range(1, caras + 1), repeat=3))

# Calcular la suma de cada combinación
sumas = [sum(combinacion) for combinacion in combinaciones]

# Contar la frecuencia de cada suma
frecuencia = defaultdict(int)
for suma in sumas:
    frecuencia[suma] += 1

# Convertir el diccionario de frecuencias a una lista de tuplas (suma, frecuencia)
frecuencia_lista = sorted(frecuencia.items())

# Extraer las sumas y las frecuencias
sumas_x, frecuencias_y = zip(*frecuencia_lista)

# Calcular las probabilidades como fracciones
probabilidades_fracciones = [Fraction(frec, len(combinaciones)) for frec in frecuencias_y]

# Convertir las fracciones a decimales para graficar
probabilidades_decimales = [float(prob) for prob in probabilidades_fracciones]

# Crear la gráfica
plt.figure(figsize=(12, 6))
barras = plt.bar(sumas_x, probabilidades_decimales, color='purple')

# Configurar el eje Y para mostrar porcentajes
ax = plt.gca()
ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))

# Añadir etiquetas a cada barra evitando el amontonamiento
for barra, prob in zip(barras, probabilidades_decimales):
    altura = barra.get_height()
    # Colocar el texto ligeramente por encima de la barra
    plt.text(barra.get_x() + barra.get_width() / 2, altura + 0.001, f'{prob * 100:.2f}%', 
             ha='center', va='bottom', fontsize=8)

# Añadir etiquetas y título
plt.xlabel('Suma de los dados (X)')
plt.ylabel('Probabilidad (%)')
plt.title('Distribución de Probabilidades de la Suma de Tres Dados de 20 Caras')
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Imprimir en la consola: Suma, Frecuencia, Probabilidad (Fracción), Probabilidad (Porcentaje)
print("Suma (X)\tFrecuencia\tProbabilidad (Fracción)\tProbabilidad (Porcentaje)")
for suma, frec, prob_frac in zip(sumas_x, frecuencias_y, probabilidades_fracciones):
    prob_porcentaje = float(prob_frac) * 100  # Convertir a porcentaje
    print(f"{suma}\t\t{frec}\t\t{prob_frac}\t\t{prob_porcentaje:.6f}%")
