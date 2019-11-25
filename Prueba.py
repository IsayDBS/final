from Boleto import *
from Vendedor import *
from Ruta import *
from Parada import *

A = "A"
B = "B"
C = "C"
D = "D"
E = "E"
F = "F"
list = []
list.append(A)
list.append(B)
list.append(C)
list.append(D)
list.append(E)
list.append(F)
ruta = Ruta(3,list)
tickets = []
vendedor = Vendedor("Isay","ABCDE10","","",tickets)
ticket0 = Boleto(vendedor,"01-10-2010","A","D")
ticket1 = Boleto(vendedor,"01-10-2010","A","D")
ticket2 = Boleto(vendedor,"01-10-2010","A","D")
ticket3 = Boleto(vendedor,"01","D","F")
ticket4 = Boleto(vendedor,"01","D","E")
ticket5 = Boleto(vendedor,"01","D","F")
tickets.append(ticket0)
tickets.append(ticket1)
tickets.append(ticket2)
#tickets.append(ticket3)
tickets.append(ticket4)
tickets.append(ticket5)
vendedor.setTickets(tickets)
vendedor.ventaBoletos("01","A","F",ruta)
#print(verificaBoleto("D","F",ruta,tickets))
#print(verificaBoleto("A","C",ruta,tickets))
