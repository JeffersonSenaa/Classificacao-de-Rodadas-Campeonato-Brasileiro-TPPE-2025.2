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
            
    def test_cada_time_joga_uma_vez_por_rodada(self, times_brasileirao):
        """Teste 7: Cada time deve jogar exatamente uma vez por rodada"""
        sorteio = SorteioRodadas(times_brasileirao)
        rodadas = sorteio.gerar_rodadas()
        
        for i, rodada in enumerate(rodadas):
            times_na_rodada = []
            for jogo in rodada:
                times_na_rodada.append(jogo.mandante)
                times_na_rodada.append(jogo.visitante)
            
            # Verificar se há 20 times e se não há duplicatas
            assert len(times_na_rodada) == 20, \
                f"Rodada {i+1} não tem 20 times"
            assert len(set(times_na_rodada)) == 20, \
                f"Rodada {i+1} tem times repetidos"
    
    def test_cada_time_tem_19_jogos_como_mandante(self, times_brasileirao):
        """Teste 8: Cada time deve ter exatamente 19 jogos como mandante"""
        sorteio = SorteioRodadas(times_brasileirao)
        rodadas = sorteio.gerar_rodadas()
        
        jogos_mandante = {time: 0 for time in times_brasileirao}
        
        for rodada in rodadas:
            for jogo in rodada:
                jogos_mandante[jogo.mandante] += 1
        
        for time, quantidade in jogos_mandante.items():
            assert quantidade == 19, \
                f"Time {time} tem {quantidade} jogos como mandante, esperado 19"
    
    def test_cada_time_tem_19_jogos_como_visitante(self, times_brasileirao):
        """Teste 9: Cada time deve ter exatamente 19 jogos como visitante"""
        sorteio = SorteioRodadas(times_brasileirao)
        rodadas = sorteio.gerar_rodadas()
        
        jogos_visitante = {time: 0 for time in times_brasileirao}
        
        for rodada in rodadas:
            for jogo in rodada:
                jogos_visitante[jogo.visitante] += 1
        
        for time, quantidade in jogos_visitante.items():
            assert quantidade == 19, \
                f"Time {time} tem {quantidade} jogos como visitante, esperado 19"
    
    def test_turno_e_returno_sao_espelhados(self, times_brasileirao):
        """
        Teste 10: O returno (rodadas 20-38) deve ser o espelho do turno (rodadas 1-19)
        Ou seja, se A jogou em casa contra B na rodada X do turno,
        B deve jogar em casa contra A na rodada X do returno
        """
        sorteio = SorteioRodadas(times_brasileirao)
        rodadas = sorteio.gerar_rodadas()
        
        turno = rodadas[:19]  # Rodadas 1 a 19
        returno = rodadas[19:]  # Rodadas 20 a 38
        
        for i in range(19):
            jogos_turno = set((jogo.mandante, jogo.visitante) for jogo in turno[i])
            jogos_returno = set((jogo.visitante, jogo.mandante) for jogo in returno[i])
            
            assert jogos_turno == jogos_returno, \
                f"Rodada {i+1} do turno não é espelhada na rodada {i+20} do returno"

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