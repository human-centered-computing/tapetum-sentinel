# Validated Feedback Loop

Operational feedback is the bridge between inference and future training.

## Feedback types

- Missed detection: an object exists but the model did not detect it.
- False positive: the model detected an object that is not present.
- Wrong class: the object exists but has the wrong label.
- Poor bounding box: the object is detected but localization is inaccurate.

## Workflow

```text
Inference
  -> User correction
  -> Automated validation
  -> Human review
  -> Approved annotation pool
  -> Dataset version
  -> Fine-tuning
  -> Candidate checkpoint
  -> Regression evaluation
  -> Controlled promotion
```

Raw feedback never enters training directly. Approved examples are deduplicated, reviewed for privacy and licensing, and assigned to data splits under a leakage-prevention policy.
