class Carro:
    def __init__(self, modelo, cor, ano, preco):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.preco = preco
        self.ligado = False
        self.velocidade = 0
    
    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False # para ligar e desligar o carro

    def acelerar(self):
        self.velocidade += 10


carro1 = Carro('Fusca', 'azul', '1900', 5000)
print(carro1.ligado, carro1.velocidade)
carro1.ligar()
carro1.acelerar()
# print(carro1.ligar()) -> isso não funciona porque o método não me retorna nada, apenas executa uma função
print(carro1.ligado, carro1.velocidade)