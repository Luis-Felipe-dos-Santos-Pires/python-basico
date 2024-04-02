
# As variáveis em python são fracamente tipadas:
a = 1
print(a)
a = "TESTE"
print(a)

## Se for necessário explicitar a tipagem:
a = int(1)
print(a)
a = str("TESTE")
print(a)


## As variáveis são case sensitive:
a = 1
A = "TESTE"
print("a: ",a)
print("A: ",A)


## Strings podem ser declaradas com aspas simples ou duplas:
a = "TESTE"
# é o mesmo que
a = 'TESTE'
print(a)


# Setando múltiplos valores

# Multiplos valores para múltiplas variáveis
x, y, z = "TESTE", "ABC", "DEF"
print(x)
print(y)
print(z)

# Um valor para múltiplas variáveis
x = y = z = "TESTE"
#y = "MUDOU"
print(x)
print(y)
print(z)


# Desempacotando uma collection
carros = ["Uno","Gol","Celta"]
x ,y, z = carros
print(x)
print(y)
print(z)

# Escopo de variáveis
x = "global"
print(x)

def myfunc():
  #global x
  x = "local"
  print("The variable x is " + x)

myfunc()
print(x)
