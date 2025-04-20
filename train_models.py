import numpy as np
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

def create_dataset(data, step=10):
    X, y = [], []
    for i in range(len(data) - step):
        X.append(data[i:i+step])
        y.append(data[i+step])
    return np.array(X), np.array(y)

def train_and_save_model(data, name):
    X, y = create_dataset(data)
    model = RandomForestRegressor()
    model.fit(X, y)
    os.makedirs("ai_models", exist_ok=True)
    joblib.dump(model, f"ai_models/{name}.pkl")
    print(f"{name}.pkl modeli saqlandi.")
