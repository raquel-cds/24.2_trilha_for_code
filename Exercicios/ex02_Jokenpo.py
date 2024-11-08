# EXERCICIO: Fazer um pedra, papel e tesoura melhor de 5

import random
from time import sleep

jogo = ['pedra', 'papel', 'tesoura']
partidas = {} # salvando as partidas
c = 0
frase = "1 partida"
vitorias_jogador = 0
vitorias_computador = 0

while True:
    jogador = input("Digite sua opção: ")
    computador = random.choice(jogo)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    

# EM CADA OPÃO TEMOS 3 POSSIBILIDADES 

    if computador == 'pedra': # COMPUTADOR JOGOU PEDRA

        if jogador == 'pedra':
            print('EMPATE!')
            vitorias_jogador += 1
            vitorias_computador += 1

        elif jogador == 'papel':
            print('Você ganhou!')
            vitorias_jogador += 1

        elif jogador == 'tesoura':
            print('Computador ganhou!')
            vitorias_computador += 1
    
        else:
            print('Jogada invalida :( )')

    elif computador == 'papel': # COMPUTADOR JOGOU PAPEL

        if jogador == 'pedra':
            print('Computador ganhou!')
            vitorias_computador += 1

        elif jogador == 'papel':
            print('EMPATE!')
            vitorias_computador += 1
            vitorias_jogador += 1

        elif jogador == 'tesoura':
            print('Você ganhou!')
            vitorias_jogador += 1
    
        else:
            print('Jogada invalida :( )')

    elif computador == 'tesoura': # COMPUTADOR JOGOU TESOURA

        if jogador == 'pedra':
            print('Você venceu!')
            vitorias_jogador += 1

        elif jogador == 'papel':
            print('Computador ganhou!')
            vitorias_computador += 1

        elif jogador == 'tesoura':
            print('EMPATE!')
            vitorias_computador += 1
            vitorias_jogador += 1
    
        else:
            print('Jogada invalida :( )')        
    
    partidas[frase] = [jogador, computador] # armazenando as partidas
    c += 1
    frase = f'{1 + c} partida'

    if vitorias_computador == 5 or vitorias_jogador == 5:
        break
    

print(partidas) # printar o resultado das partidas no final
print(f'Vitórias do jogador: {vitorias_jogador}')
print(f'Vitórias do computador: {vitorias_computador}')