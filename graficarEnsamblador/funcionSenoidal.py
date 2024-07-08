import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter

#Magnitudes para tener un video a 1080p en pulgadas

Ancho = 10
Largo = 5.625

Figura = plt.figure(figsize=(Ancho, Largo))
Grafico, = plt.plot([], [], 'b-') #Crear un gráfico vacio
Segundos = 14 #Valor arbitrario de segundos que necesito la animacion
Frames = 60 #Cantidad de frames

plt.xlim(-5, 5)
plt.ylim(-2, 2)

axis = plt.gca() # Obtener los ejes

#Quitar el limite superior y derecho.

ticks_y = (np.arange(-2, 2, 1))
axis.set_yticks(ticks_y[1:]) 
axis.set_xticks([0])

axis.spines['top'].set_visible(False)
axis.spines['right'].set_visible(False)

#Establecer los 4 ejes

plt.plot(axis.get_xlim(), [0, 0], "k--")
plt.plot([0,0], axis.get_ylim(), "k--")

def funcionSenoidal(x):
    return np.sin(x)

writer = FFMpegWriter(fps = Frames)

xlist = []
ylist = []

#Generar fotograma por fotograma

with writer.saving(Figura, "Senoidal.mp4", 192): #El último valor corresponde al DPI
    
    for fotograma in np.linspace(-5, 5, Segundos * Frames):

        xlist.append(fotograma)
        ylist.append(funcionSenoidal(fotograma))

        Grafico.set_data(xlist, ylist)

        writer.grab_frame()