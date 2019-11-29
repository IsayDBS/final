#En dicha ruta, van en una direccion
class Ruta():
    def __init__(self,nombre,asientos,paradas,pk_id_ruta,precio):
        self.__nombre = nombre
        self.__asientos = asientos
        self.__paradas = paradas
        self.__pk_id_ruta = pk_id_ruta
        self.__precio = precio

    def getPrecio(self):
        return self.__precio

    def getPkRuta(self):
        return self.__pk_id_ruta

    def getNombre(self):
        return self.__nombre

    def getAsientos(self):
        return self.__asientos

    def getParadas(self):
        return self.__paradas
