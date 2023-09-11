from data.data import * #Importa todo desde el módulo data
from BD.baseDatos import * # Importa todo desde el módulo baseDatos en el paquete BD
from sklearn.linear_model import LinearRegression # Crear un modelo de regresión lineal
from grafica.grafica import * # Importa todo desde el módulo grafica
import pandas as pd # Importa el módulo pandas

#Datos del excel
dataTeoricoEsfuerzo, dataTeoricoDeformacion = dataTeorico() #Llama a la función dataTeorico() del módulo data y almacena sus resultados en las variables

#Datos de la base de datos y realizamos el modelo
data_list = lecturaDatos() #Llama a la función lecturaDatos() del módulo baseDatos y almacena sus resultados en la variable data_list
data_real = pd.DataFrame(data_list) #Se crea un DataFrame de pandas llamado data_real
data_real_fit = data_real #Se hace una copia del DataFrame data_real y se almacena en data_real_fit
X = data_real_fit['Esfuerzo[kN]'].values.reshape(-1, 1) #Extrae la columna Esfuerzo[kN] del DataFrame data_real_fit
y = data_real_fit['Deformacion[mm]'].values.reshape(-1, 1) #Extrae la columna Deformacion[mm] del DataFrame data_real_fit
x_lim = data_real['Esfuerzo[kN]'].iloc[-1] #Calcula el valor del último elemento de la columna Esfuerzo[kN]
y_lim = data_real['Deformacion[mm]'].iloc[-1] #Calcula el valor del último elemento de la columna Deformacion[mm]
model = LinearRegression() #Crea un modelo de regresión lineal 
model.fit(X, y) #Ajusta el modelo de regresión lineal a los datos
prediction = round(model.predict(np.array([3000]).reshape(-1, 1))[0][0],1) #Realiza una predicción usando el modelo entrenado
print('la predicción a 1000 kN es de: ', prediction ,'mm') # Imprime la predicción


dataRealEsfuerzo = data_real['Esfuerzo[kN]'] #Almacena la columna Esfuerzo[kN] del DataFrame
dataRealDeformacion = data_real['Deformacion[mm]'] #Almacena la columna 'Deformacion[mm]' del DataFrame 

#realizamos la lectura de las gráficas
gr_sin_prediccion(dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion) #Lamado de las funciones definidas en el módulo grafica para generar gráficas
gr_con_prediccion(x_lim,y_lim,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion)  #Lamado de las funciones definidas en el módulo grafica para generar gráficas
gr_con_prediccion_3000(prediction,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion,model)  #Lamado de las funciones definidas en el módulo grafica para generar gráficas

