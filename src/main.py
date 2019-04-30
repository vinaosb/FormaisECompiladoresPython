import automato_finito
import gramatica_regular
import expressao_regular
import time

string = '0 0'
t_input = "0 0".split()
mode = 0
t_open = ''
n_open = 0
listas = {}
nome_dict = {}
l = len(t_input)
listas['af'] = []
listas['gr'] = []
listas['er'] = []
while t_input[0] != 'exit':
	if mode == 0:
		print('Menu inicial')
	t_input = input().split()
	l = len(t_input)
	if mode == 0 and l > 0:
		if t_input[0] == 'help':
			print('new [af|gr|er] [nome]')
			print('edit [af|gr|er] [nome]')
			print('del [af|gr|er] [nome]')
			print('list')
			continue
		elif t_input[0] == 'new'  and l > 2:
			ling = None
			if t_input[1] == 'af':
				ling = automato_finito.AutomatoFinito(t_input[2])
			if t_input[1] == 'gr':
				ling = gramatica_regular.GramaticaRegular(t_input[2])
			if t_input[1] == 'er':
				ling = expressao_regular.ExpressaoRegular(nome=t_input[2])
			listas[t_input[1]].append(ling)
			t_open = t_input[1]
			n_open = len(listas[t_open])-1
			nome_dict[(t_open, t_input[2])] = n_open
			mode = 1
			continue
		elif t_input[0] == 'edit'  and l > 2:
			t_open = t_input[1]
			n_open = nome_dict[(t_open, t_input[2])]
			mode = 1
			continue
		elif t_input[0] == 'del'  and l > 2:
			del nome_dict[(t_input[1], t_input[2])]
			mode = 0
			continue
		elif t_input[0] == 'list':
			out = ''
			for key in listas.keys():
				out = out + key + ': '
				for ling in listas[key]:
					out = out + '[' + ling.nome + ']'
				out = out + '\n'
			print(out)
			continue
	elif mode == 1 and l > 0 :
		
		if t_input[0] == 'help':
			print('add [estado] [caractere] [estado]')
			print('inicial [estado]')
			print('final [add|rem] [estado]')
			print('to_afd (caso seja um er ou af)')
			print('to_gr (apenas para af)')
			print('uniao [automato] (apenas para af)')
			print('intersecao [automato] (apenas para af)')
			print('minimizar (apenas para af)')
			print('to_afnd (apenas para gr)')
			print('add [expressao] (somente para er)')
			print('print')
			continue
		elif t_input[0] == 'exit':
			mode = 0
			t_input = ' '
			continue
		elif t_input[0] == 'print':
			print(listas[t_open][n_open].print())
			continue
		if t_open == 'af' :
			if t_input[0] == 'add' and l > 3:
				listas[t_open][n_open].add_transicao(t_input[1], t_input[2], t_input[3])
				continue
			elif t_input[0] == 'inicial' and l>1:
				listas[t_open][n_open].set_estado_inicial(t_input[1])
				continue
			elif t_input[0] == 'final' and l>2:
				if t_input[1] == 'rem' :
					listas[t_open][n_open].rem_estado_final(t_input[2])
					continue
				elif t_input[1] == 'add':
					listas[t_open][n_open].add_estados_finais(t_input[2])
					continue
			elif t_input[0] == 'to_afd':
				af = listas[t_open][n_open].to_afd()
				af.nome = listas[t_open][n_open].nome + '_afd'
				t_open = 'af'
				listas[t_open].append(af)
				n_open = len(listas[t_open])-1
				nome_dict[(t_open, af.nome)] = n_open
				mode = 1
				continue
			elif t_input[0] == 'to_gr':
				gr = listas[t_open][n_open].to_gr()
				gr.nome = listas[t_open][n_open].nome + '_gr'
				t_open = 'gr'
				listas[t_open].append(gr)
				n_open = len(listas[t_open])-1
				nome_dict[(t_open, af.nome)] = n_open
				mode = 1
				continue
			elif t_input[0] == 'uniao' and l > 2:
				af = listas[t_open][n_open].uniao(listas[t_open][nome_dict[t_input[1]]])
				af.nome = listas[t_open][n_open].nome + '_U_' + listas[t_open][nome_dict[t_input[1]]].nome
				t_open = 'af'
				listas[t_open].append(af)
				n_open = len(listas[t_open])-1
				nome_dict[(t_open, af.nome)] = n_open
				mode = 1
				continue
			elif t_input[0] == 'intersecao' and l > 2:
				af = listas[t_open][n_open].intersecao(listas[t_open][nome_dict[t_input[1]]])
				af.nome = listas[t_open][n_open].nome + '_I_' + listas[t_open][nome_dict[t_input[1]]].nome
				t_open = 'af'
				listas[t_open].append(af)
				n_open = len(listas[t_open])-1
				nome_dict[(t_open, af.nome)] = n_open
				mode = 1
				continue
			elif t_input[0] == 'minimizar':
				af = listas[t_open][n_open].minimizar()
				af.nome = listas[t_open][n_open].nome + '_minimizado'
				t_open = 'af'
				listas[t_open].append(af)
				n_open = len(listas[t_open])-1
				nome_dict[(t_open, af.nome)] = n_open
				mode = 1
				continue
		elif t_open == 'gr':
			if t_input[0] == 'add' and l > 3:
				listas[t_open][n_open].add_regras(t_input[1], t_input[2], t_input[3])
				continue
			elif t_input[0] == 'inicial' and l > 1:
				listas[t_open][n_open].set_variavel_inicial(t_input[1])
				continue
			elif t_input[0] == 'to_afnd' and l > 0:
				af = listas[t_open][n_open].to_afnd()
				af.nome = listas[t_open][n_open].nome + '_afnd'
				t_open = 'af'
				listas[t_open].append(af)
				n_open = len(listas[t_open])-1
				nome_dict[(t_open, af.nome)] = n_open
				mode = 1
				continue
			elif t_input[0] == 'remove' and l > 3:
				listas[t_open][n_open].remove_regra(t_input[1], t_input[2], t_input[3])
				continue
			elif t_input[0] == 'print':
				print(listas[t_open][n_open].print())
				continue
		elif t_open == 'er':
			if t_input[0] == 'add' and l>1:
				listas[t_open][n_open].add_expressao(t_input[1])
				continue
			elif t_input[0] == 'to_afd':
				af = listas[t_open][n_open].to_afd()
				af.nome = listas[t_open][n_open].nome + '_afd'
				t_open = 'af'
				listas[t_open].append(af)
				n_open = len(listas[t_open])-1
				nome_dict[(t_open, af.nome)] = n_open
				mode = 1
				continue
	print('comando invalido')
