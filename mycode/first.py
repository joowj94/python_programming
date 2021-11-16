def add(n1, n2):
    #pass
    return n1 + n2

print(add(10, 20))

add2 = lambda n1, n2 : n1 + n2
print(add2(100,200))



class User:
    def __init__(self, name):
        self.name = name
user = User("파리썬")
print(user)