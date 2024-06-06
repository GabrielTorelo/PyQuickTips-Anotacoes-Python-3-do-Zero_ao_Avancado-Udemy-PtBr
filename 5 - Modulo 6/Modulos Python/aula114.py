# Importa o módulo collections (usado para manipular coleções)
from collections import deque

# Cria uma fila vazia (deque é uma lista duplamente encadeada)
fila_clientes: deque[str] = deque()

# Adiciona elementos na direita da fila
fila_clientes.append('João')
fila_clientes.append('Maria')
fila_clientes.append('José')

print(f'Fila de clientes (direita): {fila_clientes}')

# Adiciona elementos na esquerda da fila
fila_clientes.appendleft('Pedro')
fila_clientes.appendleft('Ana')
fila_clientes.appendleft('Carlos')

print(f'Fila de clientes (esquerda): {fila_clientes}\n')

# Remove elementos da direita da fila
print(f'Removendo da direita: {fila_clientes.pop()}')

# Remove elementos da esquerda da fila
print(f'Removendo da esquerda: {fila_clientes.popleft()}')

print(f'\nFila de clientes: {fila_clientes}\n')
