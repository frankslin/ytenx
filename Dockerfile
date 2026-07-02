FROM --platform=linux/amd64 python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8000 \
    YTENX_DB_PATH=/app/ytenx/ytenx.sqlite \
    YTENX_ENV=production

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN test -s ytenx/ytenx.sqlite \
    && python manage.py check \
    && gunicorn --version \
    && chmod +x scripts/container_start.sh

EXPOSE 8000
CMD ["scripts/container_start.sh"]
