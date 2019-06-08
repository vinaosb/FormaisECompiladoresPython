##   Trabalho    Formais 2019-1
## Alunos: Bruno George de Moraes
##         Vinícius Schwinden Berkenbrock
##
from src import automato_finito as af
from src import gramatica_regular as gr
from src import expressao_regular as er
from src import gramatica_livre_de_contexto as glc
from testes import teste1AfndEpsulonAfd
from testes import teste2AfndAfd
from testes import teste3AfdGr
from testes import teste4GrAfnd
from testes import teste5GLCFirstFollow
from testes import teste6minAf
from testes import teste7checkAf



def main_teste():
	teste1AfndEpsulonAfd.teste1()
	teste2AfndAfd.teste2()
	teste3AfdGr.teste3()
	teste4GrAfnd.teste4()
	teste5GLCFirstFollowTabPred.teste5()
	teste6minAf.teste6()
	teste7checkAf.teste7()

if __name__ == "__main__":
	main_teste()
