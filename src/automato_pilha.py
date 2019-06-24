##   Trabalho Formais 2019-1
## Alunos: Bruno George de Moraes
##         Vinícius Schwinden Berkenbrock
##

class AutomatoPilha:
	estados = set()
	finais = set()
	inicial = ""
	Pilha = ""
	alfabetoPilha = set()
	alfabetoEntrada = set()
	transicoes = dict()

	def __init__(self, nome=''):
		self.nome = nome

	def addEstado(self,estado = -1):
		if estado == -1:
			estado = self.genNewSimb()
		self.estados.add(estado)

	def addAlfaPilha(self,letra):
		self.alfabetoPilha.add(letra)

	def addAlfaEntr(self, letra):
		self.alfabetoEntrada.add(letra)

	def setInicial(self,inicial):
		if inicial not in estados:
			addEstado(inicial)
		self.inicial = inicial
	
	def setPilhaInicial(self, pilha):
		for p in pilha:
			if p not in alfabetoPilha:
				self.addAlfaPilha(p)
		self.Pilha = pilha

	def addTransicao(self, estado, entrada, pilha, proxEstado, proxPilha):
		if entrada not in self.alfabetoEntrada:
			self.addAlfaEntr(entrada)
		if pilha not in self.alfabetoPilha:
			self.addAlfaPilha(pilha)
		if estado not in estados:
			self.addEstado(estado)
		transicoes[(estado, pilha, entrada)] = (proxEstado, proxPilha)

	def check(self, palavra) -> bool:
		atual = (self.inicial, self.Pilha)
		for ch in palavra:
			if (atual[0], atual[1], ch) in self.transicoes.keys():
				atual = self.transicoes[(atual[0], atual[1], ch)][0]
			else:
				return False
		if atual in self.finais:
			return True
		else:
			return False

	# Gera um novo simbolo para estados (função auxiliar)
	def genNewSimb(self, j = 0):
		temp = "A"
		for i in range(j,25):
			if chr(ord(temp)+ i) not in self.estados:
				return chr(ord(temp)+ i)
		temp = "a"
		k = j - 24
		if k < 0:
			k = 0
		for i in range(k,26):
			if chr(ord(temp)+ i) not in self.estados:
				return chr(ord(temp)+ i)
		l = k - 25
		if l < 0:
			l = 0
		for i in range(l,10):
			if str(i) not in self.estados:
				return str(i)