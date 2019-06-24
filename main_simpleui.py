#!/usr/bin/env python

##   Trabalho    Formais 2019-1
## Alunos: Bruno George de Moraes
##         Vinícius Schwinden Berkenbrock
##

from src import automato_finito as af
from src import gramatica_regular as gr
from src import gramatica_livre_de_contexto as glc
from src import expressao_regular as er
from src import crud
#GUI
import PySimpleGUI as sg


#print(sg.ListOfLookAndFeelValues() )
sg.ChangeLookAndFeel('LightGreen') # GreenMono  LightGreen
sg.SetOptions(text_justification='right')

expressoes = []
gramaticas = []
gramLC     = []
automatos  = []

lenaf = 0
lengr = 0
lenglc = 0
lener = 0
menu_def = [['Info', 'Sobre...'],]
###
columm_layout = [[]]


def entryAF(length, width):
    entryLayout = [[sg.InputText('', size=(3, 1)) for i in range(length)] for _ in range(width)] + [[sg.CloseButton("OK"), sg.CloseButton("Cancel")]]

    entryWin = sg.Window("Input AF").Layout(entryLayout)
    button, values = entryWin.Read()
    return values



tab1_layout = [ [sg.Text('ER', text_color='white', background_color='gray'), sg.Input(do_not_clear=False, key='_ER_'), sg.ReadFormButton('SubmitER', key='submitE')],
                [sg.Text('GR', text_color='white', background_color='gray'), sg.Multiline( size=(20, 7), key='_GR_'),  sg.ReadFormButton('SubmitGR', key='submitGR')],
                [sg.Text('GLC', text_color='white', background_color='gray'), sg.Multiline( size=(32, 11), key='_GLC_'),  sg.ReadFormButton('SubmitGLC', key='submitGLC')],
                [sg.Text('AF', text_color='white', background_color='gray'), sg.Text('Digite linha , coluna:', text_color='white', background_color='gray'),
                 sg.In(key='inROW', size=(8,1), pad=(1,1), justification='right', do_not_clear=True), sg.In(key='inCOL', size=(8,1), pad=(1,1), justification='right', do_not_clear=True), sg.ReadFormButton('SubmitAF',  key='submitA')],
                ]

tab2_layout = [ [sg.T('Carregar ER, AF, GR, GLC')],
              [sg.Button('Open')],
              [sg.T('Salvar ER, AF, GR, GLC')],
              [sg.Button('Save')] ]

tab3_layout = [ [sg.Radio('ER', "E1", default=True), sg.Radio('GR',"E1"), sg.Radio('GLC',"E1") ],
              [sg.Spin([i for i in range(0, lener )], initial_value=0, key='_selER_'), sg.Spin([i for i in range(0, lengr )], initial_value=0, key='_selGR_'), sg.Spin([i for i in range(0, lenglc )], initial_value=0, key='_selGLC_'), sg.Button('Edit') ],
              [ ],  #_selER_ _selGR_ _selGLC_
              [sg.T('Converter GR <-> AF'), sg.Button('ConvGR-AF')],
              [ ],
              [sg.Spin([i for i in range(0, len(automatos))], initial_value=0, key='_selAF_'), sg.Spin([i for i in range(0, len(automatos))], initial_value=0, key='_uniAF_'), sg.T('*Tupla AF metodos uniao e intersecao') ],
              [sg.Radio('AF0',"E2", default=True),sg.Radio('AF1',"E2"), sg.Button('EditAF') ],
              [sg.T('Converter AF <-> GR'), sg.Button('ConvAF-GR')],
              [sg.T('Converter AFND <-> AFD'), sg.Button('ConvAFND-AFD')],
              [sg.T('Minimizar AF'), sg.Button('minAF')],
              [sg.T('Uniao AF'), sg.Button('uniaoAF')],
              [sg.T('Interseção  AF'), sg.Button('interAF')],
              [sg.T('Reconhecer palavra AF'), sg.InputText('', size=(21, 1), key='_sentenca_'), sg.Button('checkAF')],
              [],
              [ ], ]


# Crud Interface
cr = crud.Crud()

