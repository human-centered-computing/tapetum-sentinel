# Training Pipeline

Training runs primarily in Google Colab while source code is loaded from GitHub.

## Modes

### New model

Creates the first checkpoint for a new task from an approved base model and curated dataset.

### Improve existing model

Loads the current task checkpoint and fine-tunes it with newly approved data.

## Required stages

1. Resolve immutable dataset version.
2. Validate labels and class map.
3. Split train, validation and test sets without leakage.
4. Train with versioned configuration.
5. Evaluate against the fixed test set.
6. Compare candidate against the active model.
7. Publish checkpoint, metrics and model card to Hugging Face.
8. Update the GitHub model registry through a pull request.

A candidate must not become active merely because training completed. Promotion requires measurable acceptance criteria.
