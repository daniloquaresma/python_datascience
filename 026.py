'''
Escreva um programa que crie uma lista vazia e permita que o usuário insira números nessa lista até que ele digite
 um número negativo. Em seguida, exiba a lista na tela.
'''

lista =  []

while True:
    try:
        n = int(input('Numero negativo para sair ; '))
        if n < 0:
            break
        lista.append(n)
    except ValueError:
        print("Aceitomos só numeros")
print(f' A lista é {lista} ')        