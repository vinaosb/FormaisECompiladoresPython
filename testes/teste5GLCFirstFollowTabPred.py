##   Trabalho    Formais 2019-1
## Alunos: Bruno George de Moraes
##         Vin�cius Schwinden Berkenbrock
##

from src import gramatica_livre_de_contexto as glc

def teste5():
	gr = glc.GramaticaLivreContexto()

	gr.addTerminal('a')
	gr.addTerminal('b')
	gr.addTerminal('c')
	gr.addTerminal('d')

	gr.addNaoTerminal('S')
	gr.addNaoTerminal('A')
	gr.addNaoTerminal('B')

	gr.addProducao('S','Ab')
	gr.addProducao('S','ABc')
	gr.addProducao('A','&')
	gr.addProducao('A','aA')
	gr.addProducao('B','bB')
	gr.addProducao('B','Ad')
	gr.addProducao('B','&')

	gr.defInicial('S')
	

	print(gr.print())
	print("First : ")
	print(gr.printFirst())
	print("Follow : ")
	print(gr.printFollow())
	print(gr.printTabelaPreditiva())
	#print(gr.calcAceitacao(""))