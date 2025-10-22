
class Jogo:
    def __init__(self, mandante, visitante):
        self.mandante = mandante
        self.visitante = visitante
    
    def __str__(self):
        return f"{self.mandante} vs {self.visitante}"
    
    def __repr__(self):
        return f"Jogo({self.mandante}, {self.visitante})"


class SorteioRodadas:
    
    def __init__(self, times):
        if len(times) % 2 != 0:
            raise ValueError("O número de times deve ser par")
        
        self.times = times.copy()

    def gerar_rodadas(self):
        """
        Gera todas as rodadas do campeonato usando o algoritmo Round-Robin:
        - fixa um time na primeira posição
        - rotaciona os demais times em sentido horário
        - a cada rodada, emparelha os times em posições opostas
        - alterna mandante e visitante para variar os jogos
        - depois do turno, inverte mandante e visitante para o returno
        """
        num_times = len(self.times)
        num_rodadas_turno = num_times - 1
        
        times_rotacao = self.times.copy()
        
        turno = []
        for rodada_num in range(num_rodadas_turno):
            rodada = []
            
            turno.append(rodada)
            
            # Rotacionar times 
            times_rotacao = [times_rotacao[0]] + [times_rotacao[-1]] + times_rotacao[1:-1]

