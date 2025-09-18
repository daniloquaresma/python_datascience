'''
Escreva um programa que leia um número n inteiro qualquer
 e mostra na tela os n primeiros elementos de uma Sequência de Fibonacci


'''

i = 0
prox = 0
ant = 1
atual = 1

numero = int(input('Digite quantos números deseja ver : '))
while i < numero:
    if i == 0:
        print('0')
    elif i == 1:
        print('1')
    elif i == 2:
        print('1')
    else:
        prox = ant + atual
        ant = atual
        atual = prox
        print(prox)
    i += 1