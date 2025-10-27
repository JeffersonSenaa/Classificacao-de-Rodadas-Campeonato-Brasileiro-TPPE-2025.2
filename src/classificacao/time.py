class Time:
    def __init__(self, nome):
        self.nome = nome
        self.pontos = 0
        self.vitorias = 0
        self.empates = 0
        self.derrotas = 0
        self.gols_marcados = 0
        self.gols_sofridos = 0

    @property
    def saldo_gols(self):
        return self.gols_marcados - self.gols_sofridos
