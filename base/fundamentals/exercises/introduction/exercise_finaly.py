'''
Escreva um programa em python que realize o gerenciamento de jogadores. Ele deve atender aos seguintes requisitos:

Adicionar um time

Remover um time

Listar times

Adicionar jogador em um time

Remover jogador de um time

Listar jogadores de um time

A opção de adicionar um time deve pedir um nome para o time que será cadastrado.

A opção de remover um time deve pedir o índice específico do time que foi cadastrado para fazer a sua exclusão.

A opção de listar os times deve mostrar o índice, o nome e a quantidade de jogadores do time.

A opção de adicionar um jogador em um time deve pedir um índice do time que foi cadastrado e associar com o nome do jogador que será adicionado.

A opção de remover um jogador em um time deve pedir um índice do time que foi cadastrado e utilizar esse índice para remover o jogador que fora cadastrado no time.

A opção de listar os jogadores de um time deve ser informado o índice de um time e listar os jogadores que foram associados a ele.

Este é o exercício de revisão do módulo, então aproveite para utilizar todos os recursos vistos até agora, como os funções, condições, loop, listas, etc.
'''

teams = []
option = 0

def insertTeam(name):
    teams.append({'name': name, 'players': []})

def deleteTeam(index):
    if 0 <= index < len(teams):
        teams.pop(index)

def listTeams():
    for index, team in enumerate(teams):
        print(f"{index + 1} - {team['name']} possui {len(team['players'])} jogadores")

def insertPlayerOnTeam(index, player_name):
    if 0 <= index < len(teams):
        teams[index]['players'].append(player_name)

def deletePlayerOnTeam(index, player_name):
    if 0 <= index < len(teams):
        if player_name in teams[index]['players']:
            teams[index]['players'].remove(player_name)

def listPlayersOnTeam(index):
    if 0 <= index < len(teams):
        print(f"Jogadores do time {teams[index]['name']}:")
        for i, player in enumerate(teams[index]['players']):
            print(f"{i + 1}. {player}")

while option != 7:
    print("="*50)
    print("ESCOLHA UMA OPÇÃO")
    print("1 => ADICIONAR UM TIME;")
    print("2 => REMOVER UM TIME;")
    print("3 => LISTAR OS TIMES;")
    print("4 => ADICIONAR JOGADOR A UM TIME;")
    print("5 => REMOVER JOGADOR DE UM TIME;")
    print("6 => LISTAR JOGADORES DE UM TIME;")
    print("7 => SAIR")
    print("="*50)
    
    option = int(input('ESCOLHA UMA OPÇÃO: '))
    
    if option == 1:
        name = input('Nome do time: ')
        insertTeam(name)
    elif option == 2:
        index = int(input('Índice do time: ')) - 1
        deleteTeam(index)
    elif option == 3:
        listTeams()
    elif option == 4:
        index = int(input('Índice do time: ')) - 1
        player_name = input('Nome do jogador: ')
        insertPlayerOnTeam(index, player_name)
    elif option == 5:
        index = int(input('Índice do time: ')) - 1
        player_name = input('Nome do jogador: ')
        deletePlayerOnTeam(index, player_name)
    elif option == 6:
        index = int(input('Índice do time: ')) - 1
        listPlayersOnTeam(index)
    elif option == 7:
        print("Saindo...")
    else:
        print("Opção inválida!")
 