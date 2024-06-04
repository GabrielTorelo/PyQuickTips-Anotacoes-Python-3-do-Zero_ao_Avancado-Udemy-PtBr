from secrets import SystemRandom, randbelow, token_hex

# Gerar um token hexadecimal de 16 bytes
token_hexadecimal = token_hex(16)

print(f'Token hexadecimal: {token_hexadecimal}')

# Criar um objeto de sistema aleatório
random = SystemRandom()

# Gerar uma senha aleatória de 10 caracteres
senha = ''.join(random.choices('TeStEdEsEnHa$@123456789*', k=10))

print(f'Senha aleatória: {senha}')

# Gerar um número aleatório entre 0 e 1010
menor_1010 = randbelow(1010)

print(f'Número aleatório entre 0 e 1010: {menor_1010}')

# Criar uma lista de nomes
lista_nomes = ['João', 'Paulo', 'Luiz', 'Lucas']

# Selecionar um nome aleatório da lista
seleciona_nome = random.choice(lista_nomes)

print(f'Nome aleatório: {seleciona_nome}')
