from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://neondb_owner:npg_mpxVE9Nq7hPK@ep-small-wave-aqg6w2qr-pooler.c-8.us-east-1.aws.neon.tech/portfolio?sslmode=require&channel_binding=require"

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=300,
    pool_size=5,
    max_overflow=10
)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
