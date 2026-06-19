# Architecture & Pipeline

End-to-end flow from raw video to a deployed prediction:

```
Video
  → MediaPipe Extraction
  → Landmark Processing
  → Format Conversion
  → Model Training
  → Evaluation
  → Deployment
```

## 1. Video

Raw EgSL-5K clips: 1080×1920, 60 FPS RGB video of a single isolated sign.

## 2. MediaPipe Extraction

`preprocessing/mediapipe_extraction/`

MediaPipe Holistic extracts per-frame pose and hand landmarks, producing a
`(T, 75, 3)` array per clip (`T` frames × 75 keypoints × `(x, y, z)`).

## 3. Landmark Processing (Normalization)

`preprocessing/normalization/`

- **Spatial normalization** — center and scale keypoints so the representation
  is invariant to signer position and camera distance.
- **Temporal sampling** — uniformly resample variable-length sequences to a
  fixed length (default 96 frames).

## 4. Format Conversion

`preprocessing/conversion/`

Converts the processed landmarks into the tensor layout each model expects.
A key conversion maps `(96, 75, 3)` → `(2, 96, 27)`:

- select 27 keypoints out of 75,
- keep only `(x, y)` (drop `z`),
- transpose to `(channels, frames, keypoints)` for the ST-GCN family.

## 5. Model Training

`experiments/*/train.py`

Each experiment builds its model from `experiments/<exp>/models/` and trains on
the chosen representation. Shared config and utilities come from `shared/`.

| Experiment | Representation consumed |
|------------|-------------------------|
| Exp-01 BiLSTM | landmark sequences |
| Exp-02 Transformer | landmark sequences |
| Exp-03 VideoMAE | RGB clips |
| Exp-04 SPOTER | landmark sequences |
| Exp-05 OpenHands ST-GCN | skeleton graphs `(2, 96, 27)` |

## 6. Evaluation

`evaluation/` + `experiments/*/evaluate.py`

Top-1 / Top-5 accuracy via `evaluation.metrics.top_k_accuracy`, plus confusion
matrices and other visualizations under `evaluation/visualizations/`.

## 7. Deployment

`inference/`

The final model (Exp-05) is served through:

- `inference/api/` — a FastAPI HTTP endpoint,
- `inference/modal/` — a Modal serverless deployment,
- `inference/utils/` — shared prediction helpers that run the full
  extraction → normalization → conversion → model pipeline at inference time.
