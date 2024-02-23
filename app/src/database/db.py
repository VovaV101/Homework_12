from os import environ
from pathlib import Path

from dotenv import load_dotenv
from fastapi import HTTPException, status
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

# Завантажуємо змінні середовища з файлу .env
ENV_FILE = Path(__file__).resolve().parent.parent.parent.joinpath(".env")

load_dotenv(ENV_FILE)

# Отримуємо значення змінних середовища
postgres_username = environ.get("POSTGRES_USERNAME")
postgres_password = environ.get("POSTGRES_PASSWORD")
postgres_host = environ.get("POSTGRES_HOST")
postgres_port = environ.get("POSTGRES_PORT")
postgres_database = environ.get("POSTGRES_DATABASE")

# Перевіряємо, чи всі необхідні змінні були визначені
assert all([postgres_username, postgres_password, postgres_host, postgres_port, postgres_database]), "Some PostgreSQL environment variables are missing"

# Формуємо URL для підключення до бази даних
SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{postgres_username}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_database}"
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# Створюємо об'єкт сесії бази даних
DBSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Функція залежності для отримання сесії бази даних
def get_db():
    db = DBSession()
    try:
        yield db
    except SQLAlchemyError as err:
        print(err)
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))
    finally:
        db.close()


if __name__ == "__main__":
    print(engine)
