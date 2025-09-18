'''
Crie um programa para jogar JOKEMPO, usando a função random.randint


'''
import random

pedra = 1
papel = 2
tesoura = 3

aleatoria = random.randint(1,3)

escolha = input('Digite uma opção: '
                '\n1. - para Pedra '
                '\n2. Para Papel '
                '\n3. Para Tesoura -------> ')
if escolha == 1 and aleatoria == 3 or escolha == 2 and aleatoria == 1 or escolha == 3 and aleatoria == 2:
    print(f'Você vencel!{escolha}X{aleatoria}')
elif escolha == aleatoria:
    print('Empate')
else:
    print(f'Você perdeu {escolha}X{aleatoria}')