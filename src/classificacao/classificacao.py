from .time import Time

def processa_rodada(partidas):
    """Processa uma lista de partidas e atualiza os pontos e estatísticas dos times."""
    for partida in partidas:
        mandante = partida['mandante']
        visitante = partida['visitante']
        gols_mandante = partida['gols_mandante']
        gols_visitante = partida['gols_visitante']

        # Atualiza gols marcados e sofridos
        mandante.gols_marcados += gols_mandante
        mandante.gols_sofridos += gols_visitante
        visitante.gols_marcados += gols_visitante
        visitante.gols_sofridos += gols_mandante

        # Atualiza pontos, vitórias, empates e derrotas
        if gols_mandante > gols_visitante:
            mandante.pontos += 3
            mandante.vitorias += 1
            visitante.derrotas += 1
        elif gols_visitante > gols_mandante:
            visitante.pontos += 3
            visitante.vitorias += 1
            mandante.derrotas += 1
        else:
            mandante.pontos += 1
            visitante.pontos += 1
            mandante.empates += 1
            visitante.empates += 1

def gera_classificacao(times):
    """Ordena a lista de times com base nos critérios de classificação."""
    # Critérios: 
    # 1. Pontos
    # 2. Vitórias 
    times_ordenados = sorted(times, key=lambda time: (-time.pontos, -time.vitorias))
    return times_ordenados
