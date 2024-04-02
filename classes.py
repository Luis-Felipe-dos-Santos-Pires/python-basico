
"""
# Para criar uma classe:
class Ex1:
    x = 5

# Criando um objeto:
objetoEx1 = Ex1()
print(objetoEx1.x)

# Construtor
class Ex2:
    def __init__(self,x,y):
        self.x = x
        self.y = y

objetoEx2 = Ex2(6,7)
print(objetoEx2.x,objetoEx2.y)

"""

# Função de representação
class Ex3:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return str({
            "x": self.x,
            "y": self.y
        })

objetoEx3 = Ex3(6,7)
print(objetoEx3)


# Métodos das classes
class Ex4:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def set_x(self, x):
        self.x = x

objetoEx4 = Ex4(6,7)
objetoEx4.set_x("asdf")
print(objetoEx4.x)

