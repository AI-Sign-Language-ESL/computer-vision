# Exp-05 — OpenHands Decoupled ST-GCN

| Field | Value |
|-------|-------|
| **Model** | Decoupled ST-GCN |
| **Input** | Skeleton data |
| **Top-1** | 22.67% |
| **Top-5** | 52.79% |
| **Status** | **Final** |

## Overview

OpenHands Decoupled Spatial-Temporal GCN operating on skeleton graphs built from the selected 27 keypoints (input layout (2, 96, 27)).

## Key findings

Best overall trade-off: competitive Top-1, strong Top-5 (52.79%), lightweight and fast for deployment. Selected as the FINAL model and is the one served by the inference package.

## Folder layout

```
exp_05_openhands/
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
python -m experiments.exp_05_openhands.train --config experiments/exp_05_openhands/configs/default.yaml

# Evaluate
python -m experiments.exp_05_openhands.evaluate --checkpoint outputs/exp_05_openhands.pt

# Inference on a single sample
python -m experiments.exp_05_openhands.inference --input path/to/sample --top-k 5
```

> **Note:** `train.py`, `evaluate.py`, `inference.py` and `models/model.py` are
> runnable skeletons containing `TODO(manual-review)` markers. Drop the original
> Decoupled ST-GCN implementation into these files to make the experiment fully
> functional. See [`docs/migration_report.md`](../../docs/migration_report.md).
