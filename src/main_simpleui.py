#!/usr/bin/env python

import automato_finito
import gramatica_regular
import expressao_regular
import crud
#GUI
import PySimpleGUI as sg  

sg.ChangeLookAndFeel('BlueMono')
sg.SetOptions(text_justification='right')      



def table():
   columm_layout = [[]]
   MAX_ROWS = 20
   MAX_COL = 10
   for i in range(MAX_ROWS):
        inputs = [sg.T('{}'.format(i), size=(4,1), justification='right')] + [sg.In(size=(10, 1), pad=(1, 1), justification='right', key=(i,j), do_not_clear=True) for j in range0(MAX_COL)]
        columm_layout.append(inputs)


## def afTable         
##        [sg.Text('AF - Digite linha , coluna e valor:', text_color='white', background_color='gray'),        
##            sg.In(key='Linha de entrada', justification='right', size=(8,1), pad=(1,1), do_not_clear=True),
##            sg.In(key='Coluna de entrada', size=(8,1), pad=(1,1), justification='right', do_not_clear=True),
##            sg.In(key='valor', size=(8,1), pad=(1,1), justification='right', do_not_clear=True)],
##        #
##         [sg.Column(columm_layout, size=(800,600), scrollable=True)]]
##        ]]#, key='_AF_'

menu_def = [['Info', 'Sobre...'],]

tab1_layout = [ [sg.Text('ER', text_color='white', background_color='gray'), sg.Input(do_not_clear=True, key='_ER_')],
        [sg.ReadFormButton('SubmitER', button_color=('gray34','azure2'), key='submit')],
        [sg.Text('GR', text_color='white', background_color='gray'), sg.Multiline( size=(42, 11), key='_GR_')],
        [sg.ReadFormButton('SubmitGR', button_color=('gray34','azure2'), key='submit')] ]

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
    elif event == 'Open':
            ##
        expressoes = crud.load_expressoes()
    elif event == 'Save':
        ##
        values['_ER_'] 
        crud.save_expressoes( expressoes )
        
 

# valores recebidos como dicionario
#print(event, values['_ER_'], values['_AF_'], values['_GR_']) 

