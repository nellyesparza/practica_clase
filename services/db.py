services:
  db:
    image: postgres:16-alpine
    container_name: gastos-db
    environment:
      POSTGRES_USER: ${POSTGRES_USER:-gastos}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD:-gastos}
      POSTGRES_DB: ${POSTGRES_DB:-gastos}
    volumes:
      - gastos_db_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER:-gastos}"]
      interval: 5s
      timeout: 5s
      retries: 5
