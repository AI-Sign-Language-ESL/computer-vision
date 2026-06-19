# Datasets

This directory holds dataset **placeholders and small samples only**. The full
EgSL-5K dataset is large and access-controlled and is **never** committed here
(see the root `.gitignore`).

## Contents

```
datasets/
├── README.md         # this file
└── sample_data/      # tiny, shareable samples for smoke-testing the pipeline
```

## EgSL-5K

| Property | Value |
|----------|-------|
| Total videos | 5,000 |
| Classes | 645 |
| Signers | 20+ |
| Resolution | 1080×1920 |
| Frame rate | 60 FPS |
| Split | 70% train / 15% val / 15% test |

Full documentation: [`../docs/dataset.md`](../docs/dataset.md).

## Obtaining the data

The raw dataset is distributed separately. Point experiments at your local copy
via the `dataset_root` field in each experiment config or the `--config` flag.

## Handling large files

Do **not** `git add` raw videos, extracted landmark arrays, or model
checkpoints. For versioned large files use **Git LFS**:

```bash
git lfs install
git lfs track "*.mp4" "*.npy"
```

Or keep them in external object storage (S3/GCS) referenced by config.
