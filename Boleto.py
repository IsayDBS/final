import datetime as dt
import random
class Boleto():
    def __init__(self,precio,entrada, salida,ruta,fecha_venta,id = ""):
        if id == "":
            self.__id = self.__setIdentificador()
        else:
            self.__id = id
        self.__ruta = ruta
        #self.__vendedor = vendedor
        #self.__fecha_salida = fecha_salida
        self.__entrada = entrada#estacion donde entra
        self.__salida = salida#estacion donde sale
        self.__precio = precio
        self.__fecha_venta = fecha_venta
        #self.diccionario = idDeBoletos()

    #def idDeBoletos(self):
        #string = "SELECT identificador FROM Boletos;"
        #self.cursor.execute(string)
        #lista = self.cursor.fetchall()
        #dict = {}
        #for l in lista:
            #dict[l[0]] = 0
        #return dict


    def getPrecio(self):
        return self.__precio

    def getPKRuta(self):
        return self.__ruta.getPkRuta()

    def getRuta(self):
        return self.__ruta.getNombre()

    def getFechaVenta(self):
        return self.__fecha_venta

    def getEntrada(self):
        return self.__entrada

    def getSalida(self):
        return self.__salida

    #def getFechaSalida(self):
        #return self.__fecha_salida

#    def getVendedor(self):
#        return self.__vendedor

    def getPrecio(self):
        return self.__precio

    def getId(self):
        return self.__id

    def __getLetra(self, posicion):
        string_aleatorio = "QWERTYUIOPASDFGHJKLZXCVBNM"
        return string_aleatorio[posicion]

    #EL identificador esta hecho de de dos letras y 3 numero al azar
    def __setIdentificador(self):
        string_regreso = ""
        for i in range(0,3):
            string_regreso += self.__getLetra(random.randint(0,25))
        for j in range(0,2):
            string_regreso += str(random.randint(0,9));
        return string_regreso.lower()

    def __str__(self):
        string_retorno = "==========================================================================================================\n"
        string_retorno+= "Identificador: " + self.__id.upper() + "\n"
        string_retorno+= "Precio: $" + str(self.getPrecio()) + "\n"
        string_retorno+= "Ruta: " + self.getRuta() + "\n"
        #string_retorno+= "Vendedor: " + self.__vendedor.getName() + "\n"
        #string_retorno+= "Fecha de venta: " + self.getFechaVenta() + "      Fecha de salida: " + str(self.__fecha_salida) + "\n"
        string_retorno+= "Estacion de entrada: " + self.__entrada + "\n"
        string_retorno+= "Estacion de llegada: " + self.__salida + "\n"
        string_retorno+= "=========================================================================================================="
        return string_retorno
