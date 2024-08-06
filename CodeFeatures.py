from art import tprint
import os

def Func(func):
    def wrapper(*args, **kwargs):
        clearConsole()
        tprint("Progs.py")
        func()
    return wrapper

def clearConsole():
    os.system("cls")