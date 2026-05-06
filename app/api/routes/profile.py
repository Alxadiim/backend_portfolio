from fastapi import APIRouter

router = APIRouter()

@router.get("/api/routes/profile")
def profile():
    return {
        "name": "Cheikhouna Ahmadoul Khadim Lo",
        "role": "Data Engineer",
        "summary": "Data Engineer avec une forte base en développement logiciel, spécialisé dans la conception de pipelines de données, la modélisation de bases et l’exploitation analytique pour des cas concrets de digitalisation.",
        
        "data_skills": {
            "data_processing": ["Pandas", "NumPy"],
            "data_analysis": ["Exploratory Data Analysis", "Data Cleaning", "Feature Engineering"],
            "machine_learning": ["Scikit-learn (bases)"],
            "databases": ["PostgreSQL", "MySQL", "SQL Server", "MongoDB"],
            "data_modeling": ["Schema design", "Normalization", "Relational modeling"],
            "data_engineering": ["ETL pipelines", "API data ingestion (FastAPI)", "Data workflows"]
        },
        
        "engineering_stack": ["Python", "FastAPI", "Docker", "Git"],
        
        "experience": [
            "Conception et implémentation de bases de données pour systèmes ERP/CRM",
            "Développement de pipelines de traitement de données pour applications métier",
            "Digitalisation de commerces avec exploitation des données (stocks, ventes, reporting)",
            "Gestion autonome de projets data en freelance"
        ],
        
        "education": [
            "Licence en Science des Données et Génie Logiciel",
            "BTS en Administration de Bases de Données"
        ],
        
        "location": "Dakar, Senegal"
    }