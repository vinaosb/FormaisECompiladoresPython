##   Trabalho    Formais 2019-1
## Alunos: Bruno George de Moraes
##         Vinícius Schwinden Berkenbrock
##
from src import automato_finito

def teste7():
    af2 = automato_finito.AutomatoFinito()

    af2.add_transicao('q0', 'a', 'q1')
    af2.add_transicao('q1', 'b', 'q2')
    af2.add_transicao('q2', 'b', 'q3')
    af2.add_transicao('q3', 'a', 'qf')
    af2.add_transicao('q3', 'a', 'q2')
    af2.add_transicao('qf', 'a', 'qf')

    af2.add_estados_finais('qf')
    af2.set_estado_inicial('q0')

    print('Automato teste7')
    print(af2.print())
    print('Verifica se o automato reconhece uma palavra, retorna true caso reconheca: \n')
    palavra = 'aaaba'
    af2.check( palavra )
 
