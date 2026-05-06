from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.transaction import TransactionIn
from services.etl_service import process_transactions
from app.core.database import SessionLocal
from models.transaction import Transaction

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/api/routes/transactions/ingest")
def ingest(data: list[TransactionIn], db: Session = Depends(get_db)):

    cleaned = process_transactions([d.model_dump() for d in data])

    inserted = 0

    for tx in cleaned:
        exists = db.query(Transaction)\
            .filter_by(transaction_id=tx["transaction_id"])\
            .first()

        if not exists:
            db.add(Transaction(**tx))
            inserted += 1

    try:
        db.commit()
    except:
        db.rollback()
        raise

    return {
        "received": len(data),
        "inserted": inserted,
        "cleaned": len(cleaned)
    }
    
@router.get("/api/routes/transactions/latest")
def latest(db: Session = Depends(get_db)):
    return db.query(Transaction)\
        .order_by(Transaction.timestamp.desc())\
        .limit(15)\
        .all()
    