# src/insalubre_survivor/eventos.py
import random
from typing import Optional
from .enums import TipoEvento, Raridade, Condicao
from .modelos import Inimigo, Item

class EventoJogo:
    def __init__(self, tipo_evento: TipoEvento, descricao: str, raridade: Raridade,
                 inimigo: Optional[Inimigo] = None, recompensa_almas: int = 0,
                 efeito_sanidade: int = 0, item: Optional[Item] = None,
                 eh_armadilha: bool = False, eh_escolha_chefe: bool = False,
                 eh_evento_especial: bool = False):
        self.tipo_evento = tipo_evento
        self.descricao = descricao
        self.raridade = raridade
        self.inimigo = inimigo
        self.recompensa_almas = recompensa_almas
        self.efeito_sanidade = efeito_sanidade
        self.item = item
        self.eh_armadilha = eh_armadilha
        self.eh_escolha_chefe = eh_escolha_chefe
        self.eh_evento_especial = eh_evento_especial

# Funções de criação/roleta que você já tem podem vir para cá,
# ex.: rolar_tipo_evento(), criar_evento_especifico(), lidar_com_escolha_chefe() etc.
