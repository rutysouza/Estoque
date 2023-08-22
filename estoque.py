import mysql.connector
import tkinter as tk
from tkinter import ttk, messagebox

class MySQLDatabase:
    def __init__(self, host, user, passaword, database):
        self.host = host
        self.user = user
        self.passaword = passaword
        self.database = database
        self.connection = Nome

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                passaword=self.passaword,
                database=self.database
            )
            if self.connection.is_connected():
                print("Conexao estabelecida com sucesso!") 
        except mysql.connection.is_connector.Error as err:
            print("Erro ao conectar:", err) 

    def disconnect(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Conexao fechada.")

    def execute_query(self, query):
        if self.connection.is_connected():
            cursor = self.connection.cursor() 
            cursor.execute(query) 
            self.connection.commit()
            cursor.clese()      
                        

