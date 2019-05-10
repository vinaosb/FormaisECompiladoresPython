##   Trabalho    Formais 2019-1
## Alunos: Bruno George de Moraes
##         Vinícius Schwinden Berkenbrock
##

import automato_finito
import gramatica_regular
import expressao_regular
import sys
sys.path.insert(0, '../testes/')
import teste1AfndEpsulonAfd
import teste2AfndAfd
import teste3AfdGr
import teste4GrAfnd



def main_teste():
    teste1()
    teste2()
    teste3()
    teste4()