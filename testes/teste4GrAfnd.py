##   Trabalho    Formais 2019-1
## Alunos: Bruno George de Moraes
##         Vinícius Schwinden Berkenbrock
##
from src import gramatica_regular

def teste4():
    gr = gramatica_regular.GramaticaRegular()

    gr.add_regras('S', '0', 'S')
    gr.add_regras('S', '1', 'A')
    gr.add_regras('A', '0', 'B')
    gr.add_regras('A', '1', 'A')
    gr.add_regras('B', '0', 'S')
    gr.add_regras('B', '1', '&')
    gr.set_variavel_inicial('S')

    print(gr.print())
    print('Teste 4: GR convertida para afnd: \n')
    print(gr.to_afnd().print())


