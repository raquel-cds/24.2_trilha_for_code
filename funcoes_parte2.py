import os
import time

def inicializa_valores():
    segundos = 0
    minutos = 0
    horas = 0
    return segundos, minutos, horas

def verifica_virada_tempo(segundos, minutos, horas):
    if segundos == 60:
        if minutos == 59:
            minutos = 0
            segundos = 0
            horas += 1
        else:
            segundo = 0
            minutos += 1

    return segundos, minutos

def duas_casas_decimais(segundos, minutos, horas):
    if segundos < 10:
        segundos = f'0{str(segundos)}'
    if minutos < 10:
        minutos = f'0{str(minutos)}'
    if horas < 10:
        segundos = f'0{str(horas)}'

    return segundos, minutos, horas

def roda_relogio():
    segundos, minutos, horas = inicializa_valores()

    while True:
        os.system('cls')

        segundos, minutos, horas = verifica_virada_tempo(segundos, minutos, horas)
        segundos, minutos, horas = duas_casas_decimais(segundos, minutos, horas)


        time.sleep(1)
        segundos += 1

roda_relogio()