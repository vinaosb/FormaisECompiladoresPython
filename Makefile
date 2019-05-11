.PHONY: run init gui
.DEFAULT: run

init:
    pip install PySimpleGUI

run:  init
    python3 main.py

gui: init
    python3 main_simpleui.py