class Padeiro:
    def __init__(self, nome):
        self.nome = nome
        self.dinheiro = 0
        self.paes = 0

    def assar_paes(self, quantidade):
        if quantidade > 6:
            print('Capacidade máxima do forno é 6')

        else:
            self.paes += quantidade

class Cliente:
    def __init__(self, nome, dinheiro):
        self.nome = nome
        self.dinheiro = dinheiro
        self.paes = 0

    def comprar_paes(self, quantidade, padeiro):
        preco_pao = quantidade * 0.5
        if quantidade > padeiro.paes:
            print('Não há pães suficiente para a compra')

        elif self.dinheiro <  preco_pao:
            print('Você não tem dinheiro suficiente para a compra')

        else:
            
            self.dinheiro -=  preco_pao # dinheiro do cliente
            self.paes += quantidade
            padeiro.dinheiro +=  preco_pao
            padeiro.paes -= quantidade
            print(f'Compra realizada com sucesso!. Agora {self.nome} tem {self.paes} e {self.dinheiro} reias.')

padeiro1 = Padeiro('Joao')
cliente1 = Cliente('Maria', 10)
padeiro1.assar_paes(6)
cliente1.comprar_paes(3, padeiro1)