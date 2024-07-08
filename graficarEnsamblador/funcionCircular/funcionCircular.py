import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter

# Magnitudes para tener un video a 1080p en pulgadas
Ancho = 10
Largo = 5.625

Figura = plt.figure(figsize=(Ancho, Largo))
Grafico, = plt.plot([], [], 'k-')  # Línea recta inicial en negro
Estela, = plt.plot([], [], 'k--', alpha=0.3)  # Estela inicial en negro con transparencia

Segundos = 14  # Valor arbitrario de segundos que necesito la animación
Frames = 60  # Cantidad de frames por segundo

plt.xlim(-1, 1)
plt.ylim(-1, 1)

axis = plt.gca()  # Obtener el eje de las abscisas (X)

# Quitar todos los spines del gráfico
axis.spines['top'].set_visible(False)
axis.spines['right'].set_visible(False)
axis.spines['bottom'].set_visible(False)
axis.spines['left'].set_visible(False)

# Asegurar que los ejes X y Y tengan la misma escala
axis.set_aspect('equal')

# Ocultar los ticks del eje x y y
axis.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)

writer = FFMpegWriter(fps=Frames)

def actualizar_grafico(angulo, tiempo, x_hist, y_hist):
    if tiempo <= 1.0:
        # Durante los primeros dos segundos, la línea se mantiene recta hasta el borde
        longitud = tiempo * 1.0  # Longitud aumenta linealmente con el tiempo
        color_estela = 'k'  # Color de la estela negro
    else:
        # Después de los dos segundos, la longitud se mantiene constante (1.0)
        longitud = 1.0
        color_estela = 'k'  # Color de la estela negro
    
    if tiempo >= 1.0:
        # Si ya terminó de dibujarse completamente, actualizar la longitud a 1.0
        longitud = 1.0
    
    # Convertir el ángulo a radianes
    radianes = np.deg2rad(angulo)
    # Calcular las coordenadas de la línea en función del ángulo y la longitud
    x = [0, longitud * np.cos(radianes)]
    y = [0, longitud * np.sin(radianes)]
    Grafico.set_data(x, y)
    
    # Guardar las coordenadas actuales en el historial
    x_hist.append(x[1])  # Solo guardamos la coordenada x del punto final
    y_hist.append(y[1])  # Solo guardamos la coordenada y del punto final
    
    # Actualizar la estela con todas las coordenadas históricas
    Estela.set_data(x_hist, y_hist)
    Estela.set_color(color_estela)  # Establecer el color de la estela

# Generar fotograma por fotograma
with writer.saving(Figura, "funcionCircular.mp4", 192):  # El último valor corresponde al DPI
    x_hist = []
    y_hist = []
    
    for fotograma in range(Segundos * Frames):
        if fotograma < 2 * Frames:  # Fase de dibujo recto durante los primeros 2 segundos
            tiempo = fotograma / float(2 * Frames)
            angulo = 0  # La línea se mantiene recta (ángulo 0) durante el dibujo recto
        else:  # Fase de rotación después de completar el dibujo recto
            tiempo = 1.0
            angulo = 360 * (fotograma - 2 * Frames) / float((Segundos - 2) * Frames)
        
        actualizar_grafico(angulo, tiempo, x_hist, y_hist)
        writer.grab_frame()
