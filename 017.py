'''
Crie um programa que retorne a tabuada de um número, e só pare quando o número digitado for 0000

'''
while True:
    tabuada = input("Digite a tabuada que deseja : ")
    if tabuada == '000':
        break
    for contador in range(11):
        conta = contador* int(tabuada)
        print(f'{tabuada}x{contador} = {conta}')