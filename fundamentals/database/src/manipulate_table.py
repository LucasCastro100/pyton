from conection_mysql import Database

class ManipulateTable:
    # CLASSE PARA EXECUTAR UM COMANDO NO BANCO DE DADOS.

    def __init__(self):
        self.db = Database()

    def execute(self, comando_sql):
        # EXECUTA O COMANDO SQL DIGITADO PARA CRIAR UMA TABELA.
        self.db.execute_comando(comando_sql)
        print("EXECUÇÃO REALIZADA COM SUCESSO!")