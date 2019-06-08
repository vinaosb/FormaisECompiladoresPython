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


sg.ChangeLookAndFeel('BlueMono')
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
    ##TODO format values in AF
    print(','.join(values))



tab1_layout = [ [sg.Text('ER', text_color='white', background_color='gray'), sg.Input(key='_ER_'), sg.ReadFormButton('SubmitER', button_color=('gray34','azure2'), key='submitE')],
                [sg.Text('GR', text_color='white', background_color='gray'), sg.Multiline( size=(42, 11), key='_GR_'),  sg.ReadFormButton('SubmitGR', button_color=('gray34','azure2'), key='submitGR')],
                [sg.Text('GLC', text_color='white', background_color='gray'), sg.Multiline( size=(42, 11), key='_GLC_'),  sg.ReadFormButton('SubmitGLC', button_color=('gray34','azure2'), key='submitGLC')],
                [sg.Text('AF', text_color='white', background_color='gray'), sg.Text('Digite linha , coluna:', text_color='white', background_color='gray'),
                 sg.In(key='inROW', size=(8,1), pad=(1,1), justification='right', do_not_clear=True), sg.In(key='inCOL', size=(8,1), pad=(1,1), justification='right', do_not_clear=True), sg.ReadFormButton('SubmitAF', button_color=('gray34','azure2'), key='submitA')],
                ]

tab2_layout = [ [sg.T('Carregar ER, AF, GR, GLC')],
              [sg.Button('Open')],
              [sg.T('Salvar ER, AF, GR, GLC')],
              [sg.Button('Save')] ]

tab3_layout = [ [sg.T('select ER, AF, GR, GLC')],
              [ ],  #_selER_ _selGR_ _selAF_ _selGLC_
              [sg.T('Converter GR <-> AF')],
              [sg.Button('ConvGR-AF')],
              [ ],
              [sg.Spin([i for i in range(1, 2 )], initial_value=1, key='_selAF_'), sg.Text('select AF')],
              [sg.T('Converter AF <-> GR'), sg.Button('ConvAF-GR')],
              [sg.T('Converter AFND <-> AFD'), sg.Button('ConvAFND-AFD')],
              [sg.T('Minimizar AF'), sg.Button('minAF')],
              [sg.T('Uniao AF'), sg.Button('uniaoAF')],
              [sg.T('interseção  AF'), sg.Button('interAF')],
              [sg.T('Reconhecer palavra AF'), sg.InputText('sentenca', key='_sentenca_')],
              [sg.Button('checkAF')],
              [ ], ]

# Window layout

layout = [  [sg.Menu(menu_def)],
            [sg.TabGroup([[sg.Tab('Entrada', tab1_layout),
             sg.Tab('Carregar/Salvar', tab2_layout),
             sg.Tab('Conversoes', tab3_layout)]] ,key='_TABGROUP_')],
         ]

# Display the window and get values
ui = sg.Window(' Trabalho Formais by Bruno e Vinicius - 2019.1 ')

# Crud Interface
cr = crud.Crud()

while True:
    event, values = ui.Layout(layout).Read()

    lenaf = len(automatos)
    lengr = len(gramaticas)
    lenglc = len(gramLC)
    lener = len(expressoes)

    #print(expressoes)
    #print ('LEN {}'.format(len(expressoes)) )

    # --- Process buttons --- #
    if event is None or event == 'Sair':
        break
    elif event == 'Sobre...':
        sg.Popup('Segunda entrega  AF ER GR - 2019.1 - ')
        continue
    elif event == 'Open':
        ##
        expressoes = cr.load_expressoes()
        gramaticas = cr.load_gramaticas()
        gramLC     = cr.load_glcs()
        automatos  = cr.load_automatos()
        print( (cr.load_expressoes) )
        ui.Element('_ER_').Update( (expressoes)[0] )
        ui.Element('_GR_').Update( (gramaticas)[1].print() )
        ui.Element('_GLC_').Update((gramLC)[2].print() )
        continue
    elif event == 'Save':
        ##
        cr.save_expressoes(expressoes)
        cr.save_gramaticas(gramaticas)
        cr.save_glcs(gramLC)
        cr.save_automatos(automatos)
        continue
    elif event == 'submitE':
       exr = er.ExpressaoRegular( values['_ER_'] + '#' )
       exr.nomear( str(len(expressoes)) )
       print ( exr.nome )
       expressoes.append(exr)
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
       entryAF( int(values['inCOL']), int(values['inROW']))
      ## sg.Column(columm_layout, size=(604,212),  key='_AF_', scrollable=True)
      ##
      # ##Table(  values,
      #   headings=None,
      #   visible_column_map=None,
      #   col_widths=None,
      #   def_col_width=10,
      #   auto_size_columns=True,
      #   max_col_width=20,
      #   select_mode=None,
      #   display_row_numbers=False,
      #   num_rows=None,
      #   row_height=None,
      #   font=None,
      #   justification='right',
      #   text_color=None,
      #   background_color=None,
      #   alternating_row_color=None,
      #   row_colors=None,
      #   vertical_scroll_only=True,
      #   size=(None,None),
      #   change_submits=False,
      #   enable_events=False,
      #   bind_return_key=False,
      #   pad=None,
      #   key=None,
      #   tooltip=None,
      #   right_click_menu=None,
      #   visible=True):
      #
      ##
       continue
    elif event == 'ConvGR-AF':
       ##
       af = gramaticas[ values['_selGR_'] ].to_afnd()
       automatos.append(af)
       continue
    elif event == 'ConvAF-GR':
       ##
       g = automatos[values['_selAF_']].to_gr()
       gramaticas.append(g)
       continue
    elif event == 'ConvAFND-AFD':
       ##
       af = automatos[values['_selAF_']].to_afd()
       automatos.append(af)
       continue
    elif event == 'minAF':
       ##
       automatos[values['_selAF_']].minimizar()
       continue
    elif event == 'checkAF':
       ##
       automatos[values['_selAF_']].checkAF( values['_sentenca_'] )
       continue
    elif event == 'interAF':
       ##
       af0 = automatos[values['_selAF_']]
       af1 = automatos[values['_intersecAF_']]
       automatos[values['_selAF_']] = af0.intersecao(af1)
       continue
    elif event == 'uniaoAF':
       ##
       af0 = automatos[values['_selAF_']]
       af1 = automatos[values['_uniAF_']]
       automatos[values['_selAF_']] = af0.uniao(af1)
       continue
