# Cria uma função 'fatorial' que calcula o fatorial de um número 'n' passado como argumento
def fatorial(n: int) -> int:
  if n == 0: # Usado para parar a recursão
    return 1
  
   # Realiza uma chamada recursiva da função 'fatorial', passando o valor de 'n - 1' como argumento
  return n * fatorial(n - 1)

print(fatorial(5)) # Calcula o fatorial de 5
