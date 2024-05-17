pessoas = {} # Cria um dicionário vazio

# Adiciona um dicionário (Alice) ao dicionário pessoas
pessoas['Carol'] = {
  'telefone': '5678-1234',
  'email': 'carol@gmail.com'
}

# Adiciona outro dicionário (Marcos) ao dicionário pessoas
pessoas['Marcos'] = {
  'telefone': '8765-4321',
  'email': 'marcos@gmail.com'
}

print(len(pessoas)) # Imprime o número de itens no dicionário

print('\n', pessoas.keys()) # Imprime as chaves do dicionário
print(tuple(pessoas.keys())) # Imprime as chaves do dicionário como uma tupla

print('\n', pessoas.values()) # Imprime os valores do dicionário
print(list(pessoas.values())) # Imprime os valores do dicionário como uma lista

print('\n', pessoas.items()) # Imprime os itens do dicionário
print(list(pessoas.items())) # Imprime os itens do dicionário como uma lista

# Adiciona um dicionário padrão ao dicionário pessoas
pessoas.setdefault('Null', {'telefone': '0000-0000', 'email': 'null@null.com'})

print('\n', pessoas, '\n') # Imprime o dicionário completo

if pessoas.get('Marlon') is None: # Verifica se a chave 'Marlon' não existe no dicionário
  print('Null: ', pessoas['Null']) # Imprime o valor associado à chave 'Null'
