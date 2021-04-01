class No:
    def __init__(self, valor, proximo = None): #__init__ -> construtor 
        self.valor = valor #self -> tudo que pertence ao construtor
        self.proximo = proximo

    def setProximo(self, proximo):
        self.proximo = proximo

    def getProximo(self):
        return self.proximo

    def getValor(self)
        return self.valor