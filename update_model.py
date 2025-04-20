import pandas as pd
from train_models import train_and_save_model

def update_model_from_csv(csv_path, model_name):
    try:
        df = pd.read_csv(csv_path)
        if 'value' not in df.columns:
            raise ValueError("CSV faylida 'value' ustuni yo‘q")
        data = df['value'].tolist()
        train_and_save_model(data, model_name)
        print(f"{model_name} modeli yangilandi.")
    except Exception as e:
        print(f"Xatolik: {e}")
