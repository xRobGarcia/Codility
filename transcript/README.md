# fbtranscribe

CLI para descargar un video (p.ej. Facebook), segmentar el audio en partes y transcribirlo aunque dure +2 horas.

## Estructura del proyecto

```text
.
├── deploy/                # Docker, Compose y bootstrap de infraestructura local
├── docs/                  # Seguimiento funcional por epic
├── src/fbtranscribe/      # Código de aplicación
├── data/                  # Runtime local para jobs y artefactos temporales
├── out/                   # Salidas manuales del CLI
├── pyproject.toml
└── README.md
```

Notas:

- `deploy/` concentra toda la infraestructura local.
- `src/fbtranscribe/` contiene CLI, API, worker y utilidades.
- `data/` y `out/` son runtime artifacts, no código fuente.

## Requisitos

- `ffmpeg` instalado (ya lo tienes si `ffmpeg -version` funciona)
- Python 3.10+

### Backend de transcripción (elige uno)

**Opción A (recomendada si puedes instalarlo):** `faster-whisper` (todo en Python).

**Opción B (si Python 3.13 te complica wheels):** `whisper.cpp` (binario externo). El proyecto soporta este backend también.

## Instalación

Desde esta carpeta:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e .
```

Para `faster-whisper`:

```bash
pip install -e ".[faster-whisper]"
```

## Uso

Transcribir el link (pipeline completo: descarga → chunks → transcripción):

```bash
fbtranscribe \
  --url "https://www.facebook.com/share/v/1KcdPhHagC/" \
  --out-dir out \
  --cookies /ruta/a/cookies.txt \
  --language es \
  --segment-minutes 30 \
  --backend faster-whisper \
  --model small
```

Si ya tienes el video descargado:

```bash
fbtranscribe --input-video /ruta/video.mp4 --out-dir out --language es
```

Salida:

- `out/transcript.txt`
- `out/transcript.srt` (si el backend entrega timestamps)
- `out/chunks/` (audio segmentado)
- `out/state/` (progreso para reanudar)

## Stack local con Docker Compose

Se agregó un stack local con Docker Compose para emular los servicios principales del proyecto:

- `postgres`: metadatos, jobs y artefactos indexados
- `minio`: storage S3-compatible local
- `redis`: reservado para cola y cache futura
- `api`: FastAPI para crear y consultar jobs
- `worker`: proceso que toma jobs pendientes y ejecuta el pipeline
- `ollama` (opcional con profile `ai`): motor local para análisis futuro

### Persistent volumes

All containers use persistent volumes in the Compose stack:

- `postgres_data`: PostgreSQL data files
- `minio_data`: object storage data
- `redis_data`: Redis data
- `jobs_data`: shared job outputs between API and worker
- `api_state`: API local state
- `worker_state`: worker local state
- `huggingface_cache`: downloaded model cache
- `faster_whisper_cache`: transcription model cache
- `ollama_data`: local Ollama models

### Arranque

```bash
cp .env.example .env
docker compose up --build
```

Archivos relevantes del stack:

- `docker-compose.yml`
- `deploy/docker/Dockerfile.app`
- `deploy/postgres/init/001_init.sql`

### Endpoints útiles

- API health: `http://localhost:8000/health`
- API docs: `http://localhost:8000/docs`
- MinIO console: `http://localhost:9001`

### Crear un job

```bash
curl -X POST http://localhost:8000/jobs \
  -H 'Content-Type: application/json' \
  -d '{
    "url": "https://www.facebook.com/share/v/1KcdPhHagC/",
    "language": "es",
    "model": "small",
    "backend": "faster-whisper",
    "segment_minutes": 30
  }'
```

### Consultar un job

```bash
curl http://localhost:8000/jobs/<job_id>
```

Los resultados de cada job quedan bajo `./data/jobs/<job_id>/`.

## Reanudar

Si el proceso se corta, vuelve a correr el mismo comando; el CLI salta chunks ya transcritos.

## whisper.cpp (backend alternativo)

1) Compilar y descargar un modelo (ejemplo):

```bash
git clone https://github.com/ggerganov/whisper.cpp
cd whisper.cpp
make -j
bash ./models/download-ggml-model.sh base
cd ..
```

2) Ejecutar con backend `whisper.cpp`:

```bash
fbtranscribe --url "..." --out-dir out --backend whisper.cpp \
  --whisper-cpp-bin ./whisper.cpp/main \
  --whisper-cpp-model ./whisper.cpp/models/ggml-base.bin \
  --language es
```

> Nota: los flags exactos del binario pueden variar según versión; si falla, corre `./whisper.cpp/main -h`.
