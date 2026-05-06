import random
import uuid
from datetime import datetime

providers = ["Wave", "Orange Money"]

def generate_transaction():
    return {
        "transaction_id": str(uuid.uuid4()),
        "provider": random.choice(providers),
        "amount": random.randint(500, 50000),
        "currency": "FCFA",
        "status": "success" if random.random() > 0.1 else "failed",
        "timestamp": datetime.utcnow().isoformat()
    }