##   Trabalho Formais 2019-1
## Alunos: Bruno George de Moraes
##         Vin�cius Schwinden Berkenbrock
##


from src import automato_pilha

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

	def remProducao(self,nt,prod):
		self.regrasProd[nt].remove(prod)

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
			for t in self.terminal.union({"$"}):
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
	
	def calcAceitacao(self, expr):
		return self.convertToAP().check(expr)

	# Chomsky usa Z como estado inicial
	def Chomsky(self):
		# Eliminar simbolo inicial do lado direito de outras producoes
		# Adicionar Z -> S como simbolo inicial
		self.addNaoTerminal('Z')
		self.addProducao('Z', self.inicial)
		self.defInicial('Z')
		aux = set()
		# Criar regra para levar de um nao terminal novo para um terminal | A -> a
		for termi in self.terminal:
			i = self.genNewSimb()
			self.addNaoTerminal(i)
			self.addProducao(i,termi)
			aux.add(i)

		newRegrasProd = dict()
		

		# Olha as producoes que tem A-> BcD e transforma em A->BCD
		for nt in self.naoTerminal:
			newRegrasProd[nt] = set()
			if nt not in aux:
				for prod in self.regrasProd[nt]:
					newprod = ""
					for i in range(0,len(prod)):
						if prod[i] in self.naoTerminal:
							newprod += prod[i]
						else:
							for a in aux:
								if prod[i] in self.regrasProd[a]:
									newprod += a
					newRegrasProd[nt].add(newprod)
			else:
				newRegrasProd[nt] = self.regrasProd[nt]
			
		self.regrasProd = newRegrasProd.copy()

		# Elimina producoes com mais de 2 nao terminais | A -> BCD = A ->BE & E -> CD
		newRegrasProd.clear()

		newNaoTerminais = set()
		added = True
		while(added):
			added = False
			i = 0
			for nt in self.naoTerminal:
				newNaoTerminais.add(nt)
				newRegrasProd[nt] = set()
				for prod in self.regrasProd[nt]:
					if (len(prod) < 3 and len(prod) > 0):
						newRegrasProd[nt].add(prod)
					elif len(prod) > 0:
						aux = self.genNewSimb(i)
						i += 1
						added = True
						newRegrasProd[nt].add(prod[0] + aux)
						newNaoTerminais.add(aux)
						newRegrasProd[aux] = set()
						newRegrasProd[aux].add(prod[1:])

			for nnt in newNaoTerminais:
				if nnt not in self.naoTerminal:
					self.addNaoTerminal(nnt)
			newNaoTerminais.clear()
			self.regrasProd = newRegrasProd.copy()
			newRegrasProd.clear()


		# Remove & producoes
		self.remEpsulonProducoes()
		
		# Remove Producoes Unitarias
		newRegrasProd.clear()
		for nt in self.naoTerminal:
			newRegrasProd[nt] = set()

			if nt not in aux:
				newRegrasProd[nt] = self.addProdUni(nt)
			else:
				newRegrasProd[nt] = self.regrasProd[nt]

		self.regrasProd = newRegrasProd.copy()

		newRegrasProd.clear()

		# Remove Nao terminais Equivalentes (iguais) (maioria - 90% funcional)
		remv = True
		nextDel = set()
		aux = set()
		aux2 = dict()
		while(remv):
			remv = False
			aux.clear()
			for nt in self.naoTerminal:
				for ntt in self.naoTerminal:
					if nt != ntt and self.regrasProd[nt].issubset(self.regrasProd[ntt]) and self.regrasProd[ntt].issubset(self.regrasProd[nt]) and ntt+nt not in aux and nt+ntt not in aux:
						aux.add(ntt + nt)
			aux2.clear()
			for a in aux:
				for nt in self.naoTerminal:
					aux2[nt] = dict()
					if nt != a[1]:
						for prod in self.regrasProd[nt]:
							if a[0] in prod:
								for i in range(0,len(prod)):
									if a[0] == prod[i]:
										aux2[nt][prod] = a[0] + prod[:i] + a[1] + prod[i+1:]
			for nt in self.naoTerminal:
				for prod, res in aux2[nt].items():
					self.regrasProd[nt].remove(prod)
					self.regrasProd[nt].add(res[1:])
					nextDel.add(res[0])
			for nd in nextDel:
				self.regrasProd.pop(nd)
				self.naoTerminal.remove(nd)
				remv = True
			nextDel.clear()
		
		# Estados Inalcancaveis
		temp = self.removeInalcancaveis(self.inicial)

		for k in self.naoTerminal.difference(temp):
			self.regrasProd.pop(k)
			self.naoTerminal.remove(k)

	def removeInalcancaveis(self, nt):
		ret = set()
		for prod in self.regrasProd[nt]:
			for i in range(0,len(prod)):
				if prod[i] in self.terminal:
					ret.add(nt)
					break
				else:
					ret = ret.union(self.removeInalcancaveis(prod[i]))
					ret.add(nt)
		return ret

	def remEpsulonProducoes(self):
		novo = GramaticaLivreContexto("temporario")
		novo.terminal = self.terminal
		conjE = self.idProducaoComEpsulon()

		for nt in self.naoTerminal:
			novo.addNaoTerminal(nt)
			for prod in self.regrasProd[nt]:
				if prod != "&":
					novo.addProducao(nt,prod)
		
		adc = True
		while(adc):
			adc = False
			for nt in novo.naoTerminal:
				aux2 = set()
				for prod in novo.regrasProd[nt]:
					if len(prod) > 1:
						for i in range(0,len(prod)):
							if prod[i] in conjE:
								aux = prod[:i]
								aux = prod[i+1:]
								if aux not in novo.regrasProd[nt]:
									aux2.add(aux)
									adc = True
				for added in aux2:
					novo.addProducao(nt,added)
		
		if self.inicial in conjE:
			novoInicial = novo.genNewSimb()
			novo.addNaoTerminal(novoInicial)
			novo.addProducao(novoInicial, '&')
			novo.addProducao(novoInicial, self.inicial)
		else:
			novo.defInicial(self.inicial)
		
		self.terminal = novo.terminal
		self.naoTerminal = novo.naoTerminal
		self.regrasProd = novo.regrasProd
		self.inicial = novo.inicial

	def idProducaoComEpsulon(self):
		mod = True
		e = set()
		e.add('&')
		while(mod):
			mod = False
			# X E N
			for nt in self.naoTerminal:
				# X !E E
				if nt not in e:
					# Existe uma producao de X em E
					for prod in self.regrasProd[nt]:
						if prod in e:
							e.add(nt)
							mod = True
							break
		return e

	def addProdUni(self, nt):
		newRegrasProd = set()
		if nt in self.terminal:
			newRegrasProd.add(nt)
		else:
			for prod in self.regrasProd[nt]:
				if (len(prod) == 1):
					for n in self.addProdUni(prod):
						newRegrasProd.add(n)
				else:
					newRegrasProd.add(prod)
		return newRegrasProd

	def Fatoracao(self):
		added = True
		aux = dict()
		aux2 = dict()
		aux3 = set() # Nao Terminais a adicionar
		while(added):
			aux.clear() # Producoes a adicionar
			aux2.clear() # Producoes a remover
			added = False
			j = 0
			for nt in self.naoTerminal:
				aux[nt] = set()
				aux2[nt] = set()
				for prod1 in self.regrasProd[nt]:
					for prod2 in self.regrasProd[nt]:
						if prod1 != prod2:
							k = -1
							for i in range(0, min(len(prod1),len(prod2))):
								if prod1[i] != prod2[i]:
									break
								k=i
							if k >= 0:
								novo = self.genNewSimb(j)
								j+=1
								aux[nt].add(prod1[0:k] + novo)
								aux2[nt].add(prod1)
								aux2[nt].add(prod2)
								aux3.add(novo)
								aux[novo] = set()
								aux[novo].add(prod1[k+1:])
								aux[novo].add(prod2[k+1:])
			for nt in aux3:
				if nt not in self.naoTerminal:
					self.addNaoTerminal(nt)
			for nt,prods in aux.items():
				for prod in prods:
					self.addProducao(nt,prod)
			for nt,prods in aux2.items():
				for prod in prods:
					self.remProducao(nt,prod)

	# Gera um novo simbolo para gramatica (função auxiliar)
	def genNewSimb(self, j = 0):
		temp = "A"
		for i in range(j,25):
			if chr(ord(temp)+ i) not in self.naoTerminal and chr(ord(temp)+ i) not in self.terminal:
				return chr(ord(temp)+ i)
		temp = "a"
		k = j - 24
		if k < 0:
			k = 0
		for i in range(k,26):
			if chr(ord(temp)+ i) not in self.naoTerminal and chr(ord(temp)+ i) not in self.terminal:
				return chr(ord(temp)+ i)
		l = k - 25
		if l < 0:
			l = 0
		for i in range(l,10):
			if str(i) not in self.naoTerminal and str(i) not in self.terminal:
				return str(i)

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
		for t in self.terminal.union({"$"}):
			saida = saida + t + '\t\t\t'
		saida = saida + '\n'

		for nt in self.naoTerminal:
			saida = saida + nt + '\t'
			for t in self.terminal.union({"$"}):
				for pt in self.preditiveTable[nt][t]:
					saida = saida + pt + ' '
				saida = saida + '\t\t\t'
			saida = saida + '\n'
		return saida

	def convertToAP(self):
		ap = automato_pilha.AutomatoPilha(self.nome + "1")
		self.calcPred()

		for nt in self.naoTerminal:
			ap.addAlfaPilha(nt)
			for t in self.terminal:
				ap.addAlfaEntr(t)
				ap.addAlfaPilha(t)
				ap.addEstado()
		return ap
		