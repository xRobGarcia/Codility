# Epic: Store and Reuse Results

## Objective

Persist source metadata, processing outputs, and reuse signals so repeated requests can return results quickly without redundant work.

## Current Status

- Status: `in progress`

## Scope

- Persist canonical video records
- Store transcript variants and metadata
- Track deduplication keys
- Reuse existing results for repeated requests
- Track access patterns for future optimization

## Milestones

- [x] PostgreSQL schema defined
- [ ] Deduplication key strategy implemented
- [x] Transcript asset records persisted
- [ ] Repeat-request cache path implemented
- [x] Object storage strategy finalized
- [x] MinIO artifact upload integrated

## Open Questions

- What should be the canonical dedupe key for each platform?
- Which artifacts stay in PostgreSQL versus object storage?
- Should transcript reuse depend on model and language only, or also on cleanup version?

## Decisions

- The design direction is PostgreSQL for metadata and object storage or filesystem for large artifacts.
- The local stack now uses PostgreSQL for metadata and MinIO plus shared filesystem volumes for artifacts.
- Primary job artifacts are uploaded to MinIO and exposed as object URIs through the API.

## Next Actions

- Create the first relational schema draft
- Define Bronze, Silver, and Gold persistence boundaries
- Add request logging model for repeat demand
