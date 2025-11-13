# src/insalubre_survivor/main.py
import sys
from .runner import executar_executavel
from jogo import iniciar_jogo_cli

def main():
    # Caso você ainda queira manter a opção de abrir o .exe externo:
    if len(sys.argv) > 1 and sys.argv[1] == "--exe":
        # passe o caminho real via argumento 2 se quiser
        caminho = sys.argv[2] if len(sys.argv) > 2 else "caminho/para/o/jogo.exe"
        executar_executavel(caminho)
        return

    # Caso contrário, inicia o jogo em Python (CLI atual)
    iniciar_jogo_cli()

if __name__ == "__main__":
    main()
