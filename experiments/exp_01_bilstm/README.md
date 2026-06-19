# Exp-01 — BiLSTM

| Field | Value |
|-------|-------|
| **Model** | BiLSTM |
| **Input** | MediaPipe landmarks |
| **Top-1** | 2.19% |
| **Top-5** | 7.10% |
| **Status** | **Rejected** |

## Overview

A bidirectional LSTM over per-frame MediaPipe landmark vectors. This was the first baseline and established the landmark input pipeline.

## Key findings

Severely underfit the 645-class problem; recurrent modelling of raw landmark vectors did not capture the fine-grained hand shape distinctions needed. Rejected as a viable direction.

## Folder layout

```
exp_01_bilstm/
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
python -m experiments.exp_01_bilstm.train --config experiments/exp_01_bilstm/configs/default.yaml

# Evaluate
python -m experiments.exp_01_bilstm.evaluate --checkpoint outputs/exp_01_bilstm.pt

# Inference on a single sample
python -m experiments.exp_01_bilstm.inference --input path/to/sample --top-k 5
```

> **Note:** `train.py`, `evaluate.py`, `inference.py` and `models/model.py` are
> runnable skeletons containing `TODO(manual-review)` markers. Drop the original
> BiLSTM implementation into these files to make the experiment fully
> functional. See [`docs/migration_report.md`](../../docs/migration_report.md).
