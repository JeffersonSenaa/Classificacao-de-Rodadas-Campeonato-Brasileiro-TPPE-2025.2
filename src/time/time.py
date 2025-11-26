class Time:
    def __init__(self, nome):
        """Inicializa um time com suas estatísticas zeradas."""
        self.nome = nome
        self.pontos = 0
        self.vitorias = 0
        self.empates = 0
        self.derrotas = 0
        self.gols_marcados = 0
        self.gols_sofridos = 0
        self.saldo_gols = 0
    
    @staticmethod
    def gera_classificacao(times):
        """Ordena a lista de times com base nos critérios de classificação."""
        # Critérios: 
        # 1. Pontos
        # 2. Vitórias
        # 3. Saldo de Gols
        # 4. Gols Marcados
        times_ordenados = sorted(times, key=lambda time: (-time.pontos, -time.vitorias, -time.saldo_gols, -time.gols_marcados))
        return times_ordenados
