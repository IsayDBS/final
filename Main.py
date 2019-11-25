from dotenv import load_dotenv
from os.path import join, dirname, isdir
from os import environ
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

    def comenzar(self):
        admin = FacadeAdministrador("Isay",self.cursor,self.connection)
        #admin.agregarRuta("y",10,["a","b","e","f","g","h","n"])
        #admin.agregarRuta("z",10,["h","i","e","k","l","m","n"])
        #admin.eliminarParada("b","con queso")
        vendedor = FacadeVendedor("Isay",self.cursor,self.connection)
        #ruta = Ruta("La 600",10,["La Haya","Azcapo","La vieja","La nueva"],7)
        #for l in range(0,5):
            #vendedor.ventaBoletos("01-01-01 01-01-01","e","h")
        #vendedor.borrarBoletos("BVJ77")
        #vendedor.ventaBoletos("=1=1=1","a","h")
        admin.eliminarRuta("z")
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

    def encriptar(self, string):
        sha_signature = hashlib.sha256(string.encode()).hexdigest()
        return sha_signature

if __name__ == '__main__':
    main = Main()
    main.comenzar()
