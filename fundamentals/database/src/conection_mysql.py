import mysql.connector
import os
from dotenv import load_dotenv

class Database:
    # CLASSE PARA GERENCIAR A CONEXÃO COM O MYSQL E OPERAÇÕES NO BANCO DE DADOS.

    def __init__(self):
        # INICIALIZA A CONEXÃO AO BANCO DE DADOS USANDO VARIÁVEIS DO .ENV.
        load_dotenv()
        self.config = {
            "host": os.getenv("MYSQL_HOST"),
            "user": os.getenv("MYSQL_USER"),
            "password": os.getenv("MYSQL_PASSWORD"),
            "database": os.getenv("MYSQL_DATABASE"),
        }
        self.conection = None
        self.cursor = None

    def connect(self):
        # ESTABELECE CONEXÃO COM O BANCO DE DADOS.
        try:
            self.conection = mysql.connector.connect(**self.config)
            self.cursor = self.conection.cursor()
            if self.conection.is_connected():
                print("CONECTADO AO MYSQL!")
        except mysql.connector.Error as erro:
            print(f"ERRO AO CONECTAR AO MYSQL: {erro}")

    def close_conection(self):
        # FECHA A CONEXÃO COM O BANCO DE DADOS.
        if self.conection and self.conection.is_connected():
            self.cursor.close()
            self.conection.close()
            print("CONEXÃO ENCERRADA.")

    def execute_comando(self, comando):
        # EXECUTA UM COMANDO SQL NO BANCO DE DADOS.
        try:
            self.connect()
            self.cursor.execute(comando)
            self.conection.commit()
            print("COMANDO EXECUTADO COM SUCESSO!")
        except mysql.connector.Error as erro:
            print(f"ERRO AO EXECUTAR COMANDO SQL: {erro}")
        finally:
            self.close_conection()

    def listar_tabelas(self):
        # LISTA TODAS AS TABELAS DO BANCO DE DADOS.
        try:
            self.connect()
            self.cursor.execute("SHOW TABLES")
            tabelas = self.cursor.fetchall()
            print("TABELAS NO BANCO DE DADOS:")
            for tabela in tabelas:
                print(tabela[0])
        except mysql.connector.Error as erro:
            print(f"ERRO AO LISTAR TABELAS: {erro}")
        finally:
            self.close_conection()
