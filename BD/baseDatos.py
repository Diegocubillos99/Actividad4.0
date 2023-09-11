from pymongo.mongo_client #Establecer la conexión con una base de datos MongoDB
import MongoClient #Establecer la conexión con una base de datos MongoDB

#CONEXIÓN
def conexion(): #Establecer la conexión con una base de datos MongoDB
    uri = "mongodb+srv://davidmateo0509:1234@cluster0.afpjypb.mongodb.net/?retryWrites=true&w=majority" #Servidor MongoDB del compañero del grupo donde se almacearon los datos de las diferentes deformaciones
    # Create a new client and connect to the server
    return MongoClient(uri)

#CREATE
""" Código necesario para crear un create en MongoDB"""


#READ
""" Código necesario para crear un read en MongoDB"""
def lecturaDatos():
    client = conexion()
    db = client.actividad4.data_real #Acceder a una base de datos llamada actividad4 y a la colección data_real
    data_list = [] #Los datos se agregan a la lista 
    for data_real_bd in db.find(): #Consulta de todos los registros 
        data_list.append(data_real_bd)
    return data_list

#UPDATE
""" Código necesario para actualizar un dato en la BD"""

#DELETE
""" Código necesario para eliminar un dato en la BD"""
