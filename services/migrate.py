  # Servicio de un solo uso: aplica las migraciones y termina (exit 0).
  # "backend" espera a que ESTE servicio termine con éxito antes de arrancar.
  migrate:
    build: .
    container_name: gastos-migrate
    depends_on:
      db:
        condition: service_healthy
    env_file:
      - .env
    environment:
      DATABASE_URL: postgresql+psycopg2://${POSTGRES_USER:-gastos}:${POSTGRES_PASSWORD:-gastos}@db:5432/${POSTGRES_DB:-gastos}
    command: ["uv", "run", "--no-sync", "alembic", "upgrade", "head"]
    restart: "no"
