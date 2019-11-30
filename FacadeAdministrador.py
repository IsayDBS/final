from Administrador import *
class FacadeAdministrador():
    def __init__(self, nombre, cursor, connection):
        self.__administrador = Administrador(nombre,cursor,connection)

    def agregarRuta(self):
        self.__administrador.mostrarRutasYParadas()
        repito = True
        while repito == True:
            nombre = input("Nombre de la ruta a agregar: ").lower()
            try:
                asientos = int(input("Numero de asientos (De dejarlo vacio, se pondra por default 10): ") or "10")
            except:
                print("No es un numero de asientos validos")
                continue
            lista_paradas = self.__administrador.paradasEntrada()
            try:
                precio = int(input("Precio por estacion(Si se deja vacio, este se vuelve aleatorio): ") or "0")
            except:
                print("No es un valor valido")
                continue
            try:
                self.__administrador.crearRuta(nombre, asientos,lista_paradas,precio)
                #print("Precio por parada: " + str(self.__administrador.precioRuta(nombre)))
            except:
                print("Ya existe una ruta con ese nombre, intenta uno diferente")
            repito = False

    def agregarParada(self):#Recordar que no se pueden agregar nombres iguales en las paradas
        nombre_parada = input("Nombre de la parada a crear: ").lower()
        self.__administrador.mostrarRutas()
        repito = True
        while repito == True:
            try:
                ruta = input("Nombre de la ruta a la que vas a agregar: ").lower()
                self.__administrador.mostrarParadas(ruta)
                repito = False
            except:
                print("No existe tal ruta")
        repito2 = True
        while repito2 == True:
            try:
                posicion = int(input("Agrega en cierta posicion de la ruta(Si se deja vacia, se agregara al final de la ruta): ") or "0")
                repito2 = False
            except:
                print("No es una posicion valida")
        #try:
        paradas = self.__administrador.crearParada(nombre_parada,ruta,posicion)
        self.__administrador.actualizarRutaParadas(ruta,paradas)
        self.__administrador.agregarParada(nombre_parada,ruta)
        #except:
            #print("No es una ruta valida")

    def eliminarParada(self):
        #self.__administrador.mostrarRutas()
        if self.__administrador.mostrarRutas() != []:
            #self.__administrador.mostrarRutas()
            try:
                ruta = input("Nombre de la ruta a la que pertenece la parada que quieres borrar: ").lower()
                self.__administrador.mostrarParadas(ruta)
            except:
                print("No existe tal ruta")
                return
            try:
                parada = input("Nombre de la parada a eliminar: ").lower()
                if self.__administrador.boletosPorParada(parada) == True and self.__administrador.verificarBoletos(ruta,parada) == False:
            #print(paradas)
                    self.__administrador.eliminarParada(parada,ruta)#Este solo elimina de la tabla parada
                    paradas = self.__administrador.deleteParada(parada,ruta)#Esto en su conjunto elimina la parada de las rutas
                    if paradas == []:
                        self.__administrador.eliminarRuta(ruta)
                    self.__administrador.actualizarRutaParadas(ruta,paradas)
            #self.__administrador.Parada(parada,ruta)
                else:
                    print("La estacion no puede ser borrada, hay algunos boletos que entran o salen en esta terminal")
            except:
                print("No existe tal parada")

    #Elimina la ruta si no hay boletos en dicha ruta
    def eliminarRuta(self):
        self.__administrador.mostrarRutas()
        #print(self.__administrador.boletosPorRuta(nombre_ruta))
        repeticon = True
        while repeticon == True:
        #if self.__administrador.mostrarRutas() == []:
            #return
            try:
                nombre_ruta = input("Escoge el nombre de la ruta: ").lower()
                if self.__administrador.boletosPorRuta(nombre_ruta) == 0:#se puede eliminar la ruta, porque no hay boletos en esa ruta
            #necesitamos cada una de las paradas de la ruta
                    paradas = self.__administrador.getParadas(nombre_ruta)
                    #print(paradas)
                    for l in paradas:
                        self.__administrador.eliminarParadaRuta(l,nombre_ruta)
                    self.__administrador.eliminarRuta(nombre_ruta)
                    repeticon = False
                else:
                    print("No se puede eliminar la ruta, porque aun hay boletos en la ruta")
                    repeticon = False
            except:
                print("No es una ruta en la base de datos")
                repeticon = False
