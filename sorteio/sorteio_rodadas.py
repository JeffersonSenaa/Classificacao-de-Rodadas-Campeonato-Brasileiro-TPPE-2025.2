
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
        pass

