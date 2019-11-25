from dotenv import load_dotenv
from os.path import join, dirname, isdir
from os import environ
import mysql.connector
from mysql.connector import Error
from pathlib import Path
class Conector():
    def __init__(self,archivo):
        self.archivo = archivo
        self.connection, self.cursor = self.conectar()


    def conectar(self):
        dotenv_path = join(dirname(__file__), self.archivo)
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
