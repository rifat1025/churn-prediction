from pydantic import BaseModel
from datetime import  datetime

class CustomerPredictionCreate(BaseModel):
    customer_id: str
    age: int
    gender: str
    tenure: int
    usage_frequency: int
    support_calls: int
    payment_delay: int
    subscription_type: str
    contract_length: str
    total_spend: float
    last_interaction: int
    
    

class CustomerPredictionResponse(BaseModel):
    id: int
    customer_id: str
    age: int
    gender: str
    tenure: int
    usage_frequency: int
    support_calls: int
    payment_delay: int
    subscription_type: str
    contract_length: str
    total_spend: float
    last_interaction: int
    # predictin
    churn_risk_score: float
    will_churn: bool
    created_at: datetime

    class Config:
        from_attributes = True
    