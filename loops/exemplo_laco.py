import os # importando biblioteca que interage com o sistema operacional
import time # biblioteca temporal 

segundos = 0
minutos = 0

while True:
    # limpa o meu terminal a cada iteração
    os.system('cls') # Para o windows 
    if segundos == 60:
        segundos = 0
        minutos += 1
    if segundos < 10:
        print(f'0{minutos}:0{segundos}')
    else:
        print(f'0{minutos}:{segundos}')
    time.sleep(1)
    segundos += 1
    
    