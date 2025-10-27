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
    
    def test_gerar_38_rodadas(self, times_brasileirao):
        """Teste 2: Deve gerar exatamente 38 rodadas"""
        sorteio = SorteioRodadas(times_brasileirao)
        rodadas = sorteio.gerar_rodadas()
        assert len(rodadas) == 38

    def test_cada_rodada_tem_10_jogos(self, times_brasileirao):
        """Teste 3: Cada rodada deve ter 10 jogos (20 times / 2)"""
        sorteio = SorteioRodadas(times_brasileirao)
        rodadas = sorteio.gerar_rodadas()
        for rodada in rodadas:
            assert len(rodada) == 10

    def test_total_de_380_jogos(self, times_brasileirao):
        """Teste 4: Deve haver 380 jogos no total (38 rodadas × 10 jogos)"""
        sorteio = SorteioRodadas(times_brasileirao)
        rodadas = sorteio.gerar_rodadas()
        total_jogos = sum(len(rodada) for rodada in rodadas)
        assert total_jogos == 380

    def test_nao_existem_jogos_duplicados(self, times_brasileirao):
        """
        Teste 5: Não deve existir dois jogos iguais ao longo das rodadas.
        Um jogo é considerado igual quando tem o mesmo mandante e visitante.
        """
        sorteio = SorteioRodadas(times_brasileirao)
        rodadas = sorteio.gerar_rodadas()
        
        jogos_vistos = set()
        for rodada in rodadas:
            for jogo in rodada:
                # Identificador de jogo
                identificador = (jogo.mandante, jogo.visitante)
                assert identificador not in jogos_vistos, \
                    f"Jogo duplicado: {jogo.mandante} vs {jogo.visitante}"
                jogos_vistos.add(identificador)

    def test_cada_time_joga_duas_vezes_contra_cada_adversario(self, times_brasileirao):
        """
        Teste 6: Cada time deve jogar duas vezes contra cada adversário
        (uma como mandante e outra como visitante)
        """
        sorteio = SorteioRodadas(times_brasileirao)
        rodadas = sorteio.gerar_rodadas()
        
        # contar confrontos
        confrontos = {}
        
        for rodada in rodadas:
            for jogo in rodada:
                times_confronto = tuple(sorted([jogo.mandante, jogo.visitante]))
                
                if times_confronto not in confrontos:
                    confrontos[times_confronto] = 0
                confrontos[times_confronto] += 1
        
        # Limitador - Cada par de times deve se enfrentar exatamente 2 vezes
        for times_confronto, quantidade in confrontos.items():
            assert quantidade == 2, \
                f"Times {times_confronto[0]} e {times_confronto[1]} se enfrentaram {quantidade} vezes"

class TestJogo:
    """Testes para a classe Jogo"""
    
    def test_criar_jogo(self):
        """Teste 11: Deve criar um jogo com mandante e visitante"""
        jogo = Jogo("Flamengo", "Palmeiras")
        assert jogo.mandante == "Flamengo"
        assert jogo.visitante == "Palmeiras"
    
    def test_representacao_jogo(self):
        """Teste 12: Deve ter uma representação string legível"""
        jogo = Jogo("Flamengo", "Palmeiras")
        assert str(jogo) == "Flamengo vs Palmeiras"