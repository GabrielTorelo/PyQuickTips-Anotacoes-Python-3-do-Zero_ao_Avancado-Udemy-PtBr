"""
  Faça um jogo para o usuário adivinhar qual
  a palavra secreta.

  * Você vai propor uma palavra secreta
  qualquer e vai dar a possibilidade para
  o usuário digitar apenas uma letra.
  * Quando o usuário digitar uma letra, você 
  vai conferir se a letra digitada está
  na palavra secreta.
    * Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    * Se a letra digitada não estiver
    na palavra secreta; exiba *.

  Faça a contagem de tentativas do seu
  usuário.
"""

palavra_secreta = "python"
letras_acertadas = ['_'] * len(palavra_secreta)
i = 0

while True:
  i += 1
  letra = input(f"{i}ª tentativa - Digite uma letra: ")

  if len(letra) > 1:
    print('Digite apenas 1 letra!\n')
    continue

  if letra in palavra_secreta:
    for indice, caract in enumerate(palavra_secreta):
      if caract == letra:
        letras_acertadas[indice] = letra
    print(''.join(letras_acertadas))

  if ''.join(letras_acertadas) == palavra_secreta:
    print(f'\nVocê acertou em {i} tentativa(s)!')
    break
