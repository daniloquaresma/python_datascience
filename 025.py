'''
Escreva um programa que crie uma lista com varios números lidos pelo usuário,
em seguida, exiba apenas os números ímpares da lista.
'''

numero = []

while True:
    try:
        n = input('Digite o número que deseja ou [S] para sair : ').lower()
        if n == 's':
            break
        numero.append(int(n))
    except ValueError:
        print('Digite apenas números!')

for i in numero:
    if i % 2 != 0:
        print(f'Os números impares são : {i}', end= ' ')