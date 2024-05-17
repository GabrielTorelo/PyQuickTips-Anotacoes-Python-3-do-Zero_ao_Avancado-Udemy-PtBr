def criar_saudacao(saudacao): # Função externa
  def saudar(nome): # Função interna
    return f'{saudacao}, {nome}!' # Retorna a saudação com o nome
  return saudar # Retorna a função interna

falar_bom_dia = criar_saudacao('Bom dia') # Cria a função falar_bom_dia
falar_boa_tarde = criar_saudacao('Boa tarde') # Cria a função falar_boa_tarde

print(falar_bom_dia('João')) # Chama a função falar_bom_dia, passando o nome João
print(falar_boa_tarde('Maria')) # Chama a função falar_boa_tarde, passando o nome Maria

# --------------------------------------------

print('\n')

# --------------------------------------------

def multiplicador(fator): # Função externa
  def multiplica(numero): # Função interna
    return numero * fator # Retorna o número multiplicado pelo fator
  return multiplica # Retorna a função interna

duplica = multiplicador(2) # Cria a função duplica
triplica = multiplicador(3) # Cria a função triplica

print(duplica(5)) # Chama a função duplica, passando o número 5 e retornando 10
print(triplica(5), '\n') # Chama a função triplica, passando o número 5 e retornando 15

for i in range(1, 3): # Para i de 1 a 5
  print(f'Duplica {i}: ', duplica(i)) # Chama a função duplica, passando o número i e retornando o dobro
  print(f'Triplica {i}: ', triplica(i)) # Chama a função triplica, passando o número i e retornando o triplo
