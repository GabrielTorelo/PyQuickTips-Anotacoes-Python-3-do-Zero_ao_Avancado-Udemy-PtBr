lista = [
    {'nome': 'Luiz', 'sobrenome': 'Miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

def exibeLista(lista):
  for i in lista:
    print(i['nome'], i['sobrenome'])

l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibeLista(l1)
print()
exibeLista(l2)

# --------------------------------------------

print('\n')

# --------------------------------------------

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))

print(numeros_pares)

numeros_ao_quadrado = list(map(lambda x: x ** 2, numeros))

print(numeros_ao_quadrado)
