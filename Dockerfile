FROM python:3.10-slim as base

ENV PYTHONUNBUFFERED=1
ENV POSTGRES_USER=restartcrm
ENV POSTGRES_PASSWORD=changeme
ENV POSTGRES_DB=restartcrm
ENV POSTGRES_HOST=postgres
ENV POSTGRES_PORT=5432
ENV SECRET_KEY=changeme
ENV ALGORITHM=HS256

COPY docker-entrypoint.sh alembic.ini requirements.txt ./
COPY app ./app

RUN pip install -r requirements.txt
RUN chmod +x docker-entrypoint.sh

EXPOSE 5000

HEALTHCHECK CMD curl --fail http://localhost:5000 || exit 1

CMD ["./docker-entrypoint.sh"]