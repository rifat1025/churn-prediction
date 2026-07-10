from fastapi import FastAPI,Depends
from database.config import Base,SessionLocal,engine
from database.schema import CustomerPredictionCreate
from database.config import get_db
from core.core import create_prediction
from sqlalchemy.orm import Session
from core.model_loader import model,scaler,feature_names
import pandas as pd

Base.metadata.create_all(bind=engine)

app =FastAPI(
     title="Customer Churn Prediction API"
)


# Default page url
@app.get("/")

def home():
    return {"message": "Customer Churn Prediction API is Running"}


# Prediction Route
@app.post("/predict")
def predict(
    customer: CustomerPredictionCreate,
    db: Session = Depends(get_db)
):
    # Dummy Prediction (Model পরে যোগ করব)
    churn_risk_score = 0.85
    will_churn = True

    result = create_prediction(
        db=db,
        customer=customer,
        churn_risk_score=churn_risk_score,
        will_churn=will_churn
    )

    return {
        "message": "Prediction saved successfully",
        "customer_id": result.customer_id,
        "churn_risk_score": result.churn_risk_score,
        "will_churn": result.will_churn
    }
    
@app.get('/model-info')
def model_info():
    return {
        "message": "Model loaded successfully",
        "total_features": len(feature_names)
    }

@app.post("/churn_predict")
def prediction_churn(customer_data: CustomerPredictionCreate):
    df = pd.DataFrame([customer_data])
    
    
    # এখানে Feature Engineering যোগ করব
    
    # Feature Order
    df = df[feature_names]

    # Scaling
    X = scaler.transform(df)

    # Prediction
    prediction = model.predict(X)[0]

    # Probability
    probability = model.predict_proba(X)[0][1]

    return prediction, probability
    