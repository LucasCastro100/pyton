# IP CONFIG DE HOJE IPVA => 10.6.128.49
# PARA ACESSAR UM ENDEREÇO LOCAL => python -m http.server
# PARA ABRIR O LINK LOCAL E O ENDEREÇO IPV4:8000

import webbrowser

done = False

while not done:    
    print('='*50)
    print('OQUE VOCÊ DESEJA FAZER \n')
    print('1 => APRENDER PYTHON')
    print('2 => APRENDER SOBRE MODULOS')
    print('3 => SAIR')
    
    chose = int(input('> '))
    
    if chose == 1:
        webbrowser.open("http://python.org")
    elif chose == 2:
        webbrowser.open("http://docs.python.org/3/py-modindex.html")
    elif chose == 3:
        done = True
    else:
        print("Opção inválida, digite uma opção entre 1 e 3: ")
        

    