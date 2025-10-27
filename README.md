# Classificacao-de-Rodadas-Campeonato-Brasileiro-TPPE-2025.2

## Requisitos

- Python 3.12
- Pytest

## Integrantes

- Felipe Aguiar Hansen - 222032810
- Gabriel Barbosa Alencar - 200049020
- Jefferson Sena Oliveira - 200020323
- Tiago Albuquerque de Lima - 202028973

## Estrutura do Projeto

Para garantir a organização, manutenibilidade e escalabilidade do código, o projeto seguirá a seguinte estrutura de diretórios e arquivos. Esta estrutura separa claramente as responsabilidades da aplicação (sorteio e classificação) e facilita os testes.

```
/
├── .gitignore               
├── README.md                
├── Roteiro.md               
├── requirements.txt         
│
├── src/                     
│   ├── __init__.py
│   │
│   ├── classificacao/       
│   │   ├── __init__.py
│   │   ├── time.py          
│   │   └── classificacao.py 
│   │
│   └── sorteio/             
│       ├── __init__.py
│       └── sorteio.py       
│
└── tests/                   
    ├── __init__.py
    │
    ├── classificacao/       
    │   ├── __init__.py
    │   └── test_classificacao.py
    │
    └── sorteio/             
        ├── __init__.py
        └── test_sorteio.py

```

## Como Executar os Testes

Siga os passos abaixo para configurar o ambiente e executar os testes automatizados do projeto.

2. **Crie e ative uma venv:**
   ```bash
   # Crie o ambiente virtual
   python3 -m venv .venv

   # Ative o ambiente virtual
   source .venv/bin/activate
   ```

3. **Instale as dependências:**
   Instale as dependências do `requirements.txt`.
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute os testes:**
   Execute o comando `pytest` na raiz do diretório.
   ```bash
   pytest
   ```

   Para executar os testes de um arquivo específico, passe o caminho do arquivo como argumento:
   ```bash
   pytest tests/sorteio/test_sorteio_rodadas.py
   ```
   ou
      ```bash
   pytest tests/classificacao/test_classificacao.py
   ```

   ## Testes Executados
   <img width="953" height="419" alt="image" src="https://github.com/user-attachments/assets/65510486-5a6c-4744-9308-0762d0ecae4e" />

