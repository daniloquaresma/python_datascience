'''
Crie um programa que leia uma frase e mostre:
Quantas vezes aparece a letra “a”
Em que posição ela aparece a primeira vez
Em que posição ela aparece na última vez


'''

frase = input('Digite Uma frase: ').strip().lower()
frase = frase.replace('á','a')
frase = frase.replace('À','a')
frase = frase.replace('à','a')
frase = frase.replace('ã','a')

print(f'Quantidade de as: {frase.count('a')}'
      f'\nPrimeiro a: {frase.find('a')+  1 } '
      f'Ultimo a: {frase.rfind('a') + 1 }')


