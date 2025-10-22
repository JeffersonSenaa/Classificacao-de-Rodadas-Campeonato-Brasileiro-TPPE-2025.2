import pytest
from sorteio_rodadas import SorteioRodadas, Jogo

class TestSorteioRodadas:
    """Testes para a classe SorteioRodadas"""
    
    @pytest.fixture
    def times_brasileirao(self):
        """Fixture com os 20 times do Brasileirão"""
        return [
            "Flamengo", "Palmeiras", "São Paulo", "Corinthians",
            "Internacional", "Grêmio", "Atlético-MG", "Cruzeiro",
            "Fluminense", "Botafogo", "Vasco", "Athletico-PR",
            "Santos", "Bahia", "Fortaleza", "Ceará",
            "Goiás", "Coritiba", "Cuiabá", "Red Bull Bragantino"
        ]
    
    def test_criar_sorteio_com_20_times(self, times_brasileirao):
        """Teste 1: Deve criar um sorteio com 20 times"""
        sorteio = SorteioRodadas(times_brasileirao)
        assert len(sorteio.times) == 20