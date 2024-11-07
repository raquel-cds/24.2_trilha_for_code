a = 0

def escopo1():
    global a # estou indicando ao meu código que esta variável é global
    a = 10

escopo1()
print(a)