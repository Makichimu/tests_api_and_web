# Используем официальный образ Python 3.9 как базовый
FROM python:3.9-slim-buster

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файлы проекта в рабочую директорию
COPY . /app

# Устанавливаем зависимости проекта
RUN pip install --no-cache-dir -r requirements.txt

# Запускаем тесты и сохраняем результаты в файл test_results.xml
CMD pytest --junitxml=test_results.xml
