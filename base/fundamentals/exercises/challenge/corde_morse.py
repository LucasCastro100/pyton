'''
Crie um programa que decodifique mensagens em código morse.
'''

list_code_morse = {
    '.-': 'A',
    '-...': 'B',
    '-.-.': 'C',
    '-..': 'D',
    '.': 'E',
    '..-.': 'F',
    '--.': 'G',
    '....': 'H',
    '..': 'I',
    '.---': 'J',
    '-.-': 'K',
    '.-..': 'L',
    '--': 'M',
    '-.': 'N',
    '---': 'O',
    '.--.': 'P',
    '--.-': 'Q',
    '.-.': 'R',
    '...': 'S',
    '-': 'T',
    '..-': 'U',
    '...-': 'V',
    '.--': 'W',
    '-..-': 'X',
    '-.--': 'Y',
    '--..': 'Z'
}

def decode_morse(morse_message):
    # QUEBRANDO A MENSAGEM EM PALAVRAS
    words = morse_message.split(' / ')
    decoded_message = []

    for word in words:
        # SEPARANDO AS LETRAS DE CADA PALAVRA
        letters = word.split()
        
        # CONCATENANDO CADA LETRA
        decoded_word = ''.join(list_code_morse[letter] for letter in letters)
        
        # ADICIONANDO A LETRA DECODIFICADA À MENSAGEM
        decoded_message.append(decoded_word)

    # MENSAGEM DECODIFICADA REVERTIDA
    reversed_message = ' '.join(word[::-1] for word in decoded_message)
    
    # MENSAGEM DECODIFICADA NORMAL
    normal_message = ' '.join(decoded_message)
        
    return normal_message

morse_message = input('Digite a mensagem em código morse: ')
decoded_message = decode_morse(morse_message)
print(decoded_message)