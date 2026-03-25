# Epic: Analyze the Content

## Objective

Extract structured meaning from transcripts, including summaries, themes, entities, and analyzable segments.

## Current Status

- Status: `not started`

## Scope

- Segment transcript content by topic
- Generate summaries
- Extract entities, dates, and references
- Produce analysis artifacts using pluggable AI engines
- Preserve outputs for comparison across engines

## Milestones

- [ ] Analysis job contract defined
- [ ] Summary generation pipeline defined
- [ ] Topic segmentation designed
- [ ] Entity extraction designed
- [ ] AI engine abstraction defined

## Open Questions

- Which analysis outputs are required for the MVP?
- Do we support multiple engines from day one or after the first stable path?
- How much of the analysis pipeline should be deterministic versus model-driven?

## Decisions

- Analysis should be modeled as a separate stage from transcription.

## Next Actions

- Define analysis result schema
- Define engine adapter interface
- Decide first open source analysis stack
