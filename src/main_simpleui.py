#!/usr/bin/env python

import sys
import PySimpleGUI as sg  

sg.ChangeLookAndFeel('BlueMono')
sg.SetOptions(text_justification='right')      



tab1_layout =  [[sg.Text('ER', text_color='white', background_color='gray'), sg.Input(do_not_clear=True, key='_ER_')],
        [sg.Text('AF', text_color='white', background_color='gray'), sg.Input(do_not_clear=True, key='_AF_')],        
        [sg.Text('GR', text_color='white', background_color='gray'), sg.Multiline( size=(42, 11), key='_GR_')],
        [sg.Submit(), sg.Cancel()]]

tab2_layout = [
               [sg.In(key='_in2_')]]
tab3_layout = [
               [sg.In(key='_in2_')]]


# Window layout
layout = [
         [sg.TabGroup([[sg.Tab('Entrada', tab1_layout),
            sg.Tab('Salvo', tab2_layout), sg.Tab('Conversoes', tab3_layout)]])],  
         ]

# Display the window and get values
#    while True:
event, values = sg.Window(' Trabalho Formais by Bruno e Vinicius - 2019.1 ').Layout(layout).Read()
#    if event == 'EXIT'  or event is None:      
#        break # exit button clicked
#    if event == 'script1':      
#    ExecuteCommandSubprocess('pip', 'list')      
#    elif event == 'script2':      
#    ExecuteCommandSubprocess('python', '--version')      
#   elif event == 'Run':      
#    ExecuteCommandSubprocess(value[0])      

# salvar editar:  valores recebidos como dicionario
print(event, values['_ER_'], values['_AF_'], values['_GR_']) 


