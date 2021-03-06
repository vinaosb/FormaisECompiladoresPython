##   Trabalho    Formais 2019-1
## Alunos: Bruno George de Moraes
##         Vinícius Schwinden Berkenbrock
##
from src import automato_finito

def teste1():
    af = automato_finito.AutomatoFinito()


    af.add_transicao('q0', 'a', 'q1')
    af.add_transicao('q0', '&', 'q2')
    af.add_transicao('q1', 'a', 'q1')
    af.add_transicao('q1', 'b', 'q2')
    af.add_transicao('q2', 'b', 'qf')

    af.add_estados_finais('qf')
    af.set_estado_inicial('q0')

    af2 = af.to_afd()

    print('Automato teste1')
    print(af.print())
    print('Automato Deterministico resultante de teste1: \n')
    print(af2.print())