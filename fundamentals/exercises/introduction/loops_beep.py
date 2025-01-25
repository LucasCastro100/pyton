'''
Faça um programa para escrever a contagem regressiva do lançamento de um foguete. O programa deve imprimir 10, 9, 8, …, 1, 0 e disparar um “beep”.
'''
import winsound #para fazer o beep

x = 10
while x >= 0:
    print(x)
    x -= 1
winsound.Beep(2500, 500)

'''
Faça um programa que calcule a tabuada de um número, com valores iniciais e finais informados pelo usuário
'''

number = int(input("Tabuada do: "))
start = int(input("De: "))
end = int(input("Até: "))

# O END + 1, REPERESENTA COMO SE FOSSE RANGE(1, 21) AI VAI DO 1 AO 20 E NÃO DO 0 AO 19
for i in range(start, end+1):
    print(f"{number} x {i} = {number * i}")
    
    