.PHONY run lint init
.DEFAULT: run

lint:
    find . -name '*.pyc' -exec rm --force {} +
    find . -name '*.pyo' -exec rm --force {} +
    name '*~' -exec rm --force  {} 

init:
    pip install PySimpleGUI

run:  init
    python main.py
