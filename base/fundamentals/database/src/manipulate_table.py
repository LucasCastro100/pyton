from src.conection_mysql import Database

class ManipulateTable:
    # CLASSE PARA EXECUTAR UM COMANDO NO BANCO DE DADOS.
    
    def __init__(self):
        self.db = Database()

    def execute(self, query, params=None):
        # EXECUTA O COMANDO SQL DIGITADO PARA CRIAR UMA TABELA OU INSERIR DADOS.
        try:
            # Se parâmetros forem passados, passa para o execute_comando
            if params:
                self.db.execute_comando(query, params)
            else:
                self.db.execute_comando(query)
            print("EXECUÇÃO REALIZADA COM SUCESSO!")
        except Exception as e:
            print(f"Erro ao executar o comando: {e}")
