salas = [
  # 0         1      2       3
  ["Maria", "João", "Ana", "Carlos"], #0
  ["Marcos", "Cintia", "Vitor", "Mariana", "João"], #1
  ["Paulo", "Lucas", ("Joana", "Pedro"), "Maria", "Júlia"] #2
]

print(salas[0][0]) # Maria
print(salas[1][2]) # Vitor
print(salas[2][1]) # Lucas
print(salas[2][2][0], '\n') # Joana

alunos = []
alunoVerifido = []

for sala in salas:
  for aluno in sala:
    if type(aluno) == tuple:
      for a in aluno:
        alunos.append(a)
    else:
      alunos.append(aluno)

print(alunos, '\n')

for aluno in alunos:
  if alunos.count(aluno) > 1:
    if aluno not in alunoVerifido:
      alunoVerifido.append(aluno)
      print(f"Aluno {aluno} está repetido na lista")
