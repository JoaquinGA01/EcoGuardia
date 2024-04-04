# app/models.py
from mongoengine import Document, IntField, StringField, connect

# Conectarse a MongoDB (ajusta los parámetros según tu configuración)
connect('nombre_de_tu_base_de_datos', host='localhost', port=27017)

class Sensor(Document):
    idUsuario = IntField(required=True)
    idPlanta = IntField(required=True)
    idSensor = IntField(required=True)
    informacion = StringField(required=True)  # JSON como string

    # Métodos GET (estos son realmente innecesarios en Python pero los añado por completitud)
    
    def get_idUsuario(self):
        return self.idUsuario

    def get_idPlanta(self):
        return self.idPlanta

    def get_idSensor(self):
        return self.idSensor

    def get_informacion(self):
        return self.informacion

    # Métodos SET
    def set_idUsuario(self, idUsuario):
        self.idUsuario = idUsuario

    def set_idPlanta(self, idPlanta):
        self.idPlanta = idPlanta

    def set_idSensor(self, idSensor):
        self.idSensor = idSensor

    def set_informacion(self, informacion):
        self.informacion = informacion
