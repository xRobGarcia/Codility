# Deployment Assets

This directory contains local infrastructure and deployment-related files.

## Layout

- `docker/`: application container build files
- `postgres/init/`: database bootstrap SQL for local environments

## Local Usage

From the repository root:

```bash
cp .env.example .env
docker compose up --build
```

The root `docker-compose.yml` references the files in this directory.
