from sqlalchemy import Column, Integer, String, DateTime
from app.core.database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    transaction_id = Column(String, unique=True, index=True)
    provider = Column(String)
    operation = Column(String)
    amount = Column(Integer)
    currency = Column(String)
    status = Column(String)
    timestamp = Column(DateTime)