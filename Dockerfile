FROM python:3.10-slim as base

ENV PYTHONUNBUFFERED=1

COPY docker-entrypoint.sh alembic.ini requirements.txt ./
COPY app ./app

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*
RUN pip install -r requirements.txt
RUN chmod +x docker-entrypoint.sh

HEALTHCHECK CMD curl --fail http://localhost:80 || exit 1

CMD ["./docker-entrypoint.sh"]