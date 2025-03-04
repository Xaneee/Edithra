import stripe
import os
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from Edithra.database.db_seetup import SessionLocal
from Edithra.config import STRIPE_API_KEY

router = APIRouter(prefix="/payments", tags=["payments"])

stripe.api_key = STRIPE_API_KEY

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/one-time")
def create_one_time_purchase(amount: int, currency: str = "usd"):
    try:
        payment_intent = stripe.PaymentIntent.create(
            amount=amount * 100,
            currency=currency,
            payment_method_types=["card"]
        )
        return {"client_secret": payment_intent.client_secret}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/subscription")
def create_subscription(customer_email: str, price_id: str):
    try:
        customer = stripe.Customer.create(email=customer_email)
        subscription = stripe.Subscription.create(
            customer=customer.id,
            items=[{"price": price_id}],
        )
        return {"subscription_id": subscription.id, "status": subscription.status}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/status/{payment_id}")
def check_payment_status(payment_id: str):
    try:
        payment_intent = stripe.PaymentIntent.retrieve(payment_id)
        return {"payment_status": payment_intent.status}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


