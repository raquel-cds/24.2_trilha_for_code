import time

c = 0 # está no escopo global

while True:
    '''if c <= 10:
       pass # continue o fluxo do código
    else:
        break # estrutura de quebra'''
    c += 1
    if c == 4:
        continue # interromper apenas a iteração atual

    elif c > 10:
        break

    print(c)
    time.sleep(1)


print('Fim!')