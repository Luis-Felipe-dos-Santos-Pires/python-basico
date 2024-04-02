# São definidas com a palavra reservada def
def funcaoteste():
    pass
"""
# Por padrão, uma função precisa ser chamada com o número correto de argumentos:
def numeroCorretoArgs(x,y):
    print(x,y)
numeroCorretoArgs("a","b")


# Podemos modificar isso colocar um * na frente do nome do parâmetro, assim a função pode receber múltiplos argumentos em uma tupla
# Porém, continuará dando erro ao tentar utilizar um argumento que não exista
def argumentosTupla(*x):
    print(len(x))
    print(x)

argumentosTupla("a","b","c","d","e","f")

# É possível definir o argumento pelo nome e não pela ordem
def namedArgs(child3, child2, child1):
  print("The youngest child is " + child3)
namedArgs(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


# Colocando ** na frente do nome do parâmetro, assim a função pode receber múltiplos argumentos em um dictionary
# OBS: os argumentos precisam ser nomeados
def argumentosDict(**x):
    print(x)
argumentosDict(a = "TESTE", v = "TESTE1")


## Utilizando pass, irá evitar um erro na função
def passExemplo():
    pass
passExemplo()


# lambda
b = lambda arg, arg2: arg + arg2
print(b(5,10))


# map
a = [1,2,3,4]
mapped = map(lambda p: p+1, a)
print(list(mapped))

# filter
a = [1,2,3,4]
filtered = filter(lambda p: p > 2, a)
print(list(filtered))


teste = [
    {
        "nome": "teste",
        "idade": 25
    },
    {
        "nome": "teste1",
        "idade": 24
    },
    {
        "nome": "teste2",
        "idade": 23
    }
]
filtered = filter(lambda p: p["idade"] >= 24, teste)
print(list(filtered))
"""

## ADICIONAR a palavra "Mapeado" ao fim de cada nome

teste = [
    {
        "nome": "teste",
        "idade": 25
    },
    {
        "nome": "teste1",
        "idade": 24
    },
    {
        "nome": "teste2",
        "idade": 23
    }
]