layout = [  [sg.Menu(menu_def)],
            [sg.TabGroup([[sg.Tab('Entrada', tab1_layout),
             sg.Tab('Carregar/Salvar', tab2_layout),
             sg.Tab('Conversoes', tab3_layout)]] ,key='_TABGROUP_')],
             ]

ui = sg.Window(' Trabalho Formais by Bruno e Vinicius - 2019.1 ')
# Window layout
while True:

    event, values = ui.Layout(layout).Read()
    # layout = layout # appears to dynamically chagne layout but to fast to allow input??

    lenaf = len(automatos)
    lengr = len(gramaticas)
    lenglc = len(gramLC)
    lener = len(expressoes)

    #print(expressoes)
    print ('LEN {}'.format(len(expressoes)) )

    # --- Process buttons --- #
    if event is None or event == 'Sair':
        break
    elif event == 'Sobre...':
        sg.Popup('Segunda entrega  AF ER GR - 2019.1 - ')
        continue
    elif event == 'Edit':
        #_selER_ _selGR_ _selAF_ _uniAF_ _selGLC_
        layout = layout
        #ui.Update()
        ui.Element('_ER_').Update( (expressoes)[ int(values['_selER_']) ])
        ui.Element('_GR_').Update( (gramaticas)[ int(values['_selGR_']) ])
        ui.Element('_GLC_').Update( (gramLC)[ int(values['_selGLC_']) ])
        continue
    elif event == 'Open':
        ##
        expressoes = cr.load_expressoes()
        gramaticas = cr.load_gramaticas()
        gramLC     = cr.load_glcs()
        automatos  = cr.load_automatos()
        #print( (cr.load_expressoes) )
        layout = layout
        ui.Element('_ER_').Update( (expressoes)[0].print() )
        ui.Element('_GR_').Update( (gramaticas)[0].print() )
        ui.Element('_GLC_').Update((gramLC)[0].print() )
        continue
    elif event == 'Save':
        ##
        cr.save_expressoes(expressoes)
        cr.save_gramaticas(gramaticas)
        cr.save_glcs(gramLC)
        cr.save_automatos(automatos)
        continue
    elif event == 'submitE':
       exr = er.ExpressaoRegular( expr= values['_ER_'] + '#', nome= str(len(expressoes))  )
       #exr.nomear( str(len(expressoes)) )
       #n = exr.nome
       expressoes.append( exr )
       continue
    elif event == 'submitGR':
       gra =  gr.GramaticaRegular( values['_GR_'] )
       print( values['_GR_' ] )
       gramaticas.append(gra)
       continue
    elif event == 'submitGLC':
       gra = glc.GramaticaLivreContexto( values['_GLC_'] )
       print( values['_GLC_' ] )
       gramLC.append(gra)
       continue
    elif event == 'submitA':
       tab = entryAF( int(values['inCOL']), int(values['inROW']))
       af = automato_finito.AutomatoFinito()
       tab.split()
       af.set_estado_inicial(tab[0:0])
       #for [i:j] in tab:
        #af.add_transicao(j[0], i[1], [2]) #


       continue
    elif event == 'ConvGR-AF':
       ##
       af = gramaticas[int(values['_selGR_'])].to_afnd()
       automatos.append(af)
       continue
    elif event == 'ConvAF-GR':
       ##
       g = automatos[int(values['_selAF_'])].to_gr()
       gramaticas.append(g)
       continue
    elif event == 'ConvAFND-AFD':
       ##
       af = automatos[int(values['_selAF_'])].to_afd()
       automatos.append(af)
       continue
    elif event == 'minAF':
       ##
       automatos[int(values['_selAF_'])].minimizar()
       continue
    elif event == 'checkAF':
       ##
       automatos[int(values['_selAF_'])].checkAF( values['_sentenca_'] )
       continue
    elif event == 'interAF':
       ##
       af0 = automatos[int(values['_selAF_'])]
       af1 = automatos[int(values['_uniAF_'])]
       af0 = af0.intersecao(af1)
       continue
    elif event == 'uniaoAF':
       ##
       af0 = automatos[int(values['_selAF_'])]
       af1 = automatos[int(values['_uniAF_'])]
       af0 = af0.uniao(af1)
       continue

    #ui.Close()
