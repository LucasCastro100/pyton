'''
Substituindo caractere repetido

Escreva um programa Python para obter uma string de uma determinada string em que todas as ocorrências de seu primeiro caractere foram alteradas para '$', exceto o próprio primeiro caractere
'''
input_string = input('Digite uma palavra: ')
input_letter = input('Digite uma letra para ser substituída: ')
input_change = input('Digite o caractere para substituir: ')

first_occurrence_index = input_string.find(input_letter)
if first_occurrence_index == -1:
    modified_string = input_string  # Retorna a string original se o caractere não for encontrado
else:
    # Substitui todas as ocorrências do caractere por "change", exceto a primeira ocorrência
    modified_string = input_string[:first_occurrence_index + 1] + input_string[first_occurrence_index + 1:].replace(input_letter, input_change)

print(modified_string)

'''
Substituindo caractere repetido

Escreva um programa Python para obter uma única string de duas strings fornecidas, separadas por um espaço e troque os dois primeiros caracteres de cada string.
'''

string1 = input('Digite a primeira palavra: ')
string2 = input('Digite a segunda palavra: ')

new_str1 = string2[0] + string1[1:]
new_str2 = string1[0] + string2[1:]

result = new_str1 + ' ' + new_str2

print(result)