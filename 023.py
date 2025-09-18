'''
Crie uma tupla preenchida com os 10 filmes mais assistidos de todos os tempos, e depois mostre:

1 Apenas os 3 primeiros mais assistidos
2 Os últimos 2 mais assistidos
3 A lista em ordem alfabética
4 Em que posição está “O rei leão”

'''

filmes =  ('Maquina Mortifera', 'O Rei Leão', 'Avatar',
           'Batman O Cavaleiro das Trevas','V de Vingança ', 'Vingadores','Homem aranha',
           'Wolverine', 'O Poderoso chefão', 'Avatar 2')

print(filmes[0:3])
print(filmes[-2:])
print(sorted(filmes))
print(filmes.index('O Rei Leão')+ 1 )