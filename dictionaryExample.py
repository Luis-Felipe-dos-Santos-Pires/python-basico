# São a interface para trabalhar com JSONS
"""
# Não pode haver a repetição de chaves
thisdict = {
  "marca": "Ford",
  "modelo": "Mustang",
  "ano": 1964,
  "ano": 2020
}
print(thisdict)
"""

# Possuem um construtor
thisdict = dict(nome = "João", idade = 24, pais = "Brasil")
#print(thisdict)


"""
# Para acessar items do dicionário
print(thisdict["nome"])
print(thisdict.get("idade"))


# Para pegar apenas as chaves
print(thisdict.keys())

# Para pegar apenas os valores
print(thisdict.values())

# Para pegar cada item individualmente
print(thisdict.items())


# Conferir se uma chave existe
if "teste" in thisdict:
    print("Existe")

# Alterando valores no dicionário
thisdict["nome"] = "TESTE"
print(thisdict)


thisdict.update({
    "nome": "João",
    "cidade": "SBS",
    "uf": "SC"
})
#print(thisdict)


# Removendo itens do dicionário
thisdict.pop("uf")
print(thisdict)

# Removendo itens do dicionário
thisdict.update({
    "uf": "SC"
})
print(thisdict)
thisdict.popitem()
print(thisdict)
del thisdict["cidade"]
print(thisdict)
thisdict.clear()
print(thisdict)

# Loops
thisdict = {
  "marca": "Ford",
  "modelo": "Mustang",
  "ano": 1964
}

# Chaves
for x in thisdict:
  print(x)

# Valores
for x in thisdict:
  print(thisdict.get(x))

# Chaves e valores
for x, y in thisdict.items():
  print(x, y)


thisdict = {
  "marca": "Ford",
  "modelo": "Mustang",
  "ano": 1964
}

# Copiando um dicionário
dict1 = thisdict
dict1.popitem()
print(thisdict,dict1)

dict1 = thisdict.copy()
dict1.popitem()
print(thisdict,dict1)

# Dicionários aninhados
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily["child1"]["name"])

# Set default
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("model", "Bronco")
y = car.setdefault("color", "White")

print(car, x, y)
"""

# From keys
x = ('key1', 'key2', 'key3')
y = 0

thisdict1 = dict.fromkeys(x, y)

print(thisdict1)

thisdict = {
  "marca": "Ford",
  "modelo": "Bronco",
  "ano": 1964
}

keys = thisdict.keys()
thisdict2 = dict.fromkeys(keys, None)

print("\n\n",thisdict2)
