# Tapetum Sentinel

Tapetum Sentinel is an open-source, human-centered video intelligence platform designed for drone and field imagery. It enhances visual input, performs task-specific object detection, stores evidence-rich metadata, and enables local, offline question answering over analyzed video.

## Core principles

- Human-centered transformation
- Open-source by default
- Local-first and offline-capable
- Model-independent architecture
- Evidence-backed answers
- Continuous improvement through validated feedback

## High-level pipeline

```text
Video / Drone Feed
        |
        v
Retinex Tapetum Enhancement
        |
        v
Task-Specific YOLO Detection
        |
        v
Tracking + Metadata Fusion
        |
        v
Local Database + Evidence Index
        |
        v
Local LLM / RAG Question Answering
```

## Repository structure

- `apps/`: desktop and API applications
- `services/`: enhancement, detection, tracking, knowledge and local LLM services
- `training/`: Colab-oriented training and evaluation workflows
- `feedback/`: annotation, validation and dataset export workflow
- `model-registry/`: user-facing task to model mapping
- `database/`: schemas and migrations
- `docker/`: Docker-related assets
- `docs/`: architecture and decision records

## Model distribution

Source code is maintained on GitHub. Trained checkpoints and model cards are intended to be published on Hugging Face. The application resolves task names such as "Disaster Analysis" or "Agriculture Analysis" to versioned models through the model registry.

## Current status

This repository is an initial architecture scaffold. Components will be implemented incrementally behind stable service contracts.

## License

GNU Affero General Public License v3.0 (AGPL-3.0). See `LICENSE`.

If you modify this AGPL-covered software and make the modified version available to users over a network, the AGPL source-availability requirements apply.
