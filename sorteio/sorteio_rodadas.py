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

            for i in range(num_times // 2):
                time_a = times_rotacao[i]
                time_b = times_rotacao[num_times - 1 - i]

                if (rodada_num + i) % 2 == 0:
                    jogo = Jogo(time_a, time_b)
                else:
                    jogo = Jogo(time_b, time_a)
                
                rodada.append(jogo)
            
            turno.append(rodada)
            
            # Rotacionar times 
            times_rotacao = [times_rotacao[0]] + [times_rotacao[-1]] + times_rotacao[1:-1]

        # Criar o returno invertendo mandante e visitante
        returno = []
        for rodada in turno:
            rodada_returno = []
            for jogo in rodada:
                # Inverte mandante e visitante
                jogo_returno = Jogo(jogo.visitante, jogo.mandante)
                rodada_returno.append(jogo_returno)
            returno.append(rodada_returno)
        
        # Retornar turno + returno (38 rodadas)
        return turno + returno
    
    def exibir_rodadas(self, rodadas):
        for i, rodada in enumerate(rodadas, 1):
            print(f"\n{'='*50}")
            print(f"RODADA {i}")
            print(f"{'='*50}")
            for jogo in rodada:
                print(f"  {jogo}")