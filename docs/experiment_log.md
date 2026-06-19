# Experiment Log

A chronological history of the modelling experiments for TAFAHOM / EgSL-5K.
Each entry records the objective, input representation, results, key findings and
the decision (rejected / baseline / final).

| ID | Model | Input | Top-1 | Top-5 | Status |
|----|-------|-------|-------|-------|--------|
| Exp-01 | BiLSTM | MediaPipe landmarks | 2.19% | 7.10% | Rejected |
| Exp-02 | Transformer | MediaPipe landmarks | 6.56% | 22.40% | Rejected |
| Exp-03 | VideoMAE | RGB videos | 22.40% | 55.00% | Baseline |
| Exp-04 | SPOTER | Landmark sequences | 24.55% | 44.11% | Baseline |
| Exp-05 | OpenHands Decoupled ST-GCN | Skeleton data | 22.67% | 52.79% | **Final** |

---

## Exp-01 — BiLSTM

- **Objective:** Establish a first end-to-end baseline and validate the
  MediaPipe landmark extraction pipeline.
- **Input representation:** Per-frame MediaPipe landmark vectors fed to a
  bidirectional LSTM.
- **Results:** Top-1 **2.19%**, Top-5 **7.10%**.
- **Key findings:** The model badly underfits a 645-class problem. Recurrent
  modelling of raw landmark vectors fails to capture the fine-grained hand-shape
  distinctions that separate signs.
- **Decision:** **Rejected.** Useful only as a sanity check that the data
  pipeline and training loop work end-to-end.

## Exp-02 — Transformer

- **Objective:** Test whether self-attention captures temporal structure better
  than recurrence on the same landmark input.
- **Input representation:** MediaPipe landmark sequences into a vanilla
  Transformer encoder.
- **Results:** Top-1 **6.56%**, Top-5 **22.40%**.
- **Key findings:** ~3× the BiLSTM's Top-1 and a large Top-5 jump, confirming
  attention helps — but absolute accuracy is still far from usable. Strongly
  suggested that *raw landmark vectors* are a weak representation regardless of
  the sequence model.
- **Decision:** **Rejected**, but motivated trying (a) richer input encodings
  and (b) pretrained backbones.

## Exp-03 — VideoMAE

- **Objective:** Sidestep landmark extraction and leverage large-scale
  pretraining by fine-tuning a video foundation model directly on RGB clips.
- **Input representation:** Sampled RGB video frames.
- **Results:** Top-1 **22.40%**, Top-5 **55.00%**.
- **Key findings:** A dramatic jump in accuracy from pretrained spatiotemporal
  features — the best Top-5 of all experiments. Downsides: heavy compute, large
  checkpoints, and slow inference, making deployment expensive.
- **Decision:** **Baseline.** Retained as the strong RGB reference point.

## Exp-04 — SPOTER

- **Objective:** Use a landmark-native architecture purpose-built for sign
  recognition rather than a generic sequence model.
- **Input representation:** Landmark sequences into SPOTER (Sign POse-based
  TransformER) with learned queries.
- **Results:** Top-1 **24.55%**, Top-5 **44.11%**.
- **Key findings:** Best **Top-1** of all experiments and far cheaper than
  VideoMAE. Demonstrated that a well-designed landmark model rivals the RGB
  foundation model at a fraction of the cost.
- **Decision:** **Baseline.** Strong, efficient landmark reference.

## Exp-05 — OpenHands Decoupled ST-GCN

- **Objective:** Model the skeleton explicitly as a spatiotemporal graph and
  optimise the accuracy/efficiency trade-off for deployment.
- **Input representation:** Skeleton graphs in the `(2, 96, 27)` layout derived
  from the landmarks.
- **Results:** Top-1 **22.67%**, Top-5 **52.79%**.
- **Key findings:** Competitive Top-1 with the best Top-5 among the efficient
  (non-RGB) models, while being lightweight and fast — the best overall balance
  of accuracy, model size and inference latency.
- **Decision:** **Final / Selected.** This is the model served by the
  `inference/` package.

---

## Takeaways

1. Raw landmark vectors + generic sequence models (Exp-01/02) are insufficient.
2. Pretraining (VideoMAE) and task-specific design (SPOTER) both close the gap,
   from opposite directions (RGB vs. landmarks).
3. Treating the skeleton as a graph (ST-GCN) gives the best deployable
   trade-off, which is why **Exp-05 was selected as the final model**.
