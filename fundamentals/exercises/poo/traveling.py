'''
Desenvolva um mini cadastro de viagem que tenha os seguintes requisitos:

- Usuário deve informar o seu nome para cadastrar uma viagem.

- Usuário deve selecionar um destino com base nas instâncias de objetos da classe viagem.

- Deve ser apresentado uma mensagem indicando que o a cadastro da viagem no destino específico foi feito com sucesso.
'''

class Trip:
    def __init__(self, destiny):
        self.destiny = destiny