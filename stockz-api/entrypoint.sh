#!/bin/sh

python -m alembic revision --autogenerate -m "new migration"

python -m alembic upgrade head

python index.py
