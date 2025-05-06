# Dicionário de letras para morse
text_to_morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', ' ': '/'
}

# Dicionário de morse para letras
morse_to_text = {v: k for k, v in text_to_morse.items()}

def texto_para_morse(texto):
    texto = texto.upper()
    return ' '.join(text_to_morse.get(char, '?') for char in texto)

def morse_para_texto(morse):
    palavras = morse.strip().split(' / ')
    traduzido = []
    for palavra in palavras:
        letras = palavra.split()
        traduzido.append(''.join(morse_to_text.get(letra, '?') for letra in letras))
    return ' '.join(traduzido)

entrada = input("Digite o texto ou código morse: ")

# Se o usuário digitar apenas . ou -, assumimos que é morse
if set(entrada.strip()) <= {'.', '-', ' ', '/'}:
    resultado = morse_para_texto(entrada)
    print("Texto traduzido:", resultado)
else:
    resultado = texto_para_morse(entrada)
    print("Código Morse:", resultado)   

