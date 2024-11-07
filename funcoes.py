# O que são funções ?
# Quando declaro uma função, eu estou executando nada, apenas salvando um conjunto de info. do meu código
# print("Hello World") # executei algo

# carregando o código na memória 
# argumentos facultativos tem que vir depois dos não definidos.
'''def soma(x, y=10): # dois pontos cria o escopo
    variavel_soma = x + y
    # print(variavel_soma)
    return variavel_soma # guarda na memória

soma(3, 3) # executei
print(soma(10, 20)) '''
# Sem o print, a soma(10,20) não retorna nada. 
# Se eu não colocar nenhum return ele vai me retornar None

'''def par(numero):
    return numero % 2 == 0

print(par(2))'''

print("Hello World", end="") # end é parâmetro facultativo de pular linha
print("Hello World", end="")