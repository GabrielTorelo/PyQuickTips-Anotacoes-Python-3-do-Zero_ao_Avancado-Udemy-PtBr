# Função para formatar o tamanho de um arquivo em bytes para KB, MB, GB, TB, PB, EB, ZB, YB
def formata_tamanho(tamanho_em_bytes: int, base: int = 1024) -> str:
  # Unidades de medida de bytes
  unidades = ["B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"]

  # Se o tamanho for 0, retorna "0B"
  if tamanho_em_bytes == 0:
    return "0B"
  
  # Percorre as unidades de medida e retorna o tamanho formatado
  for unidade in unidades:

    if tamanho_em_bytes < base: # Se o tamanho for menor que a base, retorna o tamanho formatado
      return f"{tamanho_em_bytes:.2f}{unidade}"
    
    tamanho_em_bytes /= base # Divide o tamanho pela base

print(formata_tamanho(5000))
print(formata_tamanho(50000))
print(formata_tamanho(500000))
print(formata_tamanho(5000000))
