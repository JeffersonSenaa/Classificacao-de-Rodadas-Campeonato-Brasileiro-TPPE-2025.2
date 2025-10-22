# Classificacao-de-Rodadas-Campeonato-Brasileiro-TPPE-2025.2
Classificação de Rodadas do Campeonato Brasileiro - Trabalho Prático TPPE - 2025.2

## Estrutura do Projeto

Para garantir a organização, manutenibilidade e escalabilidade do código, o projeto seguirá a seguinte estrutura de diretórios e arquivos. Esta estrutura separa claramente as responsabilidades da aplicação (sorteio e classificação) e facilita os testes.

```
/
├── .gitignore               # Arquivo para ignorar arquivos e diretórios do Git
├── README.md                # Documentação do projeto
├── Roteiro.md               # Enunciado e requisitos do trabalho
├── requirements.txt         # Dependências do projeto Python
│
├── src/                     # Diretório principal do código-fonte
│   ├── __init__.py
│   │
│   ├── classificacao/       # Módulo para lógica de classificação e pontuação
│   │   ├── __init__.py
│   │   ├── time.py          # Classe que representa um time e suas estatísticas
│   │   └── classificacao.py # Funções para processar rodadas e gerar a tabela
│   │
│   └── sorteio/             # Módulo para lógica de sorteio das rodadas
│       ├── __init__.py
│       └── sorteio.py       # Funções para gerar as rodadas do campeonato
│
└── tests/                   # Diretório para os casos de teste (estrutura espelhada)
    ├── __init__.py
    │
    ├── classificacao/       # Testes para o módulo de classificação
    │   ├── __init__.py
    │   └── test_classificacao.py
    │
    └── sorteio/             # Testes para o módulo de sorteio
        ├── __init__.py
        └── test_sorteio.py

```
