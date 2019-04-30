class ExpressaoRegular:

    expr = '#'
    nome = ''
    def __init__(self, expr='#', nome=''):
        self.expr = expr
        self.nome = nome

    def concatenar(self, expressao):                
        self.expr = self.expr[:-1] + expressao + '#'

    def print(self):
        saida = '' + self.expr[:-1]
        saida += '\n'
        return saida
