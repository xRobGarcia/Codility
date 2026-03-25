# Epic: Expose the Workflow Through Services and Job Handling

## Objective

Expose the processing pipeline through stable services, asynchronous jobs, and clear operational state transitions.

## Current Status

- Status: `in progress`

## Scope

- Accept requests through an API
- Create and manage jobs
- Track job state and progress
- Prevent duplicate work when the same video is requested repeatedly
- Support local emulation through Dockerized services

## Milestones

- [x] FastAPI service scaffold created
- [x] Job submission endpoint defined
- [x] Job status endpoint defined
- [x] Job artifacts endpoint defined
- [x] Worker process separated from API
- [ ] Queue strategy selected
- [x] Docker Compose orchestration created

## Open Questions

- Should the first queue be PostgreSQL-backed or Redis-backed?
- Will the first API include user identity or stay anonymous?
- Which service owns transcript cleanup and later analysis stages?

## Decisions

- Local platform emulation through separate Docker services is the preferred path.

## Next Actions

- Define API contracts
- Define job lifecycle states
- Decide when to move from database polling to a dedicated queue
