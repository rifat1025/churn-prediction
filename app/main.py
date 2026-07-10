from fastapi import FastAPI
from database.config import Base,SessionLocal,engine



Base.metadata.create_all(bind=engine)

app =FastAPI(
     title="Customer Churn Prediction API"
)


# Default page url
@app.get("/")

def home():
    return {"message": "Customer Churn Prediction API is Running"}
    