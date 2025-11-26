
class Jogo:
    @staticmethod
    def gerar_rodadas(partida):
        """Processa o resultado de um jogo e atualiza os pontos, vitórias, empates e derrotas dos times."""
        mandante = partida['mandante']
        visitante = partida['visitante']
        gols_mandante = partida['gols_mandante']
        gols_visitante = partida['gols_visitante']

        # Atualiza gols marcados e sofridos
        mandante.gols_marcados += gols_mandante
        mandante.gols_sofridos += gols_visitante
        visitante.gols_marcados += gols_visitante
        visitante.gols_sofridos += gols_mandante
        
        # Atualiza saldo de gols
        mandante.saldo_gols = mandante.gols_marcados - mandante.gols_sofridos
        visitante.saldo_gols = visitante.gols_marcados - visitante.gols_sofridos

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