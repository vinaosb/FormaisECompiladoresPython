##   Trabalho    Formais 2019-1
## Alunos: Bruno George de Moraes
##         Vinícius Schwinden Berkenbrock
##
from src import automato_finito as af
from src import gramatica_regular as gr
from src import expressao_regular as er
from testes import teste1AfndEpsulonAfd
from testes import teste2AfndAfd
from testes import teste3AfdGr
from testes import teste4GrAfnd



def main_teste():
    teste1AfndEpsulonAfd.teste1()
    teste2AfndAfd.teste2()
    teste3AfdGr.teste3()
    teste4GrAfnd.teste4()

if __name__ == "__main__":
    main_teste()
