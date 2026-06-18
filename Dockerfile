FROM --platform=linux/amd64 python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8000 \
    YTENX_DB_PATH=/app/ytenx/ytenx.sqlite

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN python scripts/build_sqlite.py --target ytenx/ytenx.sqlite --reset \
    && python manage.py check

EXPOSE 8000
CMD ["sh", "-c", "gunicorn ytenx.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers ${WEB_CONCURRENCY:-2} --access-logfile - --error-logfile -"]
