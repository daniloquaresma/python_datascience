'''
Faça um programa que leia um número e retorne o fatorial !

4! = 4 x 3 x 2 x 1

'''

fatorial = 1
contador = 0

numero = int(input('Digite o fatorial que deseja : '))
if numero  == 0:
    print('Digite um número valido!')
    numero = int(input('Digite o fatorial que deseja : '))
while numero > 1:
    fatorial = fatorial * numero
    numero -= 1
    print(f'O Fatorial é {contador+1} x {fatorial}')
    contador+= 1
