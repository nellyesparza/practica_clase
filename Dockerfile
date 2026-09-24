FROM python:3.12-slim

# Copiar el ejecutable de uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# Copiar archivos de dependencias
COPY pyproject.toml uv.lock ./


COPY app/ ./app/
COPY alembic.ini ./
COPY alembic/ ./alembic/


RUN useradd --create-home appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 8000

# Instalar dependencias en la imagen
RUN uv sync --frozen --no-dev --no-install-project
CMD ["uv", "run", "--no-sync", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]