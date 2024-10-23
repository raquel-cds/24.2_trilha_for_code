# O computador vai "pensar" em um número entre 0 e 10. 
# Crie um jogo onde o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer

import random

num_aleatorio = random.randint(0, 10)
print(num_aleatorio)
palpite = int(input('Qual foi o número que o computador pensou? '))
p = 1
while num_aleatorio != palpite:
    print('Você errou! Tente novamente.')
    palpite = int(input('Qual foi o número que o computador pensou? '))
    p += 1

else:
    print('Você acertou!')
    print(f'Você precisou de {p} palpites para acertar')
    