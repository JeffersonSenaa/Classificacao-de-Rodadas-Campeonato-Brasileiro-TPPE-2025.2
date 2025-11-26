from src.time.time import Time
from src.jogo.jogo import Jogo

def processa_rodada(partidas):
    """Processa uma lista de partidas e atualiza os pontos e estatísticas dos times."""
    for partida in partidas:
        Jogo.gerar_rodadas(partida)
