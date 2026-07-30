# Contributing

Thank you for contributing to Tapetum Sentinel.

## Contribution flow

1. Create an issue describing the change.
2. Fork the repository or create a feature branch.
3. Add tests and documentation with the implementation.
4. Open a pull request using the provided template.
5. Address review feedback before merge.

## Model contributions

A model contribution must include:

- Intended task and supported classes
- Dataset provenance and license
- Training configuration
- Evaluation metrics
- Known limitations and failure cases
- Hugging Face model identifier and immutable revision

Do not commit large model files directly to GitHub.

## Dataset and feedback quality

User feedback is treated as untrusted until validation. New annotations must pass review before entering any training dataset. Training, validation and test sets must remain separated.

## Development principles

- Preserve offline operation after initial model download.
- Keep service interfaces model-independent.
- Avoid hard-coding checkpoint names in the user interface.
- Every answer generated from analyzed video must link to evidence such as frame, timestamp and metadata.
