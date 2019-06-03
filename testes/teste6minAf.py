##   Trabalho    Formais 2019-1
## Alunos: Bruno George de Moraes
##         Vinícius Schwinden Berkenbrock
##
from src import automato_finito

def teste6():
    af2 = automato_finito.AutomatoFinito()

    af2.add_transicao('q0', 'a', 'q1')
    af2.add_transicao('q1', 'b', 'q2')
    af2.add_transicao('q2', 'b', 'q3')
    af2.add_transicao('q3', 'a', 'qf')
    af2.add_transicao('q3', 'a', 'q2')
    af2.add_transicao('qf', 'a', 'qf')

    af2.add_estados_finais('qf')
    af2.set_estado_inicial('q0')

    af3 = af2.minimizar()




    print('Automato teste6')
    print(af2.print())
    print('Automato minimo resultante de teste6: \n')
    print(af3.print())

    print('Automato Entrada \n')
    print(af2.print())
