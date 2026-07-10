from fastapi import FastAPI,Depends
from database.config import Base,SessionLocal,engine
from database.models import CustomerPredictionCreate
from database.config import get_db
from core.core import create_prediction
from sqlalchemy.orm import Session


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
    