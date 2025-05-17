import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.operations import CreateTable, AlterTable, DropTable, InsertTable

query_create_table_users = """
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    telefone VARCHAR(20),
    email VARCHAR(255) UNIQUE NOT NULL
);
"""
CreateTable(query_create_table_users).execute()

nome = input("Digite o nome: ")
telefone = input("Digite o telefone: ")
email = input("Digite o email: ")

InsertTable("usuarios", ["nome", "telefone", "email"], [nome, telefone, email]).execute()