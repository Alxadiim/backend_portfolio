
import asyncio
import logging
from app.services.stream_service import generate_transaction
from app.services.etl_service import process_transactions
from app.models.transaction import Transaction
from app.core.database import SessionLocal

async def stream_transactions():
    while True:
        db = SessionLocal()

        batch = [generate_transaction() for _ in range(5)]
        cleaned = process_transactions(batch)

        for tx in cleaned:
            db.add(Transaction(**tx))

        db.commit()
        db.close()

        await asyncio.sleep(3)
        