from app.api.routes.transactions import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from app.core.database import SessionLocal
from app.models.transaction import Transaction
from sqlalchemy import func
from datetime import datetime, timedelta

router = APIRouter()

@router.get("/api/routes/analytics/summary")
def summary(db: Session = Depends(get_db)):

    last_24h = datetime.utcnow() - timedelta(hours=24)

    total = db.query(func.count(Transaction.id)).scalar()

    success = db.query(func.count(Transaction.id))\
        .filter(Transaction.status == "success")\
        .scalar()

    volume = db.query(func.sum(Transaction.amount)).scalar() or 0

    recent = db.query(func.count(Transaction.id))\
        .filter(Transaction.timestamp >= last_24h)\
        .scalar()

    return {
        "total_transactions": total,
        "success_rate_percentage": round((success/total)*100,2) if total else 0,
        "processed_volume_fcfa": volume,
        "transactions_last_24h": recent,
        "pipelines": ["Wave","Orange Money"]
    }
