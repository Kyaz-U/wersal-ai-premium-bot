import joblib
import numpy as np

def predict_next_value(model_name, data, step=10):
    model_path = f"ai_models/{model_name}.pkl"
    try:
        model = joblib.load(model_path)
        X = np.array(data[-step:]).reshape(1, -1)
        prediction = model.predict(X)[0]
        return round(float(prediction), 2)
    except Exception as e:
        return f"Xatolik yuz berdi: {e}"
