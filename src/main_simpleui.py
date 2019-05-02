#!/usr/bin/env python

import sys
import PySimpleGUI as sg  

sg.ChangeLookAndFeel('BlueMono')

tab1_layout =  [[sg.T('This is inside tab 1')]]        
tab2_layout =  [[sg.T('AF')], [sg.T('ER')], [sg.T('GR')],   
               [sg.In(key='in')]]    



# Column layout
col = [[sg.Text('Entrada', text_color='white', background_color='blue')],
        [sg.Text('ER', text_color='white', background_color='blue'), sg.Input('col input 1')],
        [sg.Text('ER', text_color='white', background_color='blue'), sg.Input('col input 2')],
        [sg.Text('GR', text_color='white', background_color='blue'), sg.Input('col input 3')]]
# Window layout
layout = [[sg.Listbox(values=('Listbox Item 1', 'Listbox Item 2', 'Listbox Item 3'),
                      select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE, size=(20, 3)),
           sg.Column(col, background_color='blue')],
          [sg.Input('Last input')],
          [sg.OK()]]

# Display the window and get values
event, values = sg.Window(' Trabalho Formais by Bruno e Vinicius - 2019.1 ').Layout(layout).Read()

sg.Popup(event, values, line_width=200)
