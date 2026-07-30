# ADR 0002: Store Model Artifacts on Hugging Face

## Status

Accepted

## Decision

GitHub stores source code and model registry metadata. Hugging Face stores checkpoints, model cards and optionally approved datasets.

## Rationale

Large binaries do not belong in the Git history. Hugging Face provides model-oriented versioning and distribution while GitHub remains the source-control and collaboration platform.
