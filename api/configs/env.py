import os

# DATABASE

DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_PORT = os.environ.get("DB_PORT", 1433)
DB_USER = os.environ.get("DB_USER", "sa")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "Admin!123")
DB_NAME = os.environ.get("DB_NAME", "teste_incrustacao_db")
