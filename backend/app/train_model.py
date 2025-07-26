import pandas as pd
from surprise import SVD, Dataset, Reader
import pickle

# Caminho dos dados
base_path = "../../data/movielens/ml-100k/"

# Carregar ratings
ratings = pd.read_csv(base_path + "u.data", sep="\t", names=["user_id", "movie_id", "rating", "timestamp"])

# Preparar para Surprise
reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(ratings[['user_id', 'movie_id', 'rating']], reader)

# Treinar modelo SVD
trainset = data.build_full_trainset()
model = SVD()
model.fit(trainset)

# Salvar modelo treinado
with open("../../data/svd_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Modelo SVD treinado e salvo com sucesso!")