import unittest

class Time:
    def __init__(self, nome, pontos=0, vitorias=0, gols_marcados=0, gols_sofridos=0):
        self.nome = nome
        self.pontos = pontos
        self.vitorias = vitorias
        self.gols_marcados = gols_marcados
        self.gols_sofridos = gols_sofridos
        self.saldo_gols = gols_marcados - gols_sofridos

def processa_rodada(partidas):
    # Função será implementada
    pass

def gera_classificacao(times):
    # Função será implementada
    return times

class TestCalculoPontuacao(unittest.TestCase):

    def test_vitoria_mandante_atribui_3_pontos(self):
        """Teste para verificar a atribuição de 3 pontos para vitória."""
        time_a = Time("Time A")
        time_b = Time("Time B")
        partida = {"mandante": time_a, "visitante": time_b, "gols_mandante": 2, "gols_visitante": 0}
        
        processa_rodada([partida])
        
        # Define os pontos inivialemnte como 0
        time_a.pontos = 0 # Forçando a falha, esperando 3
        time_b.pontos = 0
        
        self.assertEqual(time_a.pontos, 3)
        self.assertEqual(time_b.pontos, 0)

class TestCalculoEstatisticas(unittest.TestCase):

    def test_calcula_estatisticas_uma_partida(self):
        """Teste para verificar o cálculo de vitórias, gols e saldo."""
        time_a = Time("Time A")
        time_b = Time("Time B")
        partida = {"mandante": time_a, "visitante": time_b, "gols_mandante": 3, "gols_visitante": 1}
        
        processa_rodada([partida])

        self.assertEqual(time_a.vitorias, 1)
        self.assertEqual(time_a.gols_marcados, 3)
        self.assertEqual(time_a.gols_sofridos, 1)
        self.assertEqual(time_a.saldo_gols, 2)
        self.assertEqual(time_b.vitorias, 0)
        self.assertEqual(time_b.gols_marcados, 1)
        self.assertEqual(time_b.gols_sofridos, 3)
        self.assertEqual(time_b.saldo_gols, -2)

class TestCriteriosDesempate(unittest.TestCase):

    def test_desempate_por_vitorias(self):
        """Teste para verificar o critério de desempate por número de vitórias."""
        time_a = Time("Time A", pontos=3, vitorias=1)
        time_b = Time("Time B", pontos=3, vitorias=0)
        
        times = [time_b, time_a]  # Desordenado propositalmente
        
        classificacao = gera_classificacao(times)
        
        self.assertEqual(classificacao[0].nome, "Time A")
        self.assertEqual(classificacao[1].nome, "Time B")

if __name__ == '__main__':
    unittest.main()
