# Importa a função calendar do módulo calendar (usado para manipular calendários)
from calendar import calendar, day_name, isleap, month, monthrange, FRIDAY, weekday

print(calendar(2024)) # Imprime o calendário do ano de 2024

print("\n")

print(month(2024, 5)) # Imprime o calendário do mês de maio de 2024

print("\n")

# Imprime o último dia do mês
print(monthrange(2024, 5)[1]) # O índice 1 do retorno da função monthrange é o último dia do mês

print("\n")

# Imprime o dia da semana em que o mês de maio de 2024 começa e a quantidade de dias que ele tem
print(monthrange(2024, 5))

print("\n")

# Conta a quantidade de sextas-feiras no mês de maio de 2024
qtd_sextas = month(2024, 5).count(str(FRIDAY))
print(f"O mês de maio de 2024 tem {qtd_sextas} sextas-feiras.")

print("\n")

dia_um_maio = weekday(2024, 5, 1) # Obtém o numero do dia da semana
dia_semana = day_name[dia_um_maio] # Obtém o nome do dia da semana

print(f"O dia 1 de maio de 2024 cai em um(a) {dia_semana}.")

print("\n")

eh_bissexto = isleap(2024) # Verifica se o ano é bissexto
print(f"O ano de 2024 é bissexto? {eh_bissexto}")
