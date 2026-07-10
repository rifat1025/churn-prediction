from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from datetime import datetime
from app.database.config import Base

class CustomerPrediction(Base):
    __tablename__ = "customer_prediction"

    id = Column(Integer, primary_key=True, index=True)

    # Customer Information
    customer_id = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String(20), nullable=False)
    tenure = Column(Integer, nullable=False)
    usage_frequency = Column(Integer, nullable=False)
    support_calls = Column(Integer, nullable=False)
    payment_delay = Column(Integer, nullable=False)
    subscription_type = Column(String(50), nullable=False)
    contract_length = Column(String(50), nullable=False)
    total_spend = Column(Float, nullable=False)
    last_interaction = Column(Integer, nullable=False)

    # Prediction Result
    churn_risk_score = Column(Float, nullable=False)
    will_churn = Column(Boolean, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)