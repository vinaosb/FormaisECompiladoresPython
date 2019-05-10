import automato_finito
import gramatica_regular
import expressao_regular


class Crud:
    def save_automatos(automatos):
        file_object = open("automatos.txt",'w')

        for a in automatos:
            file_object.write(a.nome)
            file_object.write(a.inicial)
            file_object.write(a.finais)
            file_object.write(a.estados)
            file_object.write(a.transicoes)
            file_object.write('\n')

    
    def save_gramaticas(gramaticas):
        file_object = open("gramaticas.txt",'w')

        for g in gramaticas:
            file_object.write(g.nome)
            file_object.write(g.inicial)
            file_object.write(g.variaveis)
            file_object.write(g.transicoes)
            file_object.write('\n')

                
    def save_expressoes(expressoes):
        file_object = open("expressoes.txt",'w')

        for e in expressoes:
            file_object.write(e.nome)
            file_object.write(e.expr)
            file_object.write('\n')


    def load_automatos():
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
            
    def load_gramaticas():
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

    def load_expressoes():
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
