class Persona():
    def __init__(self, name, cursor, connection):
        self.__name = name
        self.cursor = cursor
        self.connection = connection

    def getName(self):
        return self.__name

    def listaString(self,lista):
        string = ""
        for l in lista:
            if l == lista[-1]:
                string += l.lower()
            else:
                string += l.lower() + ", "
        return string

    def stringLista(self,string):
        lista = []
        lista = list(string.split(", "))
        return lista

    def tuplaAstring(self,lista):
        string = ""
        for l in lista:
            if l == lista[-1]:
                string += l[0]
            else:
                string += l[0] + ", "
        return string

    def getParadas(self,nombre_ruta):
        string_paradas = "SELECT paradas FROM Ruta WHERE nombre = " + self.setSQL(nombre_ruta) + ";"
        #print(string_paradas)
        self.cursor.execute(string_paradas)
        return self.stringLista(self.cursor.fetchall()[0][0])

    def todasParadas(self):
        string = "SELECT nombre FROM Ruta;"
        self.cursor.execute(string)
        lista = []
        for l in self.cursor.fetchall():
            lista.append(l[0])
        return lista

    def mostrarParadas(self,ruta):
        lista = self.getParadas(ruta)
        i = 0
        #print(lista)
        for l in lista:
            i += 1
            print("" + str(i) + "." + l.capitalize())


    def mostrarRutas(self):
        lista = self.todasParadas()
        i = 0
        if lista == []:
            print("No hay rutas registradas")
        #print(lista)
        else:
            for l in lista:
                i += 1
                print("" + str(i) + "." + l.capitalize())
        return lista

    def mostrarRutasYParadas(self):
        string = "SELECT nombre,paradas FROM Ruta;"
        self.cursor.execute(string)
        lista = self.cursor.fetchall()
        for i in range(len(lista)):
            print("Ruta: " + lista[i][0] + "\nParadas: " + lista[i][1]+"\n")

    def getRutas2Paradas(self,parada_uno,parada_dos):
        string_regreso = "SELECT nombre FROM Ruta WHERE paradas LIKE '%" + parada_uno + "%' AND paradas LIKE '%" + parada_dos + "%';"
        self.cursor.execute(string_regreso)
        lista = self.cursor.fetchall()
        if lista == []:
            return ""
        else:
            return self.tuplaAstring(lista)


    def setSQL(self,string):
        return "'" + string + "'"
