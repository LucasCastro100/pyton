import re

text = "Python é a linguagem legal, e estou focado e decidido que vou mudar de carreira com ela!"

# INDICE INICIAL E FINAL DE PALAVRAS
# O r significa que estamos trabalhando com uma string bruta (raw string)

match = re.search(r'focado e decidido', text)
print(f"Indice Inicial: {match.start()}")
print(f"Indice Inicial: {match.end()}")

# BUSCANDO O INDICE QUE POSSUI O PONTO (com isso preciso passar a \ junto com o ponto apra que ela possa buscar)
url = 'https://ideias.dev.br'
match = re.search(r'\.', url)
print(match)

# BUSCANDO UMA LISTA DE CARACTERES DENTRO DE UMA FRASE
pattern = "[a-m]"
result = re.findall(pattern, text)
print(text)
print(result)

# VERIFICANDO O INICIO DE UMA STRING
rule = r"^A" # iniciio com  a letra A 
phrases = ['A casa esta suja!', 'O dia esta lindo!', 'A escola esta sempre uma bagunça!', 'O Lucas e legal!']

for f in phrases:
    if re.match(rule, f):
        print(f"Correspondente: {f}")
    else:
        print(f"Não correspondente: {f}")
        
# VERIFICANDO O FINAL DE UMA STRING
rule_end = r"!$" # final com !
phrases_end = ['A casa esta suja?', 'O dia esta lindo?', 'A escola esta sempre uma bagunça!', 'O Lucas e legal!']

for f_end in phrases_end:
    if re.search(rule_end, f_end):
        print(f"Correspondente: {f_end}")
    else:
        print(f"Não correspondente: {f_end}")