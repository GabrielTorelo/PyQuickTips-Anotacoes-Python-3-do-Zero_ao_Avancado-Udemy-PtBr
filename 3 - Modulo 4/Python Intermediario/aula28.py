# --------------------------------------------
# ----------------- Métodos ------------------
# --------------------------------------------

lista_frutas = ['banana', 'maçã', 'banana', 'tangerina']

frutas = set(lista_frutas)

print(frutas) # Retorna 'maçã', 'tangerina' e 'banana'

# --------------------------------------------

frutas.add('abacaxi')

print(frutas) # Retorna 'abacaxi', 'maçã', 'tangerina' e 'banana'

# --------------------------------------------

novas_frutas = ['acerola', 'abacate']

frutas.update(novas_frutas)

print(frutas) # Retorna 'abacaxi', 'banana', 'maçã', 'tangerina', 'abacate' e 'acerola'

# --------------------------------------------

frutas.remove('banana')

print(frutas) # Retorna 'abacaxi', 'maçã', 'tangerina', 'abacate' e 'acerola'

# --------------------------------------------

frutas.clear()

print(frutas) # Retorna um conjunto vazio

# --------------------------------------------

frutas = set(lista_frutas)

frutas.discard('maçã')
frutas.discard('maçã')

print(frutas) # Retorna 'tangerina' e 'banana'

# --------------------------------------------
# ---------------- Operadores ----------------
# --------------------------------------------

outras_frutas = ['açaí', 'amora', 'banana']

uniao_frutas = frutas.union(outras_frutas)

print(uniao_frutas) # Retorna 'açaí', 'tangerina', 'banana' e 'amora'

# --------------------------------------------

insercao_frutas = frutas.intersection(outras_frutas)

print(insercao_frutas) # Retorna 'banana'

# --------------------------------------------

outras_frutas = set(outras_frutas)

diferenca_frutas_1 = frutas.difference(outras_frutas)
diferenca_frutas_2 = outras_frutas.difference(frutas)

print(diferenca_frutas_1) # Retorna 'tangerina', 
print(diferenca_frutas_2) # Retorna 'açaí' e 'amora' 

# --------------------------------------------

diferenca_simetrica_frutas = frutas.symmetric_difference(outras_frutas)

print(diferenca_simetrica_frutas) # Retorna 'açaí', 'tangerina' e 'amora'
