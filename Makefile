.PHONY: run init
.DEFAULT: run

init:
    pip install PySimpleGUI

run:  init
    python3 main.py
