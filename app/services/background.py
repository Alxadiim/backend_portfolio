import asyncio
import logging

from app.services.stream_service import generate_transaction
from app.services.etl_service import process_transactions
from app.models.transaction import Transaction
from app.core.database import SessionLocal

logger = logging.getLogger(__name__)

async def stream_transactions():

    while True:

        db = None

        try:
            db = SessionLocal()

            batch = [generate_transaction() for _ in range(5)]

            cleaned = process_transactions(batch)

            for tx in cleaned:
                db.add(Transaction(**tx))

            db.commit()

            logger.info(f"{len(cleaned)} transactions inserted")

        except Exception as e:

            logger.error(f"STREAM ERROR: {e}")

            if db:
                db.rollback()

        finally:

            if db:
                db.close()

        await asyncio.sleep(10)
