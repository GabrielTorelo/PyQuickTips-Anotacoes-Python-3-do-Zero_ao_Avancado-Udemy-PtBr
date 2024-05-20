quadrados = [n**2 for n in range(1, 11)]

print(quadrados)

# --------------------------------------------

print('\n')

# --------------------------------------------

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros_pares = [n for n in numeros if n % 2 == 0]

print(numeros_pares)

# --------------------------------------------

print('\n')

# --------------------------------------------

palavras = ['python', 'javascript', 'java', 'c', 'c++', 'c#']

letras_maiusculas = [palavra.upper() for palavra in palavras]

print(letras_maiusculas)

# --------------------------------------------

print('\n')

# --------------------------------------------

numeros_impares = [n for n in range(1, 21) if n % 2 != 0 and n % 3 != 0]

print(numeros_impares)
