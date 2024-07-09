import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter

#Magnitudes para tener un video a 1080p en pulgadas

Ancho = 10
Largo = 5.625

Figura = plt.figure(figsize=(Ancho, Largo))
graficoCuadratico, = plt.plot([], [], 'k-', label = "Función Cuadrática")
graficoRaiz, = plt.plot([], [], "b-", label = "Raíz Cuadrada" )
plt.legend(loc = "lower right")
Segundos = 14 
Frames = 60

plt.xlim(0, 3)
plt.ylim(0, 9)

axis = plt.gca()
axis.spines["top"].set_visible(False)
axis.spines["right"].set_visible(False)
axis.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)

def funcionCuadratica(x):
    return x*x

def funcionRaiz(x):
    return x**(1/2)

writer = FFMpegWriter(fps = Frames)

xlist = []
ylist = []

xlist2 = []
ylist2 = []

#Generar fotograma por fotograma

with writer.saving(Figura, "funcionInversa.mp4", 192): #El último valor corresponde al DPI
    
    for fotograma in np.linspace(0, 3, Segundos * Frames):

        xlist.append(fotograma)
        ylist.append(funcionCuadratica(fotograma))

        graficoCuadratico.set_data(xlist, ylist)
        
        xlist2.append(fotograma)
        ylist2.append(fotograma)
        
        graficoRaiz.set_data(xlist2, ylist2)

        writer.grab_frame()
