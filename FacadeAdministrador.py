from Administrador import *
class FacadeAdministrador():
    def __init__(self, nombre, cursor, connection):
        self.__administrador = Administrador(nombre,cursor,connection)

    def agregarRuta(self,nombre, asientos, lista_paradas):
        self.__administrador.crearRuta(nombre, asientos,lista_paradas)

    def agregarParada(self,nombre_parada,ruta):
        paradas = self.__administrador.crearParada(nombre_parada,ruta)
        self.__administrador.actualizarRutaParadas(ruta,paradas)
        self.__administrador.agregarParada(nombre_parada,ruta)

    def eliminarParada(self,parada,ruta):
        if self.__administrador.boletosPorParada(parada) == True:
            #print(paradas)
            self.__administrador.eliminarParada(parada,ruta)#Este solo elimina de la tabla parada
            paradas = self.__administrador.deleteParada(parada,ruta)#Esto en su conjunto elimina la parada de las rutas
            self.__administrador.actualizarRutaParadas(ruta,paradas)
            #self.__administrador.Parada(parada,ruta)
        else:
            print("La estacion no puede ser borrada")

    #Elimina la ruta si no hay boletos en dicha ruta
    def eliminarRuta(self,nombre_ruta):
        #print(self.__administrador.boletosPorRuta(nombre_ruta))
        if self.__administrador.boletosPorRuta(nombre_ruta) == 0:#se puede eliminar la ruta, porque no hay boletos en esa ruta
            #necesitamos cada una de las paradas de la ruta
            paradas = self.__administrador.getParadas(nombre_ruta)
            #print(paradas)
            for l in paradas:
                self.__administrador.eliminarParadaRuta(l,nombre_ruta)
            self.__administrador.eliminarRuta(nombre_ruta)
        else:
            print("No se puede eliminar la ruta, porque aun hay boletos en la ruta")
