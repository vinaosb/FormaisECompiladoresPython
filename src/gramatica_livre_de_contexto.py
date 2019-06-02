##   Trabalho Formais 2019-1
## Alunos: Bruno George de Moraes
##         Vin�cius Schwinden Berkenbrock
##



class GramaticaLivreContexto:
	firsts = dict()
	follows = dict()
	preditiveTable = dict()

	def __init__(self, nome = ''):
		self.naoTerminal = set()
		self.terminal = set()
		self.regrasProd = {}
		self.inicial = ''
		self.nome = nome


	def addTerminal(self, t):
		self.terminal.add(t)

	def addNaoTerminal(self, nt):
		self.naoTerminal.add(nt)
		self.regrasProd[nt] = set()

	def defInicial(self, ini):
		if ini not in self.naoTerminal:
			self.naoTerminal.add(ini)
		self.inicial = ini

	def addProducao(self,nt,prod):
		self.regrasProd[nt].add(prod)

	def print(self):
		saida = ''
		for nt in self.naoTerminal:
			saida = saida + nt
			saida = saida + '->'
			for prod in self.regrasProd[nt]:
				saida = saida + prod + '|'
			saida = saida + '\n'
		return saida

	def first(self, simb):
		if simb in self.terminal or simb == '&':
			return {simb}
		else:
			aux = set()
			for prod in self.regrasProd[simb]:
				for i in range(0, len(prod)):
					if prod[i] in self.terminal or prod[i] == '&':
						aux.add(prod[i])
						break
					else:
						fx = self.first(prod[i])
						if '&' not in fx:
							aux = aux.union(fx)
							break
						elif i == len(prod)-1:
							aux.add('&')
						else:
							fx = fx.difference({'&'})
							aux = aux.union(fx)
			return aux

	def calcFollow(self):
		t = True

		if len(self.firsts) == 0:
			self.calcFirst()
		for simb in self.naoTerminal:
			self.follows[simb] = set()
			if simb == self.inicial:
				self.follows[simb].add('$')
		for simb in self.terminal:
			self.follows[simb] = set()
			self.follows[simb].add(simb)
		while(t):
			t = False
			for simb in self.naoTerminal:
				for prod in self.regrasProd[simb]:
					if prod != '&':
						for i in range(0, len(prod)):
							added = False
							last = False
							for j in range(i+1,len(prod)):
								if prod[i] in self.naoTerminal and prod[j] in self.terminal:
									self.follows[prod[i]] = self.follows[prod[i]].union(self.follows[prod[j]])
									break
								elif prod[i] in self.naoTerminal:
									self.follows[prod[i]] = self.follows[prod[i]].union(self.firsts[prod[j]])
									self.follows[prod[i]].discard('&')
							if i == len(prod)-1 and prod[i] in self.naoTerminal:
								l1 = len(self.follows[prod[i]])
								self.follows[prod[i]] = self.follows[prod[i]].union(self.follows[simb])
								if (l1 != len(self.follows[prod[i]])):
									t = True

						

	def calcFirst(self):
		for t in self.terminal:
			self.firsts[t] = self.first(t)
		for nt in self.naoTerminal:
			self.firsts[nt] = self.first(nt)

	def calcPred(self):
		if len(self.firsts) == 0:
			self.calcFirst()
		if len(self.follows) == 0:
			self.calcFollows()
		for nt in self.naoTerminal:
			self.preditiveTable[nt] = dict()
			for t in self.terminal:
				self.preditiveTable[nt][t] = set()
		for simb in self.naoTerminal:
			for prod in self.regrasProd[simb]:
				if prod[0] != '&':
					for t in self.firsts[prod[0]]:
						if (t != '&'):
							self.preditiveTable[simb][t].add(prod)
						if t == '&':
							for tt in self.follows[prod[0]]:
								self.preditiveTable[simb][tt].add(prod)

	def printFirst(self):
		self.calcFirst()
		saida = ''
		for nt in self.naoTerminal:
			saida = saida + 'First(' + nt + ')'
			for f in self.firsts[nt]:
				saida = saida + f
			saida = saida + '\n'
		return saida

	def printFollow(self):
		self.calcFollow()
		saida = ''
		for nt in self.naoTerminal:
			saida = saida + 'Follow(' + nt + ')'
			for f in self.follows[nt]:
				saida = saida + f
			saida = saida + '\n'
		return saida

	def printTabelaPreditiva(self):
		self.calcPred()
		saida = 'Tabela Preditiva: \n'
		saida = saida + '\t'
		for t in self.terminal:
			saida = saida + t + '\t\t\t'
		saida = saida + '\n'

		for nt in self.naoTerminal:
			saida = saida + nt + '\t'
			for t in self.terminal:
				for pt in self.preditiveTable[nt][t]:
					saida = saida + pt + ' '
				saida = saida + '\t\t\t'
			saida = saida + '\n'
		return saida