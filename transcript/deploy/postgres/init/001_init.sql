create extension if not exists pgcrypto;

create table if not exists video_source (
    id uuid primary key default gen_random_uuid(),
    platform text not null,
    original_url text,
    normalized_url text not null,
    source_video_id text,
    metadata_json jsonb not null default '{}'::jsonb,
    created_at timestamptz not null default now()
);

create unique index if not exists uq_video_source_normalized_url
    on video_source (normalized_url);

create table if not exists transcription_job (
    id uuid primary key,
    video_source_id uuid not null references video_source(id) on delete cascade,
    source_url text,
    input_video_path text,
    cookies_path text,
    language text not null,
    model text not null,
    backend text not null,
    segment_minutes integer not null default 30,
    device text not null default 'cpu',
    compute_type text not null default 'int8',
    dedupe_key text not null,
    status text not null check (status in ('pending', 'processing', 'completed', 'failed')),
    progress numeric(5,2) not null default 0,
    requested_count integer not null default 1,
    out_dir text,
    error_message text,
    requested_at timestamptz not null default now(),
    started_at timestamptz,
    finished_at timestamptz
);

create unique index if not exists uq_transcription_job_dedupe_key
    on transcription_job (dedupe_key);

create index if not exists ix_transcription_job_status
    on transcription_job (status);

create table if not exists transcript_asset (
    id uuid primary key default gen_random_uuid(),
    job_id uuid not null references transcription_job(id) on delete cascade,
    video_source_id uuid not null references video_source(id) on delete cascade,
    language text not null,
    model text not null,
    backend text not null,
    transcript_text text,
    transcript_clean_text text,
    txt_path text,
    srt_path text,
    summary_json jsonb not null default '{}'::jsonb,
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now()
);

create unique index if not exists uq_transcript_asset_job_id
    on transcript_asset (job_id);

create table if not exists request_log (
    id uuid primary key default gen_random_uuid(),
    job_id uuid not null references transcription_job(id) on delete cascade,
    requested_by_user_id text,
    requested_by_ip inet,
    user_agent text,
    created_at timestamptz not null default now()
);
