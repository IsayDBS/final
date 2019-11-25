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

    def __tuplaAstring(self,lista):
        string = ""
        for l in lista:
            if l == lista[-1]:
                string += l[0]
            else:
                string += l[0] + ", "
        return string


    def getRutas2Paradas(self,parada_uno,parada_dos):
        string_regreso = "SELECT nombre FROM Ruta WHERE paradas LIKE '%" + parada_uno + "%' AND paradas LIKE '%" + parada_dos + "%';"
        self.cursor.execute(string_regreso)
        lista = self.cursor.fetchall()
        if lista == []:
            return ""
        else:
            return self.__tuplaAstring(lista)
