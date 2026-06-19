# Dataset — EgSL-5K

EgSL-5K is the Egyptian Sign Language dataset used to train and evaluate every
experiment in this repository.

## Summary

| Property | Value |
|----------|-------|
| **Name** | EgSL-5K |
| **Total videos** | 5,000 |
| **Number of classes (glosses)** | 645 |
| **Signers** | 20+ |
| **Resolution** | 1080×1920 (portrait) |
| **Frame rate** | 60 FPS |
| **Modality** | RGB video (also processed into MediaPipe landmarks / skeletons) |

## Splits

The dataset is partitioned into train / validation / test:

| Split | Proportion | Approx. videos |
|-------|-----------|----------------|
| Train | 70% | ~3,500 |
| Validation | 15% | ~750 |
| Test | 15% | ~750 |

Splits are signer-aware where possible to reduce signer-identity leakage between
train and test. <!-- TODO(manual-review): confirm the exact split protocol. -->

## Representations

Each clip is consumed by the experiments in one of three forms:

1. **RGB clips** — raw frames sampled from the video (used by VideoMAE, Exp-03).
2. **MediaPipe landmarks** — per-frame pose + hand keypoints of shape
   `(T, 75, 3)` (used by BiLSTM, Transformer, SPOTER).
3. **Skeleton graphs** — the 27-keypoint ST-GCN layout `(2, 96, 27)` derived
   from the landmarks (used by the OpenHands Decoupled ST-GCN, Exp-05).

See [`architecture.md`](architecture.md) for how raw video is transformed into
each representation.

## Storage & access

The raw EgSL-5K media is **not** stored in this repository (it is large and
access-controlled). `datasets/sample_data/` holds only small, shareable samples
for smoke-testing the pipeline. Configure the dataset root via each experiment's
config (`dataset_root`) or the `--config` flag.

For versioning large files, use **Git LFS** or an external object store; do not
commit raw videos or extracted arrays (see the root `.gitignore`).
