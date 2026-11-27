# Tapetum Sentinel

> Übersetzungsstatus: KI-unterstützter Entwurf, menschliche Sprachprüfung ausstehend.

[English](README.md) · [Türkçe](README.tr.md) · [Deutsch](README.de.md) · [العربية](README.ar.md)

Tapetum Sentinel ist eine menschenzentrierte Open-Source-Plattform zur Videoanalyse für Drohnen- und Feldaufnahmen. Sie verbessert visuelle Eingaben, erkennt aufgabenspezifische Objekte, speichert nachweisreiche Metadaten und ermöglicht lokale Offline-Fragebeantwortung über analysierte Videos.

## Grundprinzipien

- Menschenzentrierte Transformation
- Standardmäßig Open Source
- Lokal zuerst und offline-fähig
- Modellunabhängige Architektur
- Evidenzbasierte Antworten
- Kontinuierliche Verbesserung durch validiertes Feedback

## Pipeline

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

## Repository-Struktur

- `apps/`: Desktop- und API-Anwendungen
- `services/`: Verbesserung, Erkennung, Tracking, Wissen und lokale LLM-Dienste
- `training/`: Colab-Trainings- und Evaluationsabläufe
- `feedback/`: Annotation, Validierung und Datensatzexport
- `model-registry/`: Zuordnung von Nutzeraufgaben zu Modellen
- `database/`: Schemata und Migrationen
- `docker/`: Docker-Ressourcen
- `docs/`: Architektur- und Entscheidungsdokumentation

## Modellverteilung

Quellcode auf GitHub; trainierte Checkpoints und Modellkarten sollen auf Hugging Face erscheinen. Die Registry ordnet Aufgaben wie Katastrophen- oder Landwirtschaftsanalyse versionierten Modellen zu.

## Status

Erstes Architekturgrundgerüst. Komponenten werden schrittweise hinter stabilen Dienstverträgen implementiert.

## Lizenz

GNU Affero General Public License v3.0 (AGPL-3.0). Siehe [LICENSE](LICENSE). Bei über ein Netzwerk angebotenen modifizierten AGPL-Versionen gelten die Anforderungen zur Quellcodeverfügbarkeit.
