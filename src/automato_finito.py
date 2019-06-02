##   Trabalho Formais 2019-1
## Alunos: Bruno George de Moraes
##         Vinícius Schwinden Berkenbrock
##
from src import gramatica_regular

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
		for x in self.transicoes.keys():
			lista = lista.union(set(x[1]))
		lista = lista - set('&')
		return lista

# retorna o conjunto de caracteres que compõe o alfabeto do automato
	def alfabetoComE(self):
		lista = set()
		for x in self.transicoes.keys():
			lista = lista.union(set(x[1]))
		lista = lista
		return lista

# imprime a tabela de transicoes do automato
	def print(self):
		saida = ''
		nome = 'estado'
		alfabeto = self.alfabetoComE()
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
	def to_afd(self, count=0, novos={}):
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

#realiza a uniao de dois automatos e retorna o automato resultante
	def uniao(self, at):
		novo = AutomatoFinito()
		a_1 = self.alfabeto()
		a_2 = at.alfabeto()
		k_1 = self.transicoes.keys()
		k_2 = at.transicoes.keys()
		alfabeto = a_1.union(a_2)
		novos_estados = set()
		novos_estados = novos_estados.union(((self.inicial, at.inicial),))
		novo.add_estado(self.inicial + '_' + at.inicial)
		novo.set_estado_inicial(self.inicial + '_' + at.inicial)
		while len(novos_estados) > 0:
			proximos = set()
			for e in novos_estados:
				for a in alfabeto:
					if (e[0], a) in k_1:
						ef_1 = self.transicoes[(e[0], a)][0]
					else:
						ef_1 = '&'
					if (e[1], a) in k_2:
						ef_2 = at.transicoes[(e[1], a)][0]
					else:
						ef_2 = '&'

					
					i = e[0] + '_' + e[1]
					if ef_1 == '&' and ef_2 == '&':
						f = '&'
					else:
						f = ef_1 + '_' + ef_2
					if not f in novo.estados:
						proximos.add((ef_1, ef_2),)
					novo.add_transicao(i, a, f)
					if (ef_1 in self.finais) or (ef_2 in at.finais):
						novo.add_estados_finais(f)
					if (e[0] in self.finais) or (e[1] in at.finais):
						novo.add_estados_finais(i)
			novos_estados = proximos
		novo.estados.remove('&_&')
		novo.estados.remove('&')
		return novo

	#realiza a intersecao de dois automatos e retorna o automato resultante
	def intersecao(self, at):
		novo = AutomatoFinito()
		a_1 = self.alfabeto()
		a_2 = at.alfabeto()
		k_1 = self.transicoes.keys()
		k_2 = at.transicoes.keys()
		alfabeto = a_1.union(a_2)
		novos_estados = set()
		novos_estados = novos_estados.union(((self.inicial, at.inicial),))
		novo.add_estado(self.inicial + '_' + at.inicial)
		novo.set_estado_inicial(self.inicial + '_' + at.inicial)
		while len(novos_estados) > 0:
			proximos = set()
			for e in novos_estados:
				for a in alfabeto:
					if (e[0], a) in k_1:
						ef_1 = self.transicoes[(e[0], a)][0]
					else:
						ef_1 = '&'
					if (e[1], a) in k_2:
						ef_2 = at.transicoes[(e[1], a)][0]
					else:
						ef_2 = '&'

					
					i = e[0] + '_' + e[1]
					if ef_1 == '&' and ef_2 == '&':
						f = '&'
					else:
						f = ef_1 + '_' + ef_2
					if not f in novo.estados:
						proximos.add((ef_1, ef_2),)
					novo.add_transicao(i, a, f)
					if (ef_1 in self.finais) and (ef_2 in at.finais):
						novo.add_estados_finais(f)
					if (e[0] in self.finais) and (e[1] in at.finais):
						novo.add_estados_finais(i)
			novos_estados = proximos
		novo.estados.remove('&_&')
		novo.estados.remove('&')
		return novo

	#remove os estados inalcancaveis do automato
	def remover_estados_inalcancaveis(self):
		estados_alcancaveis = set()
		transicoes_alcancaveis = {}
		novos_estados = set()
		novos_estados.add(self.inicial)
		alfabeto = self.alfabeto()
		while len(novos_estados) > 0:
			proximos = set()
			for e in novos_estados:
				estados_alcancaveis.add(e)
				for a in alfabeto:
					if (e,a) in self.transicoes.keys():
						transicoes_alcancaveis[(e,a)] = [self.transicoes[(e, a)][0]]
						n = self.transicoes[(e, a)][0]
						if n != '&' and not n in estados_alcancaveis:
							proximos.add(n)
			novos_estados = proximos
		self.estados = estados_alcancaveis
		self.transicoes = transicoes_alcancaveis

#remove os estados mortos do automato
	def remover_estados_mortos(self):
		estados_nao_mortos = set()
		transicoes_nao_mortas = {}
		novos_estados = set()
		novos_estados = self.finais
		while len(novos_estados) > 0:
			proximos = set()
			for e in novos_estados:
				estados_nao_mortos.add(e)
				for key , value in self.transicoes.items():
					if e == value[0]:
						transicoes_nao_mortas[key] = [self.transicoes[key][0]]
						if not key[0] in estados_nao_mortos:
							proximos.add(key[0])
			novos_estados = proximos
		self.estados = estados_nao_mortos
		self.transicoes = transicoes_nao_mortas


	def remover_estados_equivalentes(self):
		af = AutomatoFinito()
		estados = []
		e1 = []
		e2 = []
		for e in (frozenset(self.estados - self.finais)):
			e1.append((e, True, False))
		for e in (frozenset(self.finais)):
			e2.append((e, False, True))
		estados.append(e1)
		estados.append(e2)
		print(estados)
		estados = self.separar_estados(estados)
		print(estados)
		for e in estados:
			inicial = False
			final = False
			for x in e:
				if x[1]:
					inicial = True
				if x[2]:
					final = True
			print(e)
			#for keys in self.transicoes.keys()
			if inicial:
				af.inicial = e[0][0]
			if final:
				af.finais.add(e[0][0])
		return af

	def separar_estados(self, estados):
		transicoes = {}
		novos_estados = []
		count = 0
		for e in estados:
			for z in e:
				x = z[0]
				existe = [True] * len(novos_estados)
				for a in self.alfabeto():
					if (x, a) in self.transicoes.keys():
						for i in range(len(novos_estados)):
							if not (i, a) in transicoes.keys():
								existe[i] = False
							else:
								if not self.transicoes[(x, a)] == transicoes[(i, a)]:
									existe[i] = False
					else:
						for i in range(len(novos_estados)):
							if (i, a) in transicoes.keys():
								existe[i] = False
						#if len(novos_estados) == 0:
						#	existe[i] = False
				existiu = False
				for i in range(len(existe)):
					if existe[i]:
						novos_estados[i].append((x, x == self.inicial, x in self.finais))
						existiu = True
				if not existiu:
					novos_estados.append([(x, x == self.inicial, x in self.finais)])
					for a in self.alfabeto():
						if (x, a) in self.transicoes.keys():
							transicoes[(count, a)] = self.transicoes[(x, a)]
					count = count + 1
		if len(novos_estados) == len(estados):
			return novos_estados
		else:
			return self.separar_estados(novos_estados)

	def minimizar(self):
		at = AutomatoFinito()
		at = self
		at.remover_estados_mortos()
		at.remover_estados_inalcancaveis()
		at.remover_estados_equivalentes()
		return at
