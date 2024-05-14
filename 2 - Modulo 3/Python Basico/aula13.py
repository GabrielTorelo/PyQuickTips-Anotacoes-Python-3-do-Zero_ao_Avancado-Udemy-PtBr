msg_longa = 'Olá, sou uma mensagem muito longa'

# O método capitalize() retorna a string com a primeira letra em maiúscula
print(msg_longa[13:22].capitalize()) # retorna apenas 'mensagem'

# O método upper() retorna a string em maiúscula
print(msg_longa[22:].upper()) # retorna 'MUITO LONGA'

# O método len() retorna o tamanho de uma string
print(len(msg_longa[13:22])) # retorna 9
