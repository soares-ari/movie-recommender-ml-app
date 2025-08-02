from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import pickle

# Inicializar API
app = FastAPI(title="Movie Recommender API")

# Configurar CORS para permitir chamadas do React
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend local
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Carregar modelo SVD
with open("../../data/svd_model.pkl", "rb") as f:
    model = pickle.load(f)

# Carregar dados dos filmes
base_path = "../../data/movielens/ml-100k/"
movies = pd.read_csv(
    base_path + "u.item",
    sep="|",
    encoding="latin-1",
    header=None,
    usecols=[0, 1],
    names=["movie_id", "title"]
)

# Função de recomendação
def get_recommendations(user_id, top_n=5):
    movie_ids = movies["movie_id"].values
    preds = [(movie_id, model.predict(user_id, movie_id).est) for movie_id in movie_ids]
    preds_sorted = sorted(preds, key=lambda x: x[1], reverse=True)[:top_n]
    recommended = movies[movies["movie_id"].isin([m[0] for m in preds_sorted])]
    return recommended.to_dict(orient="records")

# Rota principal
@app.get("/recommendations/{user_id}")
def recommend_movies(user_id: int, n: int = 5):
    recs = get_recommendations(user_id, top_n=n)
    return {"user_id": user_id, "recommendations": recs}
