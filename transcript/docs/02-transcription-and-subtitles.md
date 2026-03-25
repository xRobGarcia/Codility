# Epic: Turn It Into Transcripts and Subtitles

## Objective

Convert video or audio inputs into reusable transcripts and subtitle outputs across multiple languages and formats.

## Current Status

- Status: `in progress`

## Scope

- Extract audio from video
- Chunk long media files
- Transcribe using pluggable backends
- Generate subtitle outputs such as SRT
- Preserve raw and derived outputs separately
- Support resumable processing for long jobs

## Milestones

- [x] Audio chunking implemented
- [x] `faster-whisper` backend integrated
- [x] `whisper.cpp` backend path documented
- [x] Transcript TXT generation implemented
- [x] Transcript SRT generation implemented
- [x] Resume-by-chunk behavior implemented
- [ ] Additional subtitle formats such as VTT added
- [ ] Automatic language detection added

## Open Questions

- Which transcription backend should be the default in production?
- Do we need diarization in the first release?
- Should translation be a separate pipeline stage?

## Decisions

- Separate cleaned transcript files are generated without overwriting original outputs.

## Next Actions

- Add WebVTT generation
- Add metadata about detected language and model version
- Define backend abstraction for future remote ASR engines
