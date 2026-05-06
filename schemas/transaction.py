from pydantic import BaseModel
from datetime import datetime

class TransactionIn(BaseModel):
    transaction_id: str
    provider: str
    amount: int
    currency: str
    status: str
    timestamp: datetime