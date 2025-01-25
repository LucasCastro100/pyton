'''
DICIONARIOS SAO OBJETOS QUE POSEUM CHAVES E VALORES
'''

# EM VALOR UNICO NO DICIONARIO VOCE USA {}
filme = {
    'titulo': 'Star Wars',
    'ano': 1977,
    'diretor': 'George Lucas'
}

# MAIS DE UM VALOR O DICIONARIO TEM QUE USAR [] E {}
filmes = [
    {
        'titulo': 'Star Wars',
        'ano': 1977,
        'diretor': 'George Lucas'
    },
    {
        'titulo': 'Indiana Jones',
        'ano': 1981,
        'diretor': 'Steven Spielberg'
    },
    {
        'titulo': 'Harry Potter',
        'ano': 2001,
        'diretor': 'Chris Columbus'
    },
    {
        'titulo': 'Senhor dos Anéis',
        'ano': 2001,
        'diretor': 'Peter Jackson'
    }
]

# ACESSANDO UM ITEM DO DICIONARIO
print(filme['titulo']) 
print(filmes[1]['titulo'])

# ACESSANDO UM ITEM DO DICIONARIO COM GET
print(filmes[2].get('titulo'))

# BUSCANDO AS CHAVES DO DICIONARIO
print(filmes[0].keys())

# BUSCANDO OS VALORES DO DICIONARIO
print(filmes[0].values())

# BUSCANDO OS ITENS DO DICIONARIO
print(filmes[0].items())

# ADICIONANDO UM ITEM NO DICIONARIO
filmes[0]['genero'] = 'Ficção Científica'

# ATUALIZANDO UM ITEM DO DICIONARIO
filmes[0].update({'titulo': 'Star Wars: Uma Nova Esperança'})

# REMOVENDO UM ITEM DO DICIONARIO
del filmes[0]['genero']
filmes[0].pop('genero')

# EXCLUINDO O DICIONARIO
del filmes[0]