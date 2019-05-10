#!/usr/bin/env python

import automato_finito
import gramatica_regular
import expressao_regular
import crud
#GUI
import PySimpleGUI as sg  

sg.ChangeLookAndFeel('BlueMono')
sg.SetOptions(text_justification='right')      

columm_layout = [[]]
MAX_ROWS = 8
MAX_COL = 7
for i in range(MAX_ROWS):
   inputs = [sg.T('{}'.format(i), size=(4,1), justification='right')] + [sg.In(size=(10, 1), pad=(1, 1), justification='right', key=(i,j), do_not_clear=True) for j in range(MAX_COL)]
   columm_layout.append(inputs)


menu_def = [['Info', 'Sobre...'],]

tab1_layout = [ [sg.Text('ER', text_color='white', background_color='gray'), sg.Input(do_not_clear=True, key='_ER_')],
        [sg.ReadFormButton('SubmitER', button_color=('gray34','azure2'), key='submitE')],
        [sg.Text('GR', text_color='white', background_color='gray'), sg.Multiline( size=(42, 11), key='_GR_')],
        [sg.ReadFormButton('SubmitGR', button_color=('gray34','azure2'), key='submitG')],

                
        [sg.Text('AF', text_color='white', background_color='gray'), sg.Text('Digite linha , coluna:', text_color='white', background_color='gray'),        
            sg.In(key='inROW', justification='right', size=(8,1), pad=(1,1), do_not_clear=True),
            sg.In(key='inCOL', size=(8,1), pad=(1,1), justification='right', do_not_clear=True)],
        [sg.Column(columm_layout, size=(604,212),  key='_AF_', scrollable=True)],
        [sg.ReadFormButton('SubmitAF', button_color=('gray34','azure2'), key='submitA')] ]

tab2_layout = [ [sg.T('Carregar ER, AF, GR')],
              [sg.Button('Open')],
              [sg.T('Salvar ER, AF, GR')],
              [sg.Button('Save')] ]
               
tab3_layout = [ [sg.In(key='_in2_')] ]


# Window layout
layout = [  [sg.Menu(menu_def)],
            [sg.TabGroup([[sg.Tab('Entrada', tab1_layout), sg.Tab('Carregar/Salvar', tab2_layout), sg.Tab('Conversoes', tab3_layout)]], key='_TABGROUP_')],
            [sg.Button('Sair')] ]

# Display the window and get values

while True:
    event, values = sg.Window(' Trabalho Formais by Bruno e Vinicius - 2019.1 ').Layout(layout).Read()
    #sg.PopupNonBlocking('button = %s' % event, 'Values dictionary', values)

    # --- Process buttons --- #
    if event is None or event == 'Sair':
        break
    elif event == 'Sobre...':
        sg.Popup('Primeira entrega  AF ER GR - 2019.1 - ')
    elif event == 'submitE':
       exr =  expressao_regular( values['_ER_'] )
       print( values['_ER_'] )
    elif event == 'submitG':
       gra =  gramatica_regular( values['_GR_'] )
       print( values['_GR_' ] )
    elif event == 'Open':
            ##
        expressoes = crud.load_expressoes()
    elif event == 'Save':
        ##
          
         continue

         
# valores recebidos como dicionario
#print(event, values['_ER_'], values['_AF_'], values['_GR_']) 

