#Escreva um programa que imprima a tabuada de um número fornecido pelo usuário.
tabuada = int(input("Digite a tabuada que deseja : "))
for contador in range(11):
    conta = contador*tabuada

    print(f'{tabuada}x{contador} = {conta}')