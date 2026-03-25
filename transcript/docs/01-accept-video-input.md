# Epic: Accept Video Input

## Objective

Support video intake from URLs and uploaded files, with enough normalization to identify repeat requests and route work into the processing pipeline.

## Current Status

- Status: `in progress`

## Scope

- Accept public video URLs
- Accept local or uploaded media files
- Normalize input URLs
- Extract canonical source identifiers when possible
- Validate supported formats
- Capture source metadata

## Milestones

- [x] CLI accepts a video URL
- [x] CLI accepts a local video file
- [ ] URL normalization is persisted
- [ ] Canonical source ID extraction is implemented
- [ ] Uploaded file workflow is defined

## Open Questions

- Which platforms are first-class targets beyond Facebook?
- Will uploaded files be handled by the same service as URLs?
- Should unsupported URLs be rejected immediately or queued for later validation?

## Decisions

- Initial support exists for URL-based download and local file input through the CLI.

## Next Actions

- Add canonical URL normalization rules
- Persist source metadata in the database design
- Define uploaded file intake flow for the future API
