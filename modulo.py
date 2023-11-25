"""Biblioteca pessoal"""

# Imports
from os import system
import keyboard
#from time import sleep

def tamanho(texto=""):
    iterador = iter(texto)
    n = 0
    while True:
        try:
            next(iterador)
            n += 1
        except StopIteration:
            break
    return n

def titulo(titulo="TEXTO"):
    return f"{"=" * 16} {titulo.upper()} {"=" * 16}"