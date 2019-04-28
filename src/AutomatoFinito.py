class Transicao:
    def __init__(self, Q):
        self.Q = Q
        self.P = dict()
    
    def addTransicao(self, P, a):
        if a not in self.P:
            self.P[a] = list()
            if P not in self.P[a]:
                self.P[a].append(P)
        else:
            if P not in self.P[a]:
                self.P[a].append(P)

class AF:
    def __init__(self, estadoInicial):
        self.inicial = estadoInicial
        self.estados = list()
        self.estados.append(estadoInicial)
        self.finais = list()
        self.transicoes = list()
        self.entradas = list()

    def addEstado(self, E):
        if E not in self.estados:
            self.estados.append(E)
    
    def addFinal(self, F):
        if F not in self.finais and F in self.estados:
            self.finais.append(F)
    
    def addEntradas(self, a):
        if a not in self.entradas:
            self.entradas.append(a)

    def addTransicao(self, Q, P, a):
        if (P in self.estados and Q in self.estados and a in self.entradas):
            for i in self.transicoes:
                if (i.Q == Q):
                    i.addTransicao(P,a)
                    return
            Tran = Transicao(Q)
            Tran.addTransicao(P, a)
            self.transicoes.append(Tran)
    
    def efecho(self, Q):
        p = dict()
        for i in self.entradas:
            if i != "&":
                p[i] = list()

        for t in self.transicoes:
            if (t.Q == Q):
                #todo



    def determinizarAutomato(self):
        novosEstados = list()
        novosEstados.append(self.inicial)
        for t in self.transicoes:
            for u in t.P:
                temp = ""
                for v in t.P[u]:
                    temp += v
                    self.estados.remove(v)
                t.P[u].clear()
                t.P[u].append(temp)
                self.addEstado(temp)
    