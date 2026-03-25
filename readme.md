#  Análise de Músicas do Spotify

Script em Python que busca músicas de um artista na API do Spotify e gera gráficos de análise.

## O que ele faz

- Busca as músicas de qualquer artista pelo nome
- Gera gráfico de barras com a duração de cada música
- Gera gráfico de pizza com proporção de músicas explícitas vs não explícitas
- Exibe uma tabela com nome, duração, álbum e classificação de cada música

## Como usar

1. Clone o repositório
2. Instale as dependências
3. Configure as credenciais
4. Execute o script

### Instalando dependências
```bash
pip install spotipy pandas matplotlib python-dotenv
```

### Configurando credenciais

Crie um arquivo `.env` na raiz do projeto:
```
SPOTIFY_CLIENT_ID=seu_client_id
SPOTIFY_CLIENT_SECRET=seu_client_secret
```

Para obter as credenciais, crie um app em [developer.spotify.com](https://developer.spotify.com).

### Executando
```bash
python src/analise.py
```

## Tecnologias

- Python 3.8+
- [spotipy](https://spotipy.readthedocs.io/) — acesso à API do Spotify
- [pandas](https://pandas.pydata.org/) — manipulação de dados
- [matplotlib](https://matplotlib.org/) — geração de gráficos
- [python-dotenv](https://pypi.org/project/python-dotenv/) — gerenciamento de credenciais