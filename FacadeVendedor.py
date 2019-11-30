from Boleto import *
from Vendedor import *
class FacadeVendedor():
    def __init__(self,nombre,cursor,connection):
        self.__vendedor = Vendedor(nombre, cursor, connection)

    #entrada, la estacion donde entra
    #salida, la estacion donde sale
    #nombre_ruta, la ruta donde compraran boletos
    def ventaBoletos(self):#fecha salida de la forma yyyy,mes,anio hh/mm/ss
        self.__vendedor.mostrarRutasYParadas()
        repito = True
        while repito ==True:
            try:
                entrada = input("Terminal donde quieres entrar: ").lower()
                salida = input("Terminal donde quieres llegar: ").lower()
                if entrada == salida:
                    print("Son la misma parada, no se puede vender el boleto")
                    continuar= input("Deseas continuar(si(Y), no (Culaquier otra cosa))").lower
                    if continuar == "y":
                        continue
                    else:
                        return
                elif self.__vendedor.getRutas2Paradas(entrada,salida) == "":
                    print("No hay ruta que pase por estas dos estaciones, deseas continuar(si(Y),no(Cualquier otra cosa))?")
                    continuar = input().lower
                    if continuar == "y":
                        continue
                    else:
                        return
                else:
                    repito = False
            except:
                print("Las terminales no estan registradas en el sistema, intenta de nuevo")
                continue
        #self.__vendedor.mostrarRutasVend(entrada,salida)
        importante = self.__vendedor.rutaYBoletosDisponibles(entrada,salida)
        if importante == []:
            print("No hay boletos para estas estaciones")
            return
        #no_boletos = int(input("Numero de boletos(Si se deja vacio, se entendera que se vendera solo uno): ") or "1")
        repito2 = True
        while repito2 == True:
            try:
                print("0 para salir de la venta")
                nombre_ruta = input("Entra la ruta en la cual quieras introducir el(los) boleto(s): ")
                if nombre_ruta == "0":
                    return
                ruta = self.__vendedor.getRuta(nombre_ruta.lower())
                if ruta.getNombre() not in importante:
                    print("Tal ruta no pasa por las terminales")
                    continue
                if ruta == None:
                    print("No hay tal ruta")
                repito2 = False
            except:
                print("No es una ruta valida, intenta de nuevo")
                continue
        #self.__vendedor.noDeBoletos(no_boletos,nombre_ruta)
        boletos_disponibles = self.__vendedor.boletosDisponibles(ruta,entrada,salida)
        if boletos_disponibles == 0:
            print("No hay boletos disponibles para esta ruta")
            return
        else:
            #print("Hay " + str(boletos_disponibles) + " asientos disponibles en esta ruta")
            repeticion = True
            while repeticion == True:
                no_boletos = int(input("Numero de boletos(Si se deja vacio, se entendera que se vendera solo uno): ") or "1")
                if no_boletos > boletos_disponibles:
                    print("No se puede imprimir la cantidad de boletos que pides, intenta con otro")
                    continue
                else:
                    precio = self.__vendedor.getPrecio(nombre_ruta) * self.__vendedor.noParadas(entrada,salida,ruta)
        #print(precio)
        #print(ruta.getParadas())
                    for b in range(0,no_boletos):
            #if self.__vendedor.verificaBoleto(entrada.lower(),ruta,salida.lower()) == True:#hay un lugar libre (entrada,salida,ruta,self.tickets)
                        bl = Boleto(precio,entrada.lower(), salida.lower(),ruta,str(dt.datetime.now()))#,str(dt.datetime.now())
                        print(bl)
                        self.__vendedor.boletoVendido(bl)
                repeticion = False
            #else:
                #print("No hay boletos para esta terminal")

    def borrarBoletos(self):
        id = input("Introduce el identificador del boleto: ").lower()
        self.__vendedor.cancelaBoletos(id)

    def getRutasDParada(self,parada):
        return self.__vendedor.getRutasDParada(parada)
