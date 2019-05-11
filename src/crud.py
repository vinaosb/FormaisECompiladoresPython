##   Trabalho    Formais 2019-1
## Alunos: Bruno George de Moraes
##         Vinícius Schwinden Berkenbrock
##

from src import automato_finito
from src import gramatica_regular
from src import expressao_regular


class Crud:
    def save_automatos(self, automatos):
        file_object = open("automatos.txt",'w')

        for a in automatos:
            file_object.writelines(a.nome)
            file_object.writelines(a.inicial)
            file_object.writelines(a.finais)
            file_object.writelines(a.estados)
            file_object.writelines(a.transicoes)

    
    def save_gramaticas(self, gramaticas):
        file_object = open("gramaticas.txt",'w')

        for g in gramaticas:
            file_object.writelines(g.nome)
            file_object.writelines(g.inicial)
            file_object.writelines(g.variaveis)
            file_object.writelines(g.transicoes)

                
    def save_expressoes(self, expressoes):
        file_object = open("expressoes.txt",'w')

        for e in expressoes:
            file_object.writelines(e.nome)
            file_object.writelines(e.expr)


    def load_automatos(self):
        file_object = open("automatos.txt",'r')
        ret = []
        aut = AutomatoFinito()

        lines = file_object.readlines()

        for i in range(0, len(lines)):
            if (i%5 == 0):
                aut = AutomatoFinito(lines[i])
            if (i%5 == 1):
                aut.inicial = lines[i]
            if (i%5 == 2):
                aut.finais = lines[i]
            if (i%5 == 3):
                aut.estados = lines[i]
            if (i%5 == 4):
                aut.transicoes = lines[i]
                ret.append(aut)
        return ret
            
    def load_gramaticas(self):
        file_object = open("gramaticas.txt",'r')
        ret = []
        gra = GramaticaRegular()

        lines = file_object.readlines()

        for i in range(0, len(lines)):
            if (i%4 == 0):
                gra = GramaticaRegular(lines[i])
            if (i%4 == 1):
                gra.inicial = lines[i]
            if (i%4 == 2):
                gra.variaveis = lines[i]
            if (i%4 == 3):
                gra.transicoes = lines[i]
                ret.append(gra)
        return ret

    def load_expressoes(self):
        file_object = open("expressoes.txt",'r')
        ret = []
        exp = ExpressaoRegular()

        lines = file_object.readlines()

        for i in range(0, len(lines)):
            if (i%2 == 0):
                exp = ExpressaoRegular(lines[i])
            else:
                exp.expr = lines[i]
                ret.append(exp)
                return ret
