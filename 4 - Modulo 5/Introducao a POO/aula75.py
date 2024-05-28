# Criando a classe Meta (metaclasse)
class Meta(type): # Metaclasses herdão do tipo 'type'

  # Método inicializador (cria a classe)
  def __new__(mcs, name, bases, namespace):
    print('Estamos no método __new__ da classe Meta!')

    classe = super().__new__(mcs, name, bases, namespace) # Cria a classe
    classe.var1 = 'var1: Váriavel de classe Meta!' # Adiciona a variável 'var1' à classe

    return classe # Retorna a classe

# Criando a classe Pessoa (baseada na 'metaclasse' Meta)
class Pessoa(metaclass=Meta): # A classe Pessoa herda da 'metaclasse' Meta

  # Método inicializador (cria a instância da classe)
  def __new__(cls, *args, **kwargs):
    print('Estamos no método __new__ da classe Pessoa!')
    
    classe = super().__new__(cls) # Cria a instância da classe
    classe.var2 = f'var2: {*args, kwargs}!' # Adiciona a variável 'var2' à instância da classe

    return classe # Retorna a instância da classe

# Criando uma instância da classe Pessoa, passando o nome e a idade
p1 = Pessoa('Luiz', idade=30)

print('\n')

# Imprimindo as variáveis da classe e da instância
print(p1.var1)
print(p1.var2)