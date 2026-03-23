import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os
import pandas as pd
import matplotlib.pyplot as plt

load_dotenv()

client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id = client_id,
    client_secret=client_secret
))

def buscar_musicas_artista(nome_artista):
    resultado = sp.search(q=nome_artista, type="track", limit=10)

    musicas=[]
    for track in resultado["tracks"]["items"]:
        musicas.append({
            "nome": track.get("name", "Desconhecido"),
            "duracao_seg": round(track.get("duration_ms", 0) / 1000),
            "explicito": "Sim" if track.get("explicit") else "Não",
            "album": track.get("album", {}).get("name", "Desconhecido"),
        })

    return pd.DataFrame(musicas)

def gerar_graficos(df, nome_artista):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle(f"Análise das top músicas - {nome_artista}", fontsize=14)

    ax1.barh(df["nome"], df["duracao_seg"], color="blue")
    ax1.set_title("Duração das músicas")
    ax1.set_xlabel("Duração (segundos)")

    explicito_count = df["explicito"].value_counts()
    ax2.pie(explicito_count, labels=explicito_count.index, autopct="%1.1f%%", colors=["red", "green"])
    ax2.set_title("Músicas explícitas vs não explícitas")

    plt.tight_layout()
    plt.savefig(f"{nome_artista}_analise.png")
    plt.show()

if __name__ == "__main__":
    nome = input("Digite o nome do artista: ")
    df = buscar_musicas_artista(nome)
    print(df)
    gerar_graficos(df, nome)