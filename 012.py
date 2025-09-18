'''
Escreva um programa que peça ao usuário para adivinhar um número entre 1 e 10
 e continue pedindo até que o usuário acerte o número. E no final,
  retorne também a quantidade de tentativas necessárias.

'''

import random

contador = 0

aleatorio = random.randint(1,11)

adivinhar = int(input('Adivinhe um número de 1 a 10: '))
while adivinhar != aleatorio:
    print('Você errou tente novamente : ')
    contador+= 1
    adivinhar = int(input('Tente novamente : '))
    if adivinhar == aleatorio:
        print(f'Você acertou {aleatorio} ')
        print(f'Quntidade de tentativas : {contador}')