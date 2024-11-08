lista = [1, 2, 3]

def generator(lista):
    for i in lista:
        yield lista**2 # não posso escrever o que eu quiser embaixo, pois o código continua embaixo do yield
        # return quebra o que ta embaixo da função

g = generator(lista) # precisa ser definido dentro de uma variável

for i in range(4):
    print(next(g))