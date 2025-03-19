import mysql.connector
import os
from dotenv import load_dotenv

# Carregar variáveis do arquivo .env
load_dotenv()

# Configuração da conexão usando as variáveis do .env
config = {
    "host": os.getenv("MYSQL_HOST"),
    "user": os.getenv("MYSQL_USER"),
    "password": os.getenv("MYSQL_PASSWORD"),
    "database": os.getenv("MYSQL_DATABASE")
}

try:
    # Criando a conexão
    conexao = mysql.connector.connect(**config)
    
    if conexao.is_connected():
        print("Conectado ao MySQL!")

    # Criando um cursor para executar consultas SQL
    cursor = conexao.cursor()

    # Executando um teste (listar tabelas)
    cursor.execute("SHOW TABLES")
    for tabela in cursor.fetchall():
        print(tabela)

except mysql.connector.Error as erro:
    print(f"Erro ao conectar ao MySQL: {erro}")

finally:
    if 'conexao' in locals() and conexao.is_connected():
        cursor.close()
        conexao.close()
        print("Conexão encerrada.")
