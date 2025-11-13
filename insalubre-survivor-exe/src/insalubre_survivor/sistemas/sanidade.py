# src/insalubre_survivor/sistemas/sanidade.py
def obter_efeitos_sanidade(jogador):
    sanidade = jogador.sanidade
    efeitos = []
    if sanidade > 80:
        efeitos += ["👁️  Criaturas bizarras aparecem frequentemente", "💀 Chance de inimigos 1-hit kill", "⚡ Penalidades de defesa e esquiva"]
    elif sanidade > 60:
        efeitos += ["👻 Mini-chefes em áreas comuns", "🎯 Ataques críticos inimigos aumentados", "🌌 Eventos sobrenaturais intensos"]
    elif sanidade > 40:
        efeitos += ["😰 Inimigos mais agressivos", "💎 Eventos raros mais frequentes"]
    return efeitos
