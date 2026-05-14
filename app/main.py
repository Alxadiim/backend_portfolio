from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import transactions, analytics, profile
from fastapi.staticfiles import StaticFiles
import asyncio
import logging
from app.services.background import stream_transactions

logging.basicConfig(level=logging.INFO)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://portfolio-cheikhouna.netlify.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API
app.include_router(transactions.router, prefix="/api")
app.include_router(analytics.router, prefix="/api")
app.include_router(profile.router, prefix="/api")
@app.get("/")
def root():
    return {"status": "ok"}


# Background stream sécurisé
@app.on_event("startup")
async def start_stream():
    from app.core.database import engine
    from app.models.transaction import Base
    Base.metadata.create_all(bind=engine)
    
    async def safe_stream():
        try:
            await stream_transactions()
        except Exception as e:
            logging.error(f"Stream crashed: {e}")

    asyncio.create_task(safe_stream())

@app.get("/health")
def health():
    return {"status": "ok"}
