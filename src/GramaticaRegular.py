class Producao:
    def __init__(self, inicial):
        self.inicial = inicial
        self.alvo = ""
    
    def addAlvo(self, alvo):
        self.alvo += alvo

class GR:
    def __init__(self, inicial):
        self.terminais = list()
        self.naoterminais = list()
        self.inicial = inicial
        self.producoes = list()
    
    def addProducao(self, A, B):
        DontHaveA = True
        AlreadyAdded = False
        for i in self.producoes:
            if (i.inicial == A):
                DontHaveA = False
                for k in i.alvo:
                    if k == B:
                        AlreadyAdded = True
                if (not AlreadyAdded):
                    i.addAlvo(B)
        if (DontHaveA):
            p = Producao(A)
            p.addAlvo(B)

    def addNaoTerminal(self, nt):
        if nt not in self.naoterminais:
            self.naoterminais.append(nt)

    def addTerminal(self, t):
        if t not in self.terminais:
            self.terminais.append(t)
    
    def AFDtoGR(self, automato):
        for e in automato.estados:
            self.addNaoTerminal(e)
        
        for s in automato.entradas:
            self.addTerminal(s)
        
        self.inicial = automato.inicial

        for t in automato.transicoes:
            for k in t.P:
                temp = Producao(t.Q)
                temp.addAlvo(k)
                if t.P[k] not in automato.finais:
                    temp.addAlvo(t.P[k])
                self.producoes.append(temp)
