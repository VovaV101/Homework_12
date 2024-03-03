# Використовуємо офіційний образ Python версії 3.10
FROM python:3.10

# Встановлюємо змінну середовища для додатку
ENV APP_HOME /app 

# Встановлюємо робочу директорію всередині контейнера
WORKDIR $APP_HOME

# Копіюємо файли додатку та requirements.txt в робочу директорію контейнера
COPY .. .

# Встановлюємо залежності Python, вказані у файлі requirements.txt
RUN pip install -r requirements.txt

# Команда для запуску додатку
CMD ["python", "main.py"]
