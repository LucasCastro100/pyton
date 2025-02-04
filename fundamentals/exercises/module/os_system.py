'''
Crie duas funções em python para agendar o desligamento do computador em uma hora e meia hora.
'''

import os

# DESLIGANDO O COMPUTADOR
# os.system('shutdown /s /t 0') DESLIGA IMEDIATAMENTE

# CANCELANDO O DESLIGAMENTO
# os.system('shutdown /a')


def schedule_shutdown():
    os.system('shutdown /s /t 5400')
    
def schedule_cancel_shutdown():
    os.system('shutdown /a')

    
schedule_shutdown()
schedule_cancel_shutdown()   