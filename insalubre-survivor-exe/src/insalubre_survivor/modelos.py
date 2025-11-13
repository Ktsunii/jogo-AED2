# src/insalubre_survivor/modelos.py
from typing import Dict, Optional, List
from .enums import Condicao, Raridade

class Item:
    def __init__(self, nome: str, categoria: str, efeito: str, valor: int):
        self.nome = nome
        self.categoria = categoria
        self.efeito = efeito
        self.valor = valor

class Arma:
    def __init__(self, nome: str, dano: int, custo_stamina: int,
                 tipo: str = "corpo_a_corpo", chance_crit: float = 0.0,
                 balas: int = 0, balas_maximas: int = 0):
        self.nome = nome
        self.dano = dano
        self.custo_stamina = custo_stamina
        self.tipo = tipo
        self.chance_crit = chance_crit
        self.balas = balas
        self.balas_maximas = balas_maximas
        # se você já tinha dicionários/limites:
        self.melhorias_aplicadas = {"Fragmento de Ferro": 0, "Pedaco de Ferro": 0, "Lajota de Ferro": 0}
        self.limites_melhorias = {"Fragmento de Ferro": 5, "Pedaco de Ferro": 3, "Lajota de Ferro": 1}

class Inimigo:
    def __init__(self, nome: str, vida: int, recompensa_almas: int,
                 raridade: Raridade, condicoes: Optional[List[Condicao]] = None):
        self.nome = nome
        self.vida = vida
        self.vida_maxima = vida
        self.recompensa_almas = recompensa_almas
        self.raridade = raridade
        self.condicoes = condicoes or []
