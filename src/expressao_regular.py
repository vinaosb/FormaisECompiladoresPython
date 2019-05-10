##   Trabalho    Formais 2019-1
## Alunos: Bruno George de Moraes
##         Vinícius Schwinden Berkenbrock
##

class ExpressaoRegular:

    expr = '#'
    nome = ''
    def __init__(self, expr='#', nome=''):
        self.expr = expr
        self.nome = nome

    def concatenar(self, expressao):                
        self.expr = self.expr[:-1] + expressao + '#'

    def nomear(self, nome):                
        self.nome = nome

    def print(self):
        saida = '' + self.expr[:-1]
        saida += '\n'
        return saida
