from .time import Time

def processa_rodada(partidas):
    """Processa uma lista de partidas e atualiza os pontos dos times."""
    for partida in partidas:
        mandante = partida['mandante']
        visitante = partida['visitante']
        gols_mandante = partida['gols_mandante']
        gols_visitante = partida['gols_visitante']

        if gols_mandante > gols_visitante:
            mandante.pontos += 3
        elif gols_visitante > gols_mandante:
            visitante.pontos += 3
        else:
            mandante.pontos += 1
            visitante.pontos += 1
