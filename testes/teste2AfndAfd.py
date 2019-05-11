##   Trabalho    Formais 2019-1
## Alunos: Bruno George de Moraes
##         Vinícius Schwinden Berkenbrock
##
from src import automato_finito

def teste2():
    af = automato_finito.AutomatoFinito()


    af.add_transicao('q0', 'a', 'q1')
    af.add_transicao('q1', 'a', 'q1')
    af.add_transicao('q1', 'a', 'q2')
    af.add_transicao('q1', 'b', 'q2')
    af.add_transicao('q2', 'b', 'qf')

    af.add_estados_finais('qf')
    af.set_estado_inicial('q0')

    af2 = af.to_afd()

    print('Automato teste2')
    print(af.print())
    print('Automato Deterministico resultante de teste2: \n')
    print(af2.print())