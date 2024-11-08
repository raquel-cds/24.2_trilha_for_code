from math import log, e

# função para executar a ação

def convergencia():
    num = 2 # nosso valor inicial
    soma = 0 # soma todas as sequências dos resultados
    while True:
        resultado = 1 / (num * log(num, e) ** 2)
        soma += resultado
        print(soma)
        num += 1
    
convergencia()
