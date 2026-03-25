# Epic: Run and Operate the Platform Reliably

## Objective

Provide the infrastructure, local developer workflow, deployment model, and observability needed to operate the platform reliably at low cost.

## Current Status

- Status: `in progress`

## Scope

- Local Docker-based environment
- Configuration management
- Storage and database provisioning
- Logging and metrics
- Deployment profiles for local versus real instances
- Operational scripts and recovery paths

## Milestones

- [x] Docker Compose baseline created
- [x] Environment configuration strategy documented
- [x] PostgreSQL service added
- [x] Object storage service added or deferred explicitly
- [x] Basic local developer commands added
- [x] Core local stack validated end to end
- [ ] Observability baseline defined
- [ ] Deployment target strategy documented

## Open Questions

- When do we introduce Redis?
- Is MinIO required in the first milestone or can filesystem storage hold?
- Which logs and metrics are mandatory before exposing a public API?

## Decisions

- The project should prefer open source, low-cost components and emulate external platforms locally with Docker before pointing to real services.
- Deployment assets are grouped under `deploy/` to separate infrastructure from application code.
- All Docker services should use persistent volumes, including shared job storage and model caches.

## Next Actions

- Add logs and metrics baseline
- Add deployment profiles for local versus real services
- Define service adapter boundaries for database, storage, queue, and AI engines
