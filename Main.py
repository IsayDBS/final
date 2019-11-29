from dotenv import load_dotenv
from os.path import join, dirname, isdir
from os import environ
import sys
import mysql.connector
import hashlib
from FacadeAdministrador import *
from FacadeVendedor import *
class Main():

    def __init__(self):
        self.connection, self.cursor = self.conectar()

    def conectar(self):
        dotenv_path = join(dirname(__file__), ".env")
        load_dotenv(dotenv_path)
        dbname=environ.get("db_name")
        host=environ.get("db_host")
        username=environ.get("db_username")
        password=environ.get("db_password")
        connection = mysql.connector.connect(database = dbname,
                                                host = host,
                                                username = username,
                                                password = password)
        cursor = connection.cursor()
        return connection, cursor

    def mostrarAdministrador(self):
        print("1.Agrega Ruta\n2.Agregar Parada\n3.Eliminar Parada\n4.Eliminar Ruta\n5.Salir")

    def mostrarVendedor(self):
        print("1.Vender Boleto\n2.Cancelar Boletos\n3.Salir")

    def comenzar(self):
        admin = FacadeAdministrador("Isay",self.cursor,self.connection)
        if int(sys.argv[1]) == 1:
            repeticion = True
            while repeticion == True:
                try:
                    self.mostrarAdministrador()
                    valor0 = int(input("Input del Administrador\n"))
                    if valor0 == 1:
                        admin.agregarRuta()
                    elif valor0 == 2:
                        admin.agregarParada()
                    elif valor0 == 3:
                        admin.eliminarParada()
                    elif valor0 == 4:
                        admin.eliminarRuta()
                    elif valor0 == 5:
                        print("Adios")
                        repeticion = False
                    else:
                        print("No es opcion valida")
                except:
                    print("No es opcion valida")

        elif int(sys.argv[1]) == 2:
            repeticion = True
            vendedor = FacadeVendedor("Isay",self.cursor,self.connection)
        #ruta = Ruta("La 600",10,["La Haya","Azcapo","La vieja","La nueva"],7)
        #for l in range(0,5):
            #vendedor.ventaBoletos("01-01-01 01-01-01","e","h")
        #vendedor.borrarBoletos("BVJ77")
            while repeticion == True:
                try:
                    self.mostrarVendedor()
                    valor1 = int(input("Input del vendedor\n"))
                    if valor1 == 1:
                        vendedor.ventaBoletos()
                    elif valor1 == 2:
                        vendedor.borrarBoletos()
                    elif valor1 == 3:
                        repeticion = False;
                        print("Adios")
                    else:
                        print("Opcion no valida")
                except:
                    print("NO es opcion valida")
        #admin.eliminarRuta("h")
        #vendedor.ventaBoletos("=1=1=1","a","h")
        #vendedor.ventaBoletos("=1=1=1","a","h")
        #vendedor.ventaBoletos("=1=1=1","a","h")
        #vendedor.ventaBoletos("=1=1=1","a","h")
        #vendedor.getRutasDParada("e")
        #vendedor.borrarBoletos("cyd63")

        #admin = FacadeAdministrador("Isay",self.cursor,self.connection)
        #admin.agregarRuta("con queso",10,["a","b","e","f","g","h","n"])
        #admin.agregarRuta("quesadilla",10,["h","i","e","k","l","m","n"])
        #admin.eliminarParada("b","con queso")
        #admin.agregarParada("z","quesadilla")
        #print(admin.getParadas())
        #paradas = admin.crearParada("los cochis",admin.getParadas())
        #paradas = admin.eliminarParada("La Hoya",admin.getParadas())
        #admin.actualizarRutaParadas("la uriel",paradas)
        #admin.eliminarRuta("La 600")

    #def encriptar(self, string):
        #sha_signature = hashlib.sha256(string.encode()).hexdigest()
        #return sha_signature

if __name__ == '__main__':
    main = Main()
    main.comenzar()
