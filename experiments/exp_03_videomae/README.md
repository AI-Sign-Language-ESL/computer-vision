# Exp-03 — VideoMAE

| Field | Value |
|-------|-------|
| **Model** | VideoMAE |
| **Input** | RGB videos |
| **Top-1** | 22.40% |
| **Top-5** | 55.00% |
| **Status** | **Baseline** |

## Overview

Fine-tuning a pretrained VideoMAE backbone directly on RGB clips, bypassing landmark extraction entirely.

## Key findings

Large jump in Top-1 accuracy by using pretrained spatiotemporal features. Established a strong RGB baseline but is compute-heavy and slow at inference. Kept as a baseline.

## Folder layout

```
exp_03_videomae/
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
python -m experiments.exp_03_videomae.train --config experiments/exp_03_videomae/configs/default.yaml

# Evaluate
python -m experiments.exp_03_videomae.evaluate --checkpoint outputs/exp_03_videomae.pt

# Inference on a single sample
python -m experiments.exp_03_videomae.inference --input path/to/sample --top-k 5
```

> **Note:** `train.py`, `evaluate.py`, `inference.py` and `models/model.py` are
> runnable skeletons containing `TODO(manual-review)` markers. Drop the original
> VideoMAE implementation into these files to make the experiment fully
> functional. See [`docs/migration_report.md`](../../docs/migration_report.md).
