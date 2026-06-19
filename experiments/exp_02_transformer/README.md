# Exp-02 — Transformer

| Field | Value |
|-------|-------|
| **Model** | Transformer |
| **Input** | MediaPipe landmarks |
| **Top-1** | 6.56% |
| **Top-5** | 22.40% |
| **Status** | **Rejected** |

## Overview

A vanilla Transformer encoder over landmark sequences, replacing the recurrent backbone of Exp-01 with self-attention.

## Key findings

Clear improvement over the BiLSTM (Top-5 jumped to 22.4%) but still far below usable accuracy. Confirmed that raw landmark vectors alone are a weak representation. Rejected.

## Folder layout

```
exp_02_transformer/
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
python -m experiments.exp_02_transformer.train --config experiments/exp_02_transformer/configs/default.yaml

# Evaluate
python -m experiments.exp_02_transformer.evaluate --checkpoint outputs/exp_02_transformer.pt

# Inference on a single sample
python -m experiments.exp_02_transformer.inference --input path/to/sample --top-k 5
```

> **Note:** `train.py`, `evaluate.py`, `inference.py` and `models/model.py` are
> runnable skeletons containing `TODO(manual-review)` markers. Drop the original
> Transformer implementation into these files to make the experiment fully
> functional. See [`docs/migration_report.md`](../../docs/migration_report.md).
