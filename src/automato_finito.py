import gramatica_regular

class AutomatoFinito:
	estados = set()
	transicoes = {}
	inicial = ''
	finais = set()
	nome = ''

	def __init__(self, nome=''):
		self.estados = set()
		self.transicoes = {}
		self.inicial = ''
		self.finais = set()
		self.nome = nome

#adiciona um novo estado ao automato
	def add_estado(self, estado):
		self.estados = self.estados.union((estado,))

#indica qual o estado inicial do automato
	def set_estado_inicial(self, estado):
		if (estado in self.estados):
			self.inicial = estado
		else:
			print('estado ', estado , ' nao existe')

#adiciona um novo estado final
	def add_estados_finais(self, estado):
		if (estado in self.estados):
			self.finais = self.finais.union((estado,))
		else:
			print('estado ', estado , ' nao existe')

# remove um estado final
	def rem_estado_final(self, estado):
		if (estado in self.finais):
			self.finais.remove(estado)
		else:
			print('Estado final não existe')

#adiciona uma transicao ao automato
	def add_transicao(self, ei, ch, ef):
		self.add_estado(ei)
		self.add_estado(ef)
		if ((ei, ch) in self.transicoes.keys()):
			if not ef in self.transicoes[(ei, ch)]:
				self.transicoes[(ei, ch)].append(ef)
		else:
			self.transicoes[(ei, ch)] = [ef]

#remove uma transicao do automato
	def rem_transicao(self, ei, ch, ef):
		if ((ei, ch) in self.transicoes.keys()):
			if len(self.transicoes[(ei, ch)]) > 1:
				if ef in self.transicoes[(ei, ch)]:
					self.transicoes[(ei, ch)].remove(ef)
			else:
				del self.transicoes[(ei, ch)]
		else:
			print('transicao nao existe')


#verifica se o automato reconhece uma palavra, retorna true caso reconheca
	def check(self, palavra) -> bool:
		atual = self.inicial
		for ch in palavra:
			if ((atual, ch) in self.transicoes.keys()):
				atual = self.transicoes[(atual, ch)][0]
			else:
				return False
		if atual in self.finais:
			return True
		else:
			return False

# retorna o conjunto de caracteres que compõe o alfabeto do automato
	def alfabeto(self):
		lista = set()
		count = 0
		for x in self.transicoes.keys():
			lista = lista.union(set(x[1]))
			count = count + 1
		lista = lista - set('&')
		return lista


# imprime a tabela de transicoes do automato
	def print(self):
		saida = ''
		nome = 'estado'
		alfabeto = self.alfabeto()
		temp = "-----------------"
		saida = saida + f'|{nome:15}|'
		for a in alfabeto:
			saida = saida + f'{a:15}|'
			temp = temp + "-----------------"
		saida = saida + '\n'
		saida = temp + "\n" + saida + temp + "\n"
		for e in self.estados:
			es = e
			if e == self.inicial:
				es = '->' + e
			if e in self.finais:
				es = es + '*'
			saida = saida + f'|{es:15}|'
			for a in alfabeto:
				est = ''
				if (e,a) in self.transicoes.keys():
					for t in self.transicoes[(e,a)]:
						est = est + t + ','
				else:
					est = '&'
				saida = saida + f'{est:15}|'
			saida = saida + '\n'
		return saida


# funcao que retorna um afd a partir de um automato finito
# se o automato ja estiver determinizado não haverá mudancas
# recebe como parametro 0 e {} inicialmente
	def to_afd(self, count, novos):
		repetir = False
		afd = AutomatoFinito()
		for e in self.estados:
			estados_extras = []
			if (e, '&') in self.transicoes.keys():
				for t in self.transicoes[(e, '&')]:
					estados_extras = estados_extras.append((t,))
			for a in self.alfabeto():
				if ((e, a) in self.transicoes.keys()):
					afd.add_estado(e)
					if e == self.inicial:
						afd.set_estado_inicial(e)
					if (len(self.transicoes[(e, a)]) > 1):
						novo_estado = set()
						novo_estado = novo_estado.union(estados_extras).union(self.transicoes[(e, a)])
						final = False
						for t in novo_estado:
							if t in self.finais:
								final = True
						re_novo = set()
						for n in novo_estado:
							if n[0] == '_':
								ctx = int(n[1:-1])
								for est, ct in novos.items():
									if ct == ctx:
										re_novo = re_novo.union(est)
							else:
								re_novo = re_novo.union((n,))
						novo_estado = re_novo
						refaz = False
						if novo_estado in frozenset(novos):
							count = novos[frozenset(novo_estado)]
							x = '_' + str(count) + '_'
						else:
							novos[frozenset(novo_estado)] = count
							x = '_' + str(count) + '_'
							count = count + 1
							refaz = True
						afd.add_estado(x)
						afd.add_transicao(e, a, x)
						if refaz:
							for b in self.alfabeto():
								for nova in novo_estado:								
									if (nova, b) in self.transicoes.keys():
										afd.add_transicao(x, b, self.transicoes[(nova, b)][0])
								if len(afd.transicoes[(x, b)]) > 1:
									repetir = True
						if final:
							afd.add_estados_finais(x)
					else:
						afd.add_estado(self.transicoes[(e, a)][0])
						afd.add_transicao(e, a, self.transicoes[(e, a)][0])
						if self.transicoes[(e, a)][0] in self.finais:
							afd.add_estados_finais(self.transicoes[(e, a)][0])
		if repetir:
			return afd.to_afd(count, novos)
		else:
			return afd

#converte o automato em uma gramatica regular
	def to_gr(self):
		gr = gramatica_regular.GramaticaRegular()
		gr.variaveis = self.estados
		gr.inicial = self.inicial
		for t in self.transicoes.keys():
			if self.transicoes[t][0] in self.finais:
				gr.add_regras(t[0], t[1], '&')
			else:
				gr.add_regras(t[0], t[1], self.transicoes[t][0])
		if self.inicial in self.finais:
			gr.add_regras(self.inicial, '&', '&')
		return gr