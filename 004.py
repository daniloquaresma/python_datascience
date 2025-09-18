'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
1 O nome com todas as letras maiúsculas
2 O nome com todas minúsculas
3 Quantas letras ao todo (sem considerar os espaços)
4 Quantas letras tem o primeiro nome

'''


nome = input('Digite seu Nome completo: '). strip()
nome_sem_espaco = nome.replace(' ','')
primeiro_nome =  nome[0:nome.find(' ')]
quant_letras_1_nome = len(primeiro_nome)
print(nome.upper())
print(nome.strip())
print(len(nome_sem_espaco))
print(primeiro_nome)

