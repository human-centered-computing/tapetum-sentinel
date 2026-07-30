# Architecture Overview

Tapetum Sentinel is organized as independently deployable services with stable contracts.

## Components

1. **Enhancement service**: improves low-light or degraded frames using Retinex Tapetum.
2. **Detection service**: loads a task-specific YOLO checkpoint selected through the model registry.
3. **Tracking service**: assigns persistent identities across frames.
4. **Metadata service**: merges timestamps, GPS, altitude, camera and mission metadata.
5. **Knowledge service**: stores detections and evidence references in a queryable structure.
6. **Local LLM adapter**: translates natural-language questions into retrieval and tool calls.
7. **Desktop application**: manages analysis, model selection, feedback and evidence display.

## Deployment principle

The same containerized services should run on a workstation, edge server or central server. After images and models are downloaded, core analysis must remain offline-capable.
