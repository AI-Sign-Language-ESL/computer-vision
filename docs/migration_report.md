# Migration Report

This report documents the refactor of the `computer-vision` repository into the
research-oriented TAFAHOM structure.

## Starting point

At migration time the repository contained **only**:

```
computer-vision/
├── LICENSE        # GNU GPL v3
└── README.md      # single line: "# computer-vision"
```

There was **no existing experiment / model / preprocessing code to migrate**.
Consequently this migration *scaffolds* the target structure rather than moving
existing files. Every experiment script and model definition is a **runnable
skeleton** containing `TODO(manual-review)` markers indicating exactly where the
original research code should be dropped in.

> If/when the original experiment codebases become available, move their files
> into the matching folders below (prefer `git mv` to preserve history) and
> replace the corresponding skeletons.

## Resulting structure

```
computer-vision/
├── README.md  LICENSE  .gitignore  requirements.txt  environment.yml
├── docs/        experiment_log.md  dataset.md  architecture.md  migration_report.md
├── datasets/    sample_data/  README.md
├── preprocessing/  mediapipe_extraction/  normalization/  conversion/
├── experiments/    exp_01_bilstm/ exp_02_transformer/ exp_03_videomae/
│                    exp_04_spoter/ exp_05_openhands/
├── inference/      api/  modal/  utils/
├── evaluation/     metrics/  visualizations/
├── notebooks/
└── shared/         configs/  dataloaders/  utilities/
```

Each `experiments/exp_*` folder contains: `README.md`, `train.py`,
`evaluate.py`, `inference.py`, `requirements.txt`, `configs/` (with
`default.yaml`) and `models/` (with `model.py`).

## Files / areas that require manual review

All items below are marked in-code with `TODO(manual-review)`:

| Location | What to migrate / confirm |
|----------|---------------------------|
| `experiments/*/train.py` | Real training loop (loss, optimizer, schedule, checkpointing) |
| `experiments/*/evaluate.py` | Real evaluation loop + metric reporting |
| `experiments/*/inference.py` | Real single-sample inference pipeline |
| `experiments/*/models/model.py` | Original architecture for each model |
| `preprocessing/mediapipe_extraction/extract_landmarks.py` | Exact MediaPipe config + 75-keypoint layout; batch CLI |
| `preprocessing/normalization/normalize.py` | Reference keypoint / scaling convention |
| `preprocessing/conversion/convert.py` | The real 27-keypoint subset & ordering for `(2, 96, 27)` |
| `shared/dataloaders/landmark_dataset.py` | Dataset indexing + sample decoding |
| `shared/utilities/checkpoint.py` | Serialization format alignment |
| `inference/utils/predict.py` | Model load + full inference pipeline |
| `inference/api/app.py` | Checkpoint config + upload handling |
| `inference/modal/deploy.py` | Modal image/GPU spec + model mounting |
| `evaluation/visualizations/confusion.py` | Plot styling alignment |
| `docs/dataset.md` | Confirm exact split protocol (signer-aware?) |

To list every marker:

```bash
grep -rn "TODO(manual-review)" .
```

## Import paths / conventions introduced

Because experiments import shared code, all scripts are intended to run as
**modules from the repository root** so packages resolve on `PYTHONPATH`:

```bash
python -m experiments.exp_05_openhands.train
```

New importable packages and their public entry points:

| Import | Provides |
|--------|----------|
| `shared.configs` | `BaseConfig`, `load_config` |
| `shared.utilities` | `get_logger`, `set_seed` (+ `checkpoint` helpers) |
| `shared.dataloaders` | `LandmarkSequenceDataset` |
| `preprocessing.mediapipe_extraction` | `extract_landmarks` |
| `preprocessing.normalization` | `normalize_landmarks`, `temporal_sample` |
| `preprocessing.conversion` | `to_stgcn_layout` |
| `evaluation.metrics` | `top_k_accuracy` |
| `evaluation.visualizations` | `plot_confusion_matrix` |
| `inference.utils` | `Predictor` |
| `experiments.exp_XX_*.models` | the experiment's model class |

> No pre-existing imports were *changed* (there was no prior code); the table
> above is the set of import paths newly established by this structure.

## Security

The `.gitignore` was expanded to exclude:

- secrets / credentials (`.env`, `*.key`, `*.pem`, `credentials.json`, `*token*`, …),
- large model checkpoints (`*.pt`, `*.pth`, `*.ckpt`, `*.safetensors`, `outputs/`, …),
- raw datasets / media (`datasets/**` except `README.md` + `sample_data/`,
  `*.mp4`, `*.npy`, …).

No secrets, API keys, tokens or private data were found or committed.
**Recommendation:** use **Git LFS** for any large files that must be versioned.

## Commands to verify the repository

```bash
# 1. Byte-compile everything
python -m compileall shared preprocessing inference evaluation experiments

# 2. Import smoke test (requires `pip install pyyaml`)
python -c "import shared.configs, shared.utilities, evaluation.metrics, \
preprocessing.conversion, experiments.exp_05_openhands.models; \
from shared.configs import load_config; \
print(load_config('experiments/exp_05_openhands/configs/default.yaml').experiment_name)"

# 3. Run a skeleton entry point (exits with a clear 'migrate the real ...' note)
python -m experiments.exp_05_openhands.train --epochs 1

# 4. List everything still needing manual work
grep -rn "TODO(manual-review)" .
```
