#!/bin/sh

alembic revision --autogenerate
alembic upgrade head
uvicorn app.main:app