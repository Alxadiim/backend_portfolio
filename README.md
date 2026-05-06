# Backend Portfolio API

A FastAPI-based backend for managing portfolio data with transaction ingestion and analytics.

## Project Structure

```
backend_portfolio/
├── app/                      # Main application package
│   ├── __init__.py
│   ├── main.py              # FastAPI application instance
│   ├── api/                 # API routes
│   │   ├── routes/
│   │   │   ├── transactions.py
│   │   │   ├── analytics.py
│   │   │   └── profile.py
│   ├── models/              # SQLAlchemy models
│   │   └── transaction.py
│   ├── schemas/             # Pydantic schemas
│   │   └── transaction.py
│   ├── services/            # Business logic
│   │   ├── etl_service.py
│   │   ├── stream_service.py
│   │   └── background.py
│   ├── core/                # Core configuration
│   │   ├── config.py
│   │   └── database.py
│   ├── utils/               # Utility functions
│   │   └── metrics.py
│   └── requirement.txt      # Python dependencies
├── main.py                  # Entrypoint wrapper
├── .gitignore
└── README.md
```

## Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Alxadiim/backend_portfolio.git
   cd backend_portfolio
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r app/requirement.txt
   ```

4. **Configure environment variables:**
   - Update database connection details in `app/core/database.py`
   - Configure settings in `app/core/config.py`

## Running the Application

**Option 1: Using the wrapper script (from project root):**
```bash
python main.py
```

**Option 2: Using uvicorn directly:**
```bash
uvicorn main:app --reload
```

**Option 3: Using Python module syntax:**
```bash
python -m uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

- **POST /api/routes/transactions/ingest** - Ingest transaction data
- **GET /api/routes/analytics** - Get analytics data
- **GET /api/routes/profile** - Get profile information

## Environment Variables

Make sure to set these before running:
- `DATABASE_URL` - PostgreSQL connection string
- `CORS_ORIGINS` - Allowed CORS origins (configured for portfolio-cheikhouna.netlify.app by default)

## Import Structure

All imports use the `app` prefix:
```python
from app.core.database import SessionLocal
from app.models.transaction import Transaction
from app.services.etl_service import process_transactions
```

This ensures imports work correctly regardless of how the application is launched.
