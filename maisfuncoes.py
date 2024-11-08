'''def somar(x, y):
    return x + y

somar2 = lambda x, y: (x + y) # para funcões mais simples
print(somar2(10,20))

def receba_pin():
    senha = input("Digite seu pin (somente números!)")
    try: # tente fazer tal coisa
        senha = int(senha)
    except: # se não conseguir, faça
        print("Senha invalida! Tente novamente  com números")
        receba_pin()


receba_pin()'''

pares_ate_20 = []
for i in range(11):
    pares_ate_20.append(i*2)

pares_ate_40 = [i*2 for i in range(21)]

print(pares_ate_20)
print(pares_ate_40)
