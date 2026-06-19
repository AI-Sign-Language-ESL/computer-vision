# TAFAHOM — Egyptian Sign Language Recognition (Computer Vision)

> Research monorepo consolidating all computer-vision experiments for the
> **TAFAHOM** Egyptian Sign Language (EgSL) recognition project.

## Project overview

TAFAHOM aims to translate Egyptian Sign Language into text by recognising
isolated signs from video. This repository consolidates every modelling
experiment conducted during the research — from landmark-based recurrent models
to skeleton graph networks — into a single, reproducible structure with shared
preprocessing, evaluation and inference components.

## What is TAFAHOM?

**TAFAHOM** (تفاهم, "mutual understanding") is the umbrella project for building
an accessible Egyptian Sign Language understanding system. The computer-vision
component in this repo is responsible for the core recognition model: given a
short video of a single sign, predict the corresponding gloss out of 645
classes.

## EgSL-5K dataset

The models are trained and evaluated on **EgSL-5K**, an Egyptian Sign Language
dataset:

| Property | Value |
|----------|-------|
| Total videos | 5,000 |
| Classes (glosses) | 645 |
| Signers | 20+ |
| Resolution | 1080×1920 |
| Frame rate | 60 FPS |
| Split | 70% train / 15% val / 15% test |

See [`docs/dataset.md`](docs/dataset.md) for full details. The raw dataset is
**not** committed to this repository (see [Security](#security)).

## Research workflow

```
Video
  → MediaPipe Extraction      (preprocessing/mediapipe_extraction)
  → Landmark Processing        (preprocessing/normalization)
  → Format Conversion          (preprocessing/conversion)
  → Model Training             (experiments/*/train.py)
  → Evaluation                 (evaluation/ + experiments/*/evaluate.py)
  → Deployment                 (inference/)
```

See [`docs/architecture.md`](docs/architecture.md) for the detailed pipeline.

## Experiment comparison

| ID | Model | Input | Top-1 | Top-5 | Status |
|----|-------|-------|-------|-------|--------|
| Exp-01 | BiLSTM | MediaPipe landmarks | 2.19% | 7.10% | Rejected |
| Exp-02 | Transformer | MediaPipe landmarks | 6.56% | 22.40% | Rejected |
| Exp-03 | VideoMAE | RGB videos | 22.40% | 55.00% | Baseline |
| Exp-04 | SPOTER | Landmark sequences | 24.55% | 44.11% | Baseline |
| Exp-05 | OpenHands Decoupled ST-GCN | Skeleton data | 22.67% | 52.79% | **Final** |

The full chronological narrative is in
[`docs/experiment_log.md`](docs/experiment_log.md).

## Installation

### Using conda (recommended)

```bash
conda env create -f environment.yml
conda activate tafahom
```

### Using pip

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Each experiment additionally has its own `requirements.txt` (which includes the
root one) for any model-specific dependencies:

```bash
pip install -r experiments/exp_05_openhands/requirements.txt
```

## Repository structure

```
computer-vision/
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── environment.yml
├── docs/                      # project documentation
│   ├── experiment_log.md
│   ├── dataset.md
│   ├── architecture.md
│   └── migration_report.md
├── datasets/                  # dataset placeholders (raw data NOT committed)
│   ├── sample_data/
│   └── README.md
├── preprocessing/             # video → landmark → tensor pipeline
│   ├── mediapipe_extraction/
│   ├── normalization/
│   └── conversion/
├── experiments/               # one folder per modelling experiment
│   ├── exp_01_bilstm/
│   ├── exp_02_transformer/
│   ├── exp_03_videomae/
│   ├── exp_04_spoter/
│   └── exp_05_openhands/
├── inference/                 # serving & deployment
│   ├── api/
│   ├── modal/
│   └── utils/
├── evaluation/                # metrics & visualizations
│   ├── metrics/
│   └── visualizations/
├── notebooks/                 # exploratory notebooks
└── shared/                    # reusable cross-experiment code
    ├── configs/
    ├── dataloaders/
    └── utilities/
```

## Training

Run experiments as modules from the repository root so the `shared`,
`evaluation` and `preprocessing` packages are importable:

```bash
python -m experiments.exp_05_openhands.train \
    --config experiments/exp_05_openhands/configs/default.yaml
```

## Evaluation

```bash
python -m experiments.exp_05_openhands.evaluate \
    --checkpoint outputs/exp_05_openhands.pt
```

Shared metrics (`top_k_accuracy`, confusion matrices) live under
[`evaluation/`](evaluation).

## Inference

Single-sample prediction:

```bash
python -m experiments.exp_05_openhands.inference --input path/to/clip.mp4 --top-k 5
```

Serve the final model via the API:

```bash
uvicorn inference.api.app:app --reload
# POST a video file to http://localhost:8000/predict
```

Serverless deployment templates are in [`inference/modal/`](inference/modal).

> **Status of the code:** the experiment `train.py` / `evaluate.py` /
> `inference.py` and `models/model.py` files are runnable skeletons that wire up
> config + shared utilities and contain `TODO(manual-review)` markers where the
> original model logic should be migrated in. See
> [`docs/migration_report.md`](docs/migration_report.md).

## Citation

If you use this work, please cite:

```bibtex
@misc{tafahom_egsl,
  title        = {TAFAHOM: Egyptian Sign Language Recognition},
  author       = {AI Sign Language ESL Team},
  year         = {2025},
  howpublished = {\url{https://github.com/AI-Sign-Language-ESL/computer-vision}}
}
```

## License

Released under the terms of the [GNU GPL v3](LICENSE).
