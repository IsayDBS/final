from datetime import datetime, timedelta
from Boleto import *
from Persona import *
from Ruta import *
class Vendedor(Persona):
    def __init__(self,name, cursor, connection):
        super().__init__(name,cursor,connection)
        #self.tickets = ticket

#    def obtenerTickets(self):
#        pass

    def getRutasDParada(self,nombreParada):
        string_rutas = "SELECT nombre FROM Ruta WHERE paradas LIKE '%" + nombreParada +"%';"
        self.cursor.execute(string_rutas)
        list = self.cursor.fetchall()
        return list

    def setTickets(self,tickets):
        self.tickets = tickets

#    def ventaBoletos(self,fecha_salida,entrada, salida,nombre_ruta):#fecha salida de la forma yyyy,mes,anio hh/mm/ss
#        ruta = self.__getRuta(nombre_ruta.lower())
#        if self.verificaBoleto(entrada.lower(),ruta,salida.lower()) == True:#hay un lugar libre (entrada,salida,ruta,self.tickets)
#            bl = Boleto(fecha_salida, entrada.lower(), salida.lower(),str(dt.datetime.now()),ruta)
            #print(bl)
#            self.__BoletoVendido(bl)
#        else:
#            print("No hay boletos para esta terminal")

    def getRuta(self,ruta):
        string_ruta = "SELECT * FROM Ruta WHERE nombre = "+ self.__setSQL(ruta) +";"
        self.cursor.execute(string_ruta)
        lista = self.cursor.fetchall()
        return Ruta(lista[0][1],lista[0][2],self.stringLista(lista[0][3]),lista[0][0])

    def __getRutaNombre(self,pk):
        string_ruta = "SELECT nombre FROM Ruta WHERE pk_id_ruta = "+ str(pk) +";"
        self.cursor.execute(string_ruta)
        lista = self.cursor.fetchall()
        return lista[0][0]

    def __getTickets(self,pk):#es una lista con los nombres de la parada de ruta EN ORDEN
        string_busca = "SELECT * FROM Boletos WHERE fk_id_ruta = " + str(pk) + ";"
        self.cursor.execute(string_busca)
        lista = self.cursor.fetchall()
        nombre_ruta = self.__getRutaNombre(pk)
        tickets = []
        for l in lista:
            tickets.append(Boleto(l[2],l[3],l[4],l[1],nombre_ruta,l[0]))
        return tickets

    def cancelaBoletos(self, identificador):
        string_cancelado = "DELETE FROM Boletos WHERE identificador = " + self.__setSQL(identificador) + ";"
        #print(string_cancelado)
        self.cursor.execute(string_cancelado)
        self.connection.commit()

    def __setSQL(self,string):
        return "'" + string.lower() + "'"

    def boletoVendido(self,boleto):
        string_vendido = "INSERT INTO Boletos(identificador,fecha_venta,fecha_salida,estacion_entrada,estacion_salida,fk_id_ruta) VALUES(" + self.__setSQL(boleto.getId()) + "," + self.__setSQL(boleto.getFechaVenta()) + "," + self.__setSQL(boleto.getFechaSalida()) + "," + self.__setSQL(boleto.getEntrada()) + "," + self.__setSQL(boleto.getSalida()) + "," + str(boleto.getPKRuta()) + ");"
        #print(string_vendido)
        self.cursor.execute(string_vendido)
        self.connection.commit()

    def verificaBoleto(self,entrada,ruta,estacion_llegada):
        tickets = self.__getTickets(ruta.getPkRuta())#colecciona todos los boletos que hay sido vendidos
        asientos = 0 # utilizado para ver si al final son los mismos asientos en el autobous
        for t in tickets:
            #print(t)
            if self.__ocupadoSalida(t,entrada,ruta,estacion_llegada) == True: #revisa si hay boletos que ya tengan ocupados cierta posicion
                asientos += 1
        if asientos >= ruta.getAsientos():
            return False#NO se pueden vender mas boletos
        return True#SE PUEDEN VENDER MAS BOLETOS"""

    def __ocupadoSalida(self,ticket, salida, ruta,estacion_llegada):#deber
        entra_ticket = ruta.getParadas().index(ticket.getEntrada())
        salida_ticket = ruta.getParadas().index(ticket.getSalida())
        entra_nvo = ruta.getParadas().index(salida)
        sale_viejo = ruta.getParadas().index(estacion_llegada)
        #print(ruta.getParadas())
        #print(salida)
        #print(entra)
        #print(salida0)
        #print(ruta.getParadas())
        #este revisa por dentro del ticket
        for i in range(entra_ticket,salida_ticket+1):
            if ruta.getParadas()[i] == salida and i != salida_ticket:
                return True #True, significa que el asiento esta ocupado
        #revisa por fuera
        if entra_nvo < entra_ticket and sale_viejo <= salida_ticket:
            return True
        return False #El asiento esta desocupado


#ven = Boleto("Isay","ABC19", 10,"San Lazaro","Observatorio")
#ven.ventaBoletos(2,datetime.now()+timedelta(days=1))
