# src/insalubre_survivor/enums.py
from enum import Enum

class Raridade(Enum):
    COMUM = 1
    INCOMUM = 2
    RARO = 3
    CHEFE = 4

class Condicao(Enum):
    NENHUMA = 0
    VENENO = 1
    FRENESI = 2
    QUEIMADURA = 3
    MEDO = 4
    FOGO = 5
    ELETRICO = 6
    ATORDOADO = 7

class TipoEvento(Enum):
    INIMIGO_COMUM = 1
    EVENTO_COMUM = 2
    MINI_CHEFE = 3
    FOGUEIRA = 4
    EVENTO_RARO = 5
    CHEFE = 6
