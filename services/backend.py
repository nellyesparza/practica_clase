backend:
    build: .
    container_name: gastos-backend
    depends_on:
      migrate:
        condition: service_completed_successfully
    ports:
      - "8000:8000"
    env_file:
      - .env
    environment:
      DATABASE_URL: postgresql+psycopg2://${POSTGRES_USER:-gastos}:${POSTGRES_PASSWORD:-gastos}@db:5432/${POSTGRES_DB:-gastos}
    restart: unless-stopped

volumes:
  gastos_db_data:
