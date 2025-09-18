'''
Faça um programa que leia o nome e o QI de várias pessoas, guardando tudo e uma lista. No final mostre:

1 Quantas pessoas foram cadastradas
2 Uma listagem com as pessoas com o maior QI
3 Uma listagem com as pessoas de menor QI

'''

pessoas = [[],[]]

while True:
    nome = input('Digite seu nome ou S para sair : ')
    if nome == 's':
        break

    pessoas[0].append(nome)
    pessoas[1].append(int(input('Digite Seu Qi: ')))

    print(f'A quantidade de pessoas registradas é : {len(pessoas[0])}')

    maiores_qis = sorted(pessoas[1], reverse=True)
    menores_qis = sorted(pessoas[1])

    print(f'Os maiores Qis são : {sorted(pessoas[1],reverse=True)}')
    for i in maiores_qis:
        print(pessoas[0][pessoas[1].index(i)])

    print(f'Os menores Qis são : {sorted(pessoas[1])}')
    for i in menores_qis:
        print(pessoas[0][pessoas[1].index(i)])