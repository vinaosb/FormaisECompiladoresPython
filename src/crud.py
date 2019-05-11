##   Trabalho    Formais 2019-1
## Alunos: Bruno George de Moraes
##         Vinícius Schwinden Berkenbrock
##

import automato_finito
import gramatica_regular
import expressao_regular


class Crud:
    def save_automatos(automatos):
        file_object = open("automatos.txt",'w')

        for a in automatos:
            file_object.writelines(a.nome)
            file_object.writelines(a.inicial)
            file_object.writelines(a.finais)
            file_object.writelines(a.estados)
            file_object.writelines(a.transicoes)

    
    def save_gramaticas(gramaticas):
        file_object = open("gramaticas.txt",'w')

        for g in gramaticas:
            file_object.writelines(g.nome)
            file_object.writelines(g.inicial)
            file_object.writelines(str(g.variaveis))
            file_object.writelines(str(g.transicoes))

                
    def save_expressoes(expressoes):
        file_object = open("expressoes.txt",'w')

        for e in expressoes:
            file_object.writelines(e.nome)
            file_object.writelines(e.expr)


    def load_automatos():
        file_object = open("automatos.txt",'r')
        ret = []
        aut = automato_finito.AutomatoFinito()

        lines = file_object.readlines()

        for i in range(0, len(lines)):
            if (i%5 == 0):
                aut = automato_finito.AutomatoFinito(lines[i])
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
            
    def load_gramaticas():
        file_object = open("gramaticas.txt",'r')
        ret = []
        gra = gramatica_regular.GramaticaRegular()

        lines = file_object.readlines()

        for i in range(0, len(lines)):
            if (i%4 == 0):
                gra = gramatica_regular.GramaticaRegular(lines[i])
            if (i%4 == 1):
                gra.inicial = lines[i]
            if (i%4 == 2):
                gra.variaveis = lines[i]
            if (i%4 == 3):
                gra.transicoes = lines[i]
                ret.append(gra)
        return ret

    def load_expressoes():
        file_object = open("expressoes.txt",'r')
        ret = []
        exp = expressao_regular.ExpressaoRegular()

        lines = file_object.readlines()

        for i in range(0, len(lines)):
            if (i%2 == 0):
                exp = expressao_regular.ExpressaoRegular(lines[i])
            else:
                exp.expr = lines[i]
                ret.append(exp)
                return ret
