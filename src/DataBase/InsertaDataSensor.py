from pymongo import MongoClient
from datetime import datetime

class DataSensor:
    def __init__(self):
        self.clientMongoDB=MongoClient('mongodb://localhost:27017/')
        self.conexion=self.clientMongoDB['IoTDatabase']
        self.coleccion = self.conexion['LecturasSensor']

    def insertar_lectura(self):
        lectura['timestamp'] = datetime.now()
        resultado = self.coleccion.insert_one(lectura)
        return resultado.inserted_id
    def consultar_lecturas(self):
        lecturas = self.coleccion.find()
        return list(lecturas)

    def consultar_lecturas_filtro_hora(self, hora_inicio, hora_fin):
        start_time = datetime.strptime(hora_inicio, '%Y-%m-%d %H:%M:%S')
        end_time = datetime.strptime(hora_fin, '%Y-%m-%d %H:%M:%S')
        query = {
            "timestamp": {
                "$gte": start_time,
                "$lt": end_time
            }
        }
        lecturas = self.coleccion.find(query)
        return list(lecturas)


# Pruebas para el main
# if __name__ == "__main__":

#     adquisicion = DataSensor()

#     lectura = {
#         "sensor_id": "12345",
#         "valor": 23.5,
#         "unidad": "Celsius"
#     }
#     hora_inicio = "2024-10-19 20:00:00"
#     hora_fin = "2024-10-19 20:00:00"
#     lecturas = adquisicion.consultar_lecturas_filtro_hora(hora_inicio, hora_fin)
#     print("Lecturas-->",lecturas)
#     # lectura = adquisicion.consultar_lecturas()
#     # print(f"Lectura : {lectura}")
#     # id_insertado = adquisicion.insertar_lectura('lecturas', lectura)
#     # print(f"Lectura insertada con ID: {id_insertado}")