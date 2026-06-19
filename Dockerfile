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
    && python manage.py check \
    && gunicorn --version \
    && chmod +x scripts/container_start.sh

EXPOSE 8000
CMD ["scripts/container_start.sh"]
