# Problema 2 : Análisis de temperaturas con NumPy

import numpy as np
import matplotlib.pyplot as plt

temperaturas_diarias = np.array([
    22.5, 21.3, 23.1, 25.0, 24.5, 22.1,
    23.7, 24.8, 25.3, 26.1, 23.4, 24.0,
    22.9, 21.5, 23.0, 24.3, 25.0, 24.7,
    23.1, 22.4, 23.5, 24.1, 25.4, 26.0,
    24.8, 23.9, 22.7, 23.3, 24.5, 25.1
])

# Temperatura media
temperatura_media = np.mean(temperaturas_diarias)
print(f"Temperatura media: {temperatura_media:.2f} °C")

# Temperatura máxima y mínima
temperatura_maxima = np.max(temperaturas_diarias)
temperatura_minima = np.min(temperaturas_diarias)

print("Temperatura máxima:", temperatura_maxima)
print("Temperatura mínima:", temperatura_minima)

# Gráfico de temperaturas
dias = np.arange(1, 31)

plt.plot(dias, temperaturas_diarias, marker='o')
plt.xlabel('Día')
plt.ylabel('Temperatura (°C)')
plt.title('Temperaturas Diarias del Último Mes')
plt.grid(True)
plt.show()