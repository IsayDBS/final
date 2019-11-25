from Ruta import *
from Persona import *
class Administrador(Persona):
    def __init__(self, name,cursor,connection):
        super().__init__(name,cursor,connection)

    def getParadas(self,nombre_ruta):
        string_paradas = "SELECT paradas FROM Ruta WHERE nombre = " + self.__setSQL(nombre_ruta) + ";"
        self.cursor.execute(string_paradas)
        return self.stringLista(self.cursor.fetchall()[0][0])

    def obtenerRuta(self,nombre):
        string_nombre = "SELECT * FROM Ruta WHERE nombre = " + self.__setSQL(nombre.lower()) + ";"
        self.cursor.execute(string_nombre)
        lista = self.cursor.fetchall()
        return lista

    def __setSQL(self,string):
        return "'" + string + "'"

    def eliminarParadaRuta(self,parada,ruta):
        self.eliminarParada(parada,ruta)#Este solo elimina de la tabla parada
        paradas = self.deleteParada(parada,ruta)#Esto en su conjunto elimina la parada de las rutas
        self.actualizarRutaParadas(ruta,paradas)

    def crearRuta(self,nombre,asientos,lista_paradas):
        string_ruta = "INSERT INTO Ruta(nombre,asientos,paradas) VALUES(" + self.__setSQL(nombre.lower()) + " ," + str(asientos) + " ," + self.__setSQL(self.listaString(lista_paradas)) + ");"
        #print(string_ruta)
        self.cursor.execute(string_ruta)
        self.connection.commit()
        self.paradaEnTabla(lista_paradas,nombre)

    def paradaEnTabla(self,lista,nombre):
        for l in lista:
            if self.revisaParada(l) == False:
                self.agregarParada(l,nombre)
                #revisa parada, la parada no existe, creala
                #string_paradas = "INSERT INTO Paradas(nombre,rutas) VALUES(" + self.__setSQL(l.lower()) + " ," + self.__setSQL(nombre) + ");"
                #print(string_paradas)
                #self.cursor.execute(string_paradas)
                #self.connection.commit()
            else:
                #la parada existe, actualiza una ruta a esa parada
                self.actualizarParadasAnteriores(l,nombre)

    def agregarParada(self,l,nombre):
        string_paradas = "INSERT INTO Paradas(nombre,rutas) VALUES(" + self.__setSQL(l.lower()) + " ," + self.__setSQL(nombre) + ");"
        #print(string_paradas)
        self.cursor.execute(string_paradas)
        self.connection.commit()

    def revisaParada(self,nombre_parada):
        string_revisa = "SELECT *FROM Paradas WHERE nombre = " + self.__setSQL(nombre_parada) + ";"
        self.cursor.execute(string_revisa)
        lista = self.cursor.fetchall()
        if lista == []:
            return False#La parada no existe
        else:
            return True#La parada existe

    def __getPkRuta(self,nombre_ruta):
        string_pk = "SELECT pk_id_ruta FROM Ruta WHERE nombre = " + self.__setSQL(nombre_ruta) + ";"
        self.cursor.execute(string_pk)
        list = self.cursor.fetchall()
        if list == []:
            return 0
        else:
            return list[0][0]

    def boletosPorRuta(self,nombre_ruta):
        pk_id_ruta = self.__getPkRuta(nombre_ruta)
        if pk_id_ruta == 0:
            return 0
        else:
            string_ruta = "SELECT identificador FROM Boletos WHERE fk_id_ruta = " + str(pk_id_ruta) + ";"
            self.cursor.execute(string_ruta)
            return len(self.cursor.fetchall())

    def paradasLista(self,nombre,nombre_ruta):
        string_obtener = "SELECT rutas FROM Paradas WHERE nombre = " + self.__setSQL(nombre) + ";"
        self.cursor.execute(string_obtener)
        cadena = self.cursor.fetchall()
        lista = self.stringLista(cadena[0][0])
        lista.append(nombre_ruta)
        return lista


    def actualizarParadasAnteriores(self,nombre,nombre_ruta):
        lista = self.paradasLista(nombre,nombre_ruta)
        string_rutas="UPDATE Paradas SET rutas = " + self.__setSQL(self.listaString(lista)) + " WHERE nombre = " + self.__setSQL(nombre.lower()) +";"
        self.cursor.execute(string_rutas)
        self.connection.commit()


    def mostrarRutas(self):
        print(self.listaString(self.__ruta.getParadas()))

    def actualizarRutaParadas(self,nombre,lista_paradas):
        string_ruta = "UPDATE Ruta SET paradas = " + self.__setSQL(self.listaString(lista_paradas)) + " WHERE nombre = " + self.__setSQL(nombre.lower()) + ";"
        self.cursor.execute(string_ruta)
        self.connection.commit()

    def eliminarRuta(self,nombre):
        string_ruta = "DELETE FROM Ruta WHERE nombre = " + self.__setSQL(nombre.lower()) + ";"
        self.cursor.execute(string_ruta)
        self.connection.commit()

    def boletosPorParada(self,parada):
        string_boletos = "SELECT identificador FROM Boletos WHERE estacion_entrada = " + self.__setSQL(parada) + " OR estacion_salida = " + self.__setSQL(parada) + ";"
        self.cursor.execute(string_boletos)
        if self.cursor.fetchall() == []:
            return True #La estacion puede ser borrada
        else:
            return False #La estacion no puede ser borrada

    def crearParada(self,nombre,nombre_ruta,posicion = 0):
        lista_paradas = self.getParadas(nombre_ruta)
        if posicion == 0:
            lista_paradas.append(nombre)
        else:
            lista_paradas.insert(posicion,nombre)
        return lista_paradas

    def deleteParada(self,nombre,nombre_ruta):
        lista_paradas = self.getParadas(nombre_ruta)
        lista_paradas.remove(nombre)
        return lista_paradas

    def getRutas(self,nombre):
        string_rutas = "SELECT rutas FROM Paradas WHERE nombre = " + self.__setSQL(nombre) + ";"
        self.cursor.execute(string_rutas)
        rutas = self.cursor.fetchall()
        return self.stringLista(rutas[0][0])

    def eliminarParada(self, nombre,ruta):
        algo = self.getRutas2Paradas(nombre,nombre);
        algo2 = self.stringLista(algo)
        #print(algo2)
        algo2.remove(ruta)
        #print(algo)
        #lista = self.getRutas(nombre)
        if len(algo2) == 0:
            string_borrar = "DELETE FROM Paradas WHERE nombre = " + self.__setSQL(nombre) + ";"
        else:
            #algo2 = self.stringLista(algo)
            #print(algo2)
            #algo2.remove(ruta)
            string_borrar = "UPDATE Paradas SET rutas = " + self.__setSQL(self.listaString(algo2)) + "WHERE nombre = " + self.__setSQL(nombre) + ";"
        self.cursor.execute(string_borrar)
        self.connection.commit()

    def eliminarRuta(self,nombre):
        string = "DELETE FROM Ruta WHERE nombre = " + self.__setSQL(nombre) + ";"
        self.cursor.execute(string)
        self.connection.commit()