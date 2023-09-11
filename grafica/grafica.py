import matplotlib.pyplot as plt #Importa la biblioteca Matplotlib
import numpy as np #Importa la biblioteca NumPy 



def gr_con_prediccion(x_lim,y_lim,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion): #Define una función llamada gr_con_prediccion
    
    
    plt.figure(figsize=(15, 6)) #Crea una figura para la gráfica con un tamaño de 15 unidades de ancho y 6 unidades de alto
    plt.plot(	dataTeoricoEsfuerzo , dataTeoricoDeformacion) #Dibuja una línea que representa los datos teóricos de esfuerzo en el eje x y deformación en el eje y
    plt.scatter(	dataRealEsfuerzo, dataRealDeformacion, color='red') #Dibuja puntos dispersos en la gráfica de esfuerzo en el eje x y deformación en el eje y de color rojo
    plt.xlabel('Esfuerzo [kN]') #Etiqueta el eje x con el texto "Esfuerzo [kN]"
    plt.ylabel('Deformación [mm]') # Etiqueta el eje y con el texto "Deformación [mm]"
    plt.title('Gráfica 2: teórico versus real [ZOOM]') #Establece un título para la gráfica
    plt.xlim(0, x_lim) #Limita la visualización del eje x
    plt.ylim(0, y_lim) #Limita la visualización del eje y
    plt.grid() #Agrega una cuadrícula a la gráfica
    plt.gca().invert_yaxis() # Invierte el eje y para que los valores más altos estén en la parte superior
    plt.show() #Muestra la gráfica

def gr_con_prediccion_3000(prediction,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion,model): #Define una función llamada gr_con_prediccion_3000
  plt.figure(figsize=(15, 6)) #Crea una figura para la gráfica con un tamaño de 15 unidades de ancho y 6 unidades de alto
  plt.plot(	dataTeoricoEsfuerzo , dataTeoricoDeformacion)  #Dibuja una línea que representa los datos teóricos de esfuerzo en el eje x y deformación en el eje y
  plt.scatter(	dataRealEsfuerzo , dataRealDeformacion, color='red') #Dibuja puntos dispersos en la gráfica de esfuerzo en el eje x y deformación en el eje y de color rojo
  plt.plot(np.linspace(0,1000).reshape(-1,1),model.predict(np.linspace(0,1000).reshape(-1,1)),'m') #Predicción utilizando el modelo model en un rango de esfuerzos que va desde 0 hasta 1000 kN
  plt.scatter(	3000 , prediction, color='green') #Se coloca un punto verde en la gráfica en el punto (3000 kN, prediction) para representar la predicción a una carga de 3000 kN
  plt.xlabel('Esfuerzo [kN]') #Etiqueta el eje x con el texto "Esfuerzo [kN]"
  plt.ylabel('Deformación [mm]') # Etiqueta el eje y con el texto "Deformación [mm]"
  plt.title('Gráfica 3: Predicción a una carga de 3000 kN') #Establece un título para la gráfica
  plt.xlim(0, 3000) #Limita la visualización del eje x
  plt.ylim(0, 45) #Limita la visualización del eje y
  plt.grid() #Agrega una cuadrícula a la gráfica
  plt.gca().invert_yaxis() # Invierte el eje y para que los valores más altos estén en la parte superior
  plt.show() #Muestra la gráfica

def gr_sin_prediccion(dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion): #Define una función llamada gr_sin_prediccion
  plt.figure(figsize=(15, 6)) #Crea una figura para la gráfica con un tamaño de 15 unidades de ancho y 6 unidades de alto
  plt.plot(	dataTeoricoEsfuerzo , dataTeoricoDeformacion)  #Dibuja una línea que representa los datos teóricos de esfuerzo en el eje x y deformación en el eje y
  plt.scatter(	dataRealEsfuerzo , dataRealDeformacion, color='red') #Dibuja puntos dispersos en la gráfica de esfuerzo en el eje x y deformación en el eje y de color rojo
  plt.xlabel('Esfuerzo [kN]') #Etiqueta el eje x con el texto "Esfuerzo [kN]"
  plt.ylabel('Deformación [mm]') # Etiqueta el eje y con el texto "Deformación [mm]"
  plt.title('Gráfica 1: teórico versus real') #Establece un título para la gráfica
  plt.grid() #Agrega una cuadrícula a la gráfica
  plt.gca().invert_yaxis() # Invierte el eje y para que los valores más altos estén en la parte superior
  plt.show() #Muestra la gráfica
