COMPOSE=docker compose

.PHONY: up down restart ps logs logs-api logs-worker build test-job health minio reset

up:
	$(COMPOSE) up -d --build

down:
	$(COMPOSE) down

restart:
	$(COMPOSE) down
	$(COMPOSE) up -d --build

ps:
	$(COMPOSE) ps

logs:
	$(COMPOSE) logs -f

logs-api:
	$(COMPOSE) logs -f api

logs-worker:
	$(COMPOSE) logs -f worker

build:
	$(COMPOSE) build

health:
	curl -fsS http://localhost:$${API_PORT_PUBLIC:-8000}/health

minio:
	printf 'MinIO API: http://localhost:%s\nMinIO Console: http://localhost:%s\n' "$${MINIO_API_PORT:-9100}" "$${MINIO_CONSOLE_PORT:-9101}"

test-job:
	curl -sS -X POST http://localhost:$${API_PORT_PUBLIC:-8000}/jobs \
		-H 'Content-Type: application/json' \
		-d '{"url":"https://samplelib.com/lib/preview/mp4/sample-5s.mp4","language":"en","model":"tiny","backend":"faster-whisper","segment_minutes":1}'

reset:
	$(COMPOSE) down -v