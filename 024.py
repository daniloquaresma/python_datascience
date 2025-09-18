'''
Usando tuplas, leia um número de 0 a 15, e retorne esse número escrito por extenso
'''

numeros = ('Zero','Um','Dois','três', 'Quatro','Cinco','Seis','Sete',
           'Oito', 'Nove','Dez','Onze','Doze','Treze','Quartoze','Quinze')

try:

    n = int(input('Digite um numero de 0 a 15 para ter o resultado por extenso: '))
    while n < 0  or n > 15:
        print('Tente novamente')
        n = int(input('Digite um numero de 0 a 15 para ter o resultado por extenso: '))
    print(f'O número por extesno é : {numeros[n]}')
except ValueError:
    print('Digite Apenas números')