# src/insalubre_survivor/avl.py
from typing import Optional, List, Tuple

class NoAVL:
    def __init__(self, nome_jogador: str, pontuacao_recorde: int):
        self.nome_jogador = nome_jogador
        self.pontuacao_recorde = pontuacao_recorde
        self.altura = 1
        self.esquerda = None
        self.direita = None
        self.historico_avls = []
        self.contador_mortes = 0
        self.record_eventos = 0
        self.chefes_derrotados = 0
        self.total_avls = 0

def obter_altura(no: Optional[NoAVL]) -> int:
    return no.altura if no else 0

def atualizar_altura(no: NoAVL):
    no.altura = 1 + max(obter_altura(no.esquerda), obter_altura(no.direita))

def obter_balanceamento(no: Optional[NoAVL]) -> int:
    return obter_altura(no.esquerda) - obter_altura(no.direita) if no else 0

def rotacionar_direita(y: NoAVL) -> NoAVL:
    x = y.esquerda
    T2 = x.direita
    x.direita = y
    y.esquerda = T2
    atualizar_altura(y); atualizar_altura(x)
    return x

def rotacionar_esquerda(x: NoAVL) -> NoAVL:
    y = x.direita
    T2 = y.esquerda
    y.esquerda = x
    x.direita = T2
    atualizar_altura(x); atualizar_altura(y)
    return y

# ... suas funções de inserir, encontrar_jogador, obter_top_n_pontuacoes etc.
def encontrar_jogador(no: Optional[NoAVL], nome_jogador: str) -> Optional[NoAVL]:
    if not no or no.nome_jogador == nome_jogador:
        return no
    if nome_jogador < no.nome_jogador:
        return encontrar_jogador(no.esquerda, nome_jogador)
    return encontrar_jogador(no.direita, nome_jogador)

def obter_top_n_pontuacoes(no: Optional[NoAVL], n: int, resultados: List[Tuple[str,int,int,int,int]]):
    if no and len(resultados) < n:
        obter_top_n_pontuacoes(no.direita, n, resultados)
        if len(resultados) < n:
            resultados.append((no.nome_jogador, no.pontuacao_recorde, no.record_eventos, no.chefes_derrotados, no.total_avls))
            obter_top_n_pontuacoes(no.esquerda, n, resultados)
