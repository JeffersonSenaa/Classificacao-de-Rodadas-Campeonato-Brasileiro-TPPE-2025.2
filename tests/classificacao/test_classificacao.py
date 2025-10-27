import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.classificacao.time import Time
from src.classificacao.classificacao import processa_rodada, gera_classificacao

class TestCalculoPontuacao(unittest.TestCase):

    def test_vitoria_mandante_atribui_3_pontos(self):
        """Teste para verificar a atribuição de 3 pontos para vitória."""
        time_a = Time("Time A")
        time_b = Time("Time B")
        partida = {"mandante": time_a, "visitante": time_b, "gols_mandante": 2, "gols_visitante": 0}
        
        processa_rodada([partida])
        
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
        time_a = Time("Time A")
        time_a.pontos = 3
        time_a.vitorias = 1
        
        time_b = Time("Time B")
        time_b.pontos = 3
        time_b.vitorias = 0
        
        times = [time_b, time_a]  # Desordenado
        
        classificacao = gera_classificacao(times)
        
        self.assertEqual(classificacao[0].nome, "Time A")
        self.assertEqual(classificacao[1].nome, "Time B")

    def test_desempate_por_saldo_de_gols(self):
        """Teste para verificar o critério de desempate por saldo de gols."""
        time_a = Time("Time A")
        time_a.pontos = 3
        time_a.vitorias = 1
        time_a.gols_marcados = 5
        time_a.gols_sofridos = 2  # Saldo: +3

        time_b = Time("Time B")
        time_b.pontos = 3
        time_b.vitorias = 1
        time_b.gols_marcados = 4
        time_b.gols_sofridos = 2  # Saldo: +2

        times = [time_b, time_a] # Desordenado

        classificacao = gera_classificacao(times)

        self.assertEqual(classificacao[0].nome, "Time A")
        self.assertEqual(classificacao[1].nome, "Time B")

    def test_desempate_por_gols_marcados(self):
        """Teste para o critério de desempate por gols marcados."""
        time_a = Time("Time A")
        time_a.pontos = 3
        time_a.vitorias = 1
        time_a.gols_marcados = 5
        time_a.gols_sofridos = 2  # Saldo: +3

        time_b = Time("Time B")
        time_b.pontos = 3
        time_b.vitorias = 1
        time_b.gols_marcados = 4
        time_b.gols_sofridos = 1  # Saldo: +3

        times = [time_b, time_a] # Desordenado

        classificacao = gera_classificacao(times)
        self.assertEqual(classificacao[0].nome, "Time A")
        self.assertEqual(classificacao[1].nome, "Time B")

if __name__ == '__main__':
    unittest.main()
