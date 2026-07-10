import joblib


# Load trained artifacts
model = joblib.load("nootbook+model/churn_model.pkl")
scaler = joblib.load("nootbook+model/scaler.pkl")
feature_names = joblib.load("nootbook+model/feature_names.pkl")