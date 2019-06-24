##   Trabalho    Formais 2019-1
## Alunos: Bruno George de Moraes
##         Vin�cius Schwinden Berkenbrock
##

from src import gramatica_livre_de_contexto as glc

def teste8():
        gr = glc.GramaticaLivreContexto()

        gr.addTerminal('a')
        gr.addTerminal('b')
        gr.addTerminal('c')
        gr.addTerminal('e')

        gr.addNaoTerminal('A')
        gr.addNaoTerminal('B')
        gr.addNaoTerminal('C')
        gr.addNaoTerminal('D')
        gr.defInicial('A')

        gr.addProducao('A','BCDe')
        #gr.addProducao('A','&')
        gr.addProducao('B','&')
        gr.addProducao('B','e')
        gr.addProducao('C','&')
        gr.addProducao('C','a')
        gr.addProducao('D','b')
        gr.addProducao('D','cC')


        print(gr.print())
        print(":Elim & prod:::: ")
        gr.remEpsulonProducoes()
        print("result: ")
        print(gr.print())

        print("again : ")
        gr.remEpsulonProducoes()
        print(gr.print())
