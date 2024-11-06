# Salvando texto como tipo de dado

texto = """Python é uma linguagem de programação de alto nível, [5] interpretada de script, imperativa, orientada 
a objetos, funcional, de tipagem dinâmica e forte. Foi lançada por Guido van Rossum em 1991. [1] Atualmente, possui 
um modelo de desenvolvimento comunitário, aberto e gerenciado pela organização sem fins lucrativos Python Software 
Foundation. Apesar de várias partes da linguagem possuírem padrões e especificações formais, a linguagem, como um 
todo, não é formalmente especificada. O padrão na pratica é a implementação CPython. A linguagem foi projetada com 
a filosofia de enfatizar a importância do esforço do programador sobre o esforço computacional. Prioriza a legibilidade
do código sobre a velocidade ou expressividade. Combina uma sintaxe concisa e clara com os recursos poderosos de sua 
biblioteca padrão e por módulos e frameworks desenvolvidos por terceiros.""" 

# Inicializar a variável de armazenamento 
novo_texto = ""

# Transformando o texto em uma lista de palavras
lista_palavras = texto.split(' ')

# Usamos for como iterador para varrer a lista
for indice in range(len(lista_palavras)):
    if lista_palavras[indice] == 'Python':
        lista_palavras[indice] = 'Fython'

# Usamos o for com generator para voltar a lista de palavras modificada em texto
for palavra in lista_palavras:
    novo_texto = novo_texto + palavra + " "

print(novo_texto)