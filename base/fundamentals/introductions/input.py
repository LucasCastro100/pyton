'''
UTILIZANDO INPUT E FAZENDO UM PROGRAMA QUE PEDE NOME E DATA DE NASCIMENTO DO USUAROI E MOSTRA A IDADE DELE,
COM ISSO USAREMOS O DATETIME
'''

from datetime import datetime

name = input('Digite seu nome: ')
date_of_birth = input('Digite sua data de  nascimento (formato DD/MM/AAAA): ')

date_current = datetime.now() # Pega a data atual
date_birth = datetime.strptime(date_of_birth, "%d/%m/%Y") # Converte a string para um objeto datetime
age = date_current.year - date_birth.year # Pega o ano atual e subtrai pelo ano de nascimento

# Ajustar caso o aniversário ainda não tenha ocorrido neste ano
if (date_current.month, date_current.day) < (date_birth.month, date_birth.day):
    age -= 1

print(f'Olá {name} você tem {age} anos!')

'''
NO INPUT PODEMOS CONVERTER O TIPO DE DADO QUE O USUÁRIO DIGITOU, POR EXEMPLO:
name = input('Digite seu nome: ')
age = int(input('Digite sua idade: '))
height = float(input('Digite sua altura: '))
gay = bool(input('Você e Hetero')) # Não é comum, mas é possível converter para booleano
'''