# Model Registry

The model registry decouples user-facing tasks from technical checkpoint names.

The UI displays a task name such as "Disaster Analysis". The registry resolves that task to a versioned model repository, revision and artifact.

## Update policy

The default update policy is manual approval. The application may check for a newer signed registry version, present release notes and download the selected model. The previous model remains available for rollback.
