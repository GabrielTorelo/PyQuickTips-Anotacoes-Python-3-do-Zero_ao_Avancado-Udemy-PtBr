frase = 'Esta é uma frase de exemplo'
palavras = frase.split()
print(palavras)

# --------------------------------------------

texto_com_espacos = '    Olá, mundo!    '
texto_sem_espacos = texto_com_espacos.strip()
print(texto_sem_espacos)

# --------------------------------------------

palavras = ["Esta", "é", "uma", "frase", "de", "exemplo"]
frase = " ".join(palavras)
print(frase)
