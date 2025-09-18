'''
Escreva um programa que peça ao usuário uma letra e imprima se é uma vogal ou consoante.
'''

letra = input('Digite uma Letra: ').strip().lower()[0]
vogal = ['á','ã','À','à','ã','a','È','é','è','È','i','o','u']
if letra in vogal:
    print('É uma vogal!')
else:
    print('É uma consoante!')