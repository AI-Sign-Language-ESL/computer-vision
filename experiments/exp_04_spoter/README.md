# Exp-04 — SPOTER

| Field | Value |
|-------|-------|
| **Model** | SPOTER |
| **Input** | Landmark sequences |
| **Top-1** | 24.55% |
| **Top-5** | 44.11% |
| **Status** | **Baseline** |

## Overview

SPOTER (Sign POse-based TransformER) — a landmark-native transformer with learned queries, purpose-built for sign-language recognition.

## Key findings

Best Top-1 among landmark models and far cheaper than VideoMAE. Strong landmark baseline; retained for comparison.

## Folder layout

```
exp_04_spoter/
├── README.md          # this file
├── train.py           # training entry point
├── evaluate.py        # Top-1 / Top-5 evaluation on the test split
├── inference.py       # single-sample inference
├── requirements.txt   # experiment-specific deps (+ root requirements)
├── configs/
│   └── default.yaml   # default hyper-parameters
└── models/
    └── model.py       # model definition
```

## Usage

All commands are run from the repository root so that the `shared`, `evaluation`
and `preprocessing` packages resolve on `PYTHONPATH`.

```bash
# Train
python -m experiments.exp_04_spoter.train --config experiments/exp_04_spoter/configs/default.yaml

# Evaluate
python -m experiments.exp_04_spoter.evaluate --checkpoint outputs/exp_04_spoter.pt

# Inference on a single sample
python -m experiments.exp_04_spoter.inference --input path/to/sample --top-k 5
```

> **Note:** `train.py`, `evaluate.py`, `inference.py` and `models/model.py` are
> runnable skeletons containing `TODO(manual-review)` markers. Drop the original
> SPOTER implementation into these files to make the experiment fully
> functional. See [`docs/migration_report.md`](../../docs/migration_report.md).
