import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter

#Magnitudes para tener un video a 1080p en pulgadas

Ancho = 10
Largo = 5.625

Figura = plt.figure(figsize=(Ancho, Largo))
Grafico, = plt.plot([], [], 'k-') #Crear un gráfico vacio
Segundos = 14 #Valor arbitrario de segundos que necesito la animacion
Frames = 60 #Cantidad de frames

plt.xlim(0, 10)
plt.ylim(0, 10)

def funcionLineal(x):
    return x

writer = FFMpegWriter(fps = Frames)

'''

xlist = np.linspace(0, 10, Segundos * Frames) #Quiero generar n números entre 0 a 10, donde n es la cantidad de datos que necesito para tener la fluides y duración deseada.
ylist = funcionLineal(xlist)

Grafico.set_data(xlist, ylist)
plt.show()

'''
xlist = []
ylist = []

#Generar fotograma por fotograma

with writer.saving(Figura, "Lineal.mp4", 192): #El último valor corresponde al DPI
    
    for fotograma in np.linspace(0, 10, Segundos * Frames):

        xlist.append(fotograma)
        ylist.append(funcionLineal(fotograma))

        Grafico.set_data(xlist, ylist)

        writer.grab_frame()