from Boleto import *
from Vendedor import *
class FacadeVendedor():
    def __init__(self,nombre,cursor,connection):
        self.__vendedor = Vendedor(nombre, cursor, connection)

    #entrada, la estacion donde entra
    #salida, la estacion donde sale
    #nombre_ruta, la ruta donde compraran boletos
    def ventaBoletos(self,fecha_salida,entrada, salida):#fecha salida de la forma yyyy,mes,anio hh/mm/ss
        print(self.__vendedor.getRutas2Paradas(entrada,salida))
        if self.__vendedor.getRutas2Paradas(entrada,salida) == "":
            print("No hay ruta que pase por estas dos estaciones")
            return
        nombre_ruta = input("Entra la ruta en la cual quieras introducir el boleto\n")
        ruta = self.__vendedor.getRuta(nombre_ruta.lower())
        if self.__vendedor.verificaBoleto(entrada.lower(),ruta,salida.lower()) == True:#hay un lugar libre (entrada,salida,ruta,self.tickets)
            bl = Boleto(fecha_salida, entrada.lower(), salida.lower(),str(dt.datetime.now()),ruta)
            #print(bl)
            self.__vendedor.boletoVendido(bl)
        else:
            print("No hay boletos para esta terminal")

    def borrarBoletos(self,id):
        self.__vendedor.cancelaBoletos(id)

    def getRutasDParada(self,parada):
        return self.__vendedor.getRutasDParada(parada)
