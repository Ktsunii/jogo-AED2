# src/insalubre_survivor/runner.py
import subprocess
import sys

def executar_executavel(jogo_executavel: str):
    if sys.platform == "win32":
        subprocess.Popen(['start', 'cmd', '/k', jogo_executavel], shell=True)
    else:
        print("Este script só é compatível com Windows.")
