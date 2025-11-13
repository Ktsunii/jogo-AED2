# src/insalubre_survivor/jogo.py
import random
from typing import Optional
from enums import Raridade, Condicao, TipoEvento
from modelos import Item, Arma, Inimigo
from avl import NoAVL, encontrar_jogador, obter_top_n_pontuacoes
from eventos import EventoJogo
from sistemas import fogueira as sys_fogueira
from sistemas import sanidade as sys_sanidade
from sistemas import inventario as sys_inv
# from .sistemas import combate as sys_combate

class SobreviventeInsalubre:
    def __init__(self):
        self.ranking: Optional[NoAVL] = None
        self.total_mortes = 0
        self.historico_jogadores = {}

        # ===== armas e itens (igual você já tem) =====
        self.armas = {
            "Bastão Enferrujado": Arma("Bastão Enferrujado", 5, 10),
            "Cutelo Serrato": Arma("Cutelo Serrato", 10, 15),
            "Machado Radioativo": Arma("Machado Radioativo", 15, 20),
            "Greatsword": Arma("Greatsword", 25, 30),
            "Metralhadora": Arma("Metralhadora", 30, 40, "distancia", 0.30, 50, 50),
            "Claymore": Arma("Claymore", 27, 28),
            "UltraGreatsword": Arma("UltraGreatsword", 40, 32),
            "Uchigatana": Arma("Uchigatana", 13, 15),
            "Pistola": Arma("Pistola", 2, 1, "distancia", 0.30, 20, 20),
            "Bacamarte": Arma("Bacamarte", 5, 1, "distancia", 0.30, 15, 20),
        }
        self.itens = self.inicializar_itens()

        self.jogador_atual = None
        self.recarga_fogueira = 0
        self.turno_atual = 0

        self.inicializar_inimigos()
        self.inicializar_eventos()
        self.melhorias_usadas_na_fogueira = False
        self.escala_dificuldade = 1.0
        self.contador_buff_inimigos = 0

    # ===== copie aqui os métodos “simples” de setup =====
    def inicializar_itens(self):
        itens = {
            "Fragmento de Ferro": Item("Fragmento de Ferro", "melhoria", "dano", 5),
            # ... (copie o restante sem alterar)
        }
        return itens

    def inicializar_inimigos(self):
        # ... (sem alterar)
        pass

    def inicializar_eventos(self):
        # ... (sem alterar)
        pass

    # Exemplo de delegação para sistemas:
    def abrir_fogueira(self):
        return sys_fogueira.lidar_com_fogueira(self)

    def efeitos_sanidade(self):
        return sys_sanidade.obter_efeitos_sanidade(self.jogador_atual)

    def menu_armas(self):
        return sys_inv.menu_armas(self)

    # seu loop/fluxo principal chama os módulos
    def loop_principal(self):
        # Exemplo ilustrativo
        while True:
            evento = self.gerar_evento()  # se estiver em eventos.py, apenas chame aqui
            # ...
            if evento.tipo_evento == TipoEvento.FOGUEIRA:
                self.abrir_fogueira()
            # elif combate:
            #     sys_combate.realizar_combate(self, evento.inimigo)
            # ...

# Função de alto nível chamada pela main.py
def iniciar_jogo_cli():
    jogo = SobreviventeInsalubre()
    jogo.loop_principal()
