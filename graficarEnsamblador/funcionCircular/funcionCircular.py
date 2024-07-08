import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter

# Magnitudes para tener un video a 1080p en pulgadas
Ancho = 10
Largo = 5.625

Figura = plt.figure(figsize=(Ancho, Largo))
Grafico, = plt.plot([], [], 'k-') # Cambiar el color del palo a negro
Estela, = plt.plot([], [], 'k--', alpha=0.3)  # Línea de estela con transparencia y color negro

Segundos = 14 # Valor arbitrario de segundos que necesito la animación
Frames = 60 # Cantidad de frames por segundo

plt.xlim(-1, 1)
plt.ylim(-1, 1)

axis = plt.gca() # Obtener el eje de las abscisas (X)

# Quitar todos los spines del gráfico
axis.spines['top'].set_visible(False)
axis.spines['right'].set_visible(False)
axis.spines['bottom'].set_visible(False)
axis.spines['left'].set_visible(False)

# Asegurar que los ejes X y Y tengan la misma escala
axis.set_aspect('equal')

# Ocultar los ticks del eje x y y
axis.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)

writer = FFMpegWriter(fps = Frames)

def actualizar_grafico(angulo, tiempo, x_hist, y_hist):
    # Convertir el ángulo a radianes
    radianes = np.deg2rad(angulo)
    # Calcular la longitud de la línea en función del tiempo
    longitud = 1.0  # Longitud fija para el contorno de la circunferencia
    # Calcular las coordenadas de la línea en función del ángulo y la longitud
    x = [0, longitud * np.cos(radianes)]
    y = [0, longitud * np.sin(radianes)]
    Grafico.set_data(x, y)
    
    # Guardar las coordenadas actuales en el historial
    x_hist.append(x[1])  # Solo guardamos la coordenada x del punto final
    y_hist.append(y[1])  # Solo guardamos la coordenada y del punto final
    
    # Actualizar la estela con las coordenadas anteriores
    Estela.set_data(x_hist, y_hist)

# Generar fotograma por fotograma
with writer.saving(Figura, "ContornoCircunferenciaConGiro.mp4", 192): # El último valor corresponde al DPI
    x_hist = []
    y_hist = []
    
    for fotograma in range(Segundos * Frames):
        tiempo = fotograma / float(Segundos * Frames)
        angulo = 360 * tiempo
        
        actualizar_grafico(angulo, tiempo, x_hist, y_hist)
        writer.grab_frame()
