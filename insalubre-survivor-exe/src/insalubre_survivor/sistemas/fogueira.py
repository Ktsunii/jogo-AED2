# src/insalubre_survivor/sistemas/fogueira.py
def lidar_com_fogueira(jogo) -> bool:
    jogo.melhorias_usadas_na_fogueira = False
    while True:
        print(f"\n🔥 FOGUEIRA - Almas: {jogo.jogador_atual.almas}")
        # ... (copie o corpo existente)
        # use jogo. em vez de self.
