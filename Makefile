.PHONY: run init gui
.DEFAULT: run

init:
    sudo apt install python3-tk
    pip install PySimpleGUI

run:  init
    python3 main.py

gui: init
    python3 main_simpleui.py