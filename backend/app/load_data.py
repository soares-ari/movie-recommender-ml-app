import os
import pandas as pd

# Caminho base
base_path = "../../data/movielens/ml-100k/"

print("📂 Verificando caminho:", os.path.abspath(base_path))
print("📄 Arquivos na pasta:", os.listdir(base_path))

# Leitura dos ratings
ratings_path = os.path.join(base_path, "u.data")
movies_path = os.path.join(base_path, "u.item")

print("✅ Lendo:", ratings_path)
ratings = pd.read_csv(ratings_path, sep="\t", names=["user_id", "movie_id", "rating", "timestamp"])

print("✅ Lendo:", movies_path)
movies = pd.read_csv(movies_path, sep="|", encoding="latin-1", header=None, usecols=[0, 1], names=["movie_id", "title"])

print("🔗 Fazendo merge...")
df = pd.merge(ratings, movies, on="movie_id")

print("🎬 Primeiras linhas:")
print(df.head())
