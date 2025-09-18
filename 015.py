'''
Crie uma calculadora que após ler 3 valores, mostre e opere de acordo com as opções:

1.	Somar
2.	Multiplicar
3.	Maior
4.	Novos números
5.	Sair do programa

'''


while True:

    entrada = int(input('Digite o valor que deseja :'
                    '\nPara Somar digite 1: '
                    '\nPara Multiplicar 2: '
                    '\nPara Verificar o Maior 3: '
                    '\nPara Digitar novos números 4: '
                    '\n Para Sair 5: '
                    '----------> '))

    if entrada == 1:
        entrada1 = int(input('Digite o primeiro valor que deseja somar:  '))
        entrada2 = int(input('Digite o segundo Valor: '))
        print(f'Seu resultado é : {entrada1+entrada2}')
    elif entrada == 2:
        entrada1 = int(input('Digite o primeiro valor que deseja multiplicar: '))
        entrada2 = int(input('Digite o Segundo valor: '))
        print(f'Seu resultado é {entrada1*entrada2}')
    elif entrada == 3:
        entrada1 = int(input('Digite o primeiro valor que deseja verificar se maior: '))
        entrada2 = int(input('Digite o segundo valor: '))
        if entrada1 > entrada2:
            print(f'{entrada1} é maior')
        else:
            print(f'{entrada2} é maior')
    elif entrada == 4:(
        entrada) = int(input('Digite o valor que deseja :'
                             '\nPara Somar digite 1: '
                            '\nPara Multiplicar 2: '
                            '\nPara Verificar o Maior 3: '
                            '\nPara Digitar novos números 4: '
                            '\n Para Sair 5: '
                            '----------> '))
    elif entrada == 5:
        break