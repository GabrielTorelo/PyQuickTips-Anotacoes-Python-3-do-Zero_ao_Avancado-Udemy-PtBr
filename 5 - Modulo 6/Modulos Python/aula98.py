# Importa o módulo random (usado para gerar números aleatórios)
from random import randint, randrange, choice, shuffle, random, uniform, sample

# Gera um número aleatório entre 1 e 10
numero_aleatorio = randint(1, 10)

print(f'Número inteiro aleatório: {numero_aleatorio}')

# Gera um número aleatório entre 2 e 10, pulando de 2 em 2
numero_aleatorio_2_2 = randrange(2, 10, 2)

print(f'Número inteiro aleatório (2 em 2): {numero_aleatorio_2_2}')

# Cria uma lista de frutas
lista = ['maçã', 'banana', 'cereja']

# Escolhe uma fruta aleatória da lista
fruta_aleatoria = choice(lista)

print(f'Fruta aleatória: {fruta_aleatoria}')

# Cria uma lista de números
lista = [1, 2, 3, 4, 5]

# Embaralha a lista
shuffle(lista)

print(f'Lista embaralhada: {lista}')

# Gera um número de ponto flutuante aleatório entre 0 e 1
numero_flutuante = random()

print(f'Número flutuante aleatório: {numero_flutuante}')

# Gera um número de ponto flutuante aleatório entre 1 e 10
numero_flutuante_1_10 = uniform(1, 10)

print(f'Número flutuante aleatório: {numero_flutuante_1_10}')

# Cria uma lista de nomes
nomes = ['Ana', 'João', 'Maria']

# Escolhe 2 nomes aleatórios da lista
nomes_aleatorios = sample(nomes, 2)

print(f'Nomes aleatórios: {nomes_aleatorios}')
