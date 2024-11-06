# se eu fizesse com listas
lista = [["Caxias", "Barra da Tijuca", "Lapa"], ["Rio de Janeiro", "São Paulo"]]

print(lista[0])

# se eu fizesse com dicionários

dicionario = {"Bairros":["Caxias", "Barra da Tijuca", "Lapa"], "Cidades": ["Rio de Janeiro", "São Paulo"] }

'''print(dicionario["Bairros"])
print(dicionario.keys())
print(dicionario.values())

lista_chaves = list(dicionario.keys()) # transformando as chaves do dicionário em lista
print(lista_chaves)

adicionando valores
dicionario["Bairros"].append('Botafogo')
print(dicionario)'''

# Adicionando chaves
dicionario["Estados"] = ["RJ", "SP", "MG"]
print(dicionario)