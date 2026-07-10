from sqlalchemy.orm import Session

from database.models import CustomerPrediction
from database.schema import CustomerPredictionCreate


def create_prediction(
    db: Session,
    customer: CustomerPredictionCreate,
    churn_risk_score: float,
    will_churn: bool,
):
    db_customer = CustomerPrediction(
        customer_id=customer.customer_id,
        age=customer.age,
        gender=customer.gender,
        tenure=customer.tenure,
        usage_frequency=customer.usage_frequency,
        support_calls=customer.support_calls,
        payment_delay=customer.payment_delay,
        subscription_type=customer.subscription_type,
        contract_length=customer.contract_length,
        total_spend=customer.total_spend,
        last_interaction=customer.last_interaction,
        churn_risk_score=churn_risk_score,
        will_churn=will_churn,
    )

    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)

    return db_customer