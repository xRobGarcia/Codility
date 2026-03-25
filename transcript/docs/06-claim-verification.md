# Epic: Verify Factual Claims

## Objective

Extract factual claims from transcript content, gather evidence, and classify claims with transparent and auditable reasoning.

## Current Status

- Status: `not started`

## Scope

- Extract claims from transcript segments
- Separate factual statements from opinions
- Gather candidate evidence sources
- Assign verdicts with confidence levels
- Support multiple verification engines
- Preserve traceability from claim to evidence

## Milestones

- [ ] Claim schema defined
- [ ] Evidence schema defined
- [ ] Claim extraction stage defined
- [ ] Verification verdict model defined
- [ ] Aggregate scoring model defined

## Open Questions

- What minimum evidence quality is acceptable?
- Should source ranking be deterministic, model-driven, or hybrid?
- How will conflicting evidence be represented?

## Decisions

- Truth evaluation should be claim-based, not a single opaque video score.

## Next Actions

- Draft claim and evidence data model
- Define verification taxonomy
- Define first-pass evidence retrieval strategy
