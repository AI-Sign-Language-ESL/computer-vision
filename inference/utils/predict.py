"""Prediction utility wrapping the final (Exp-05 OpenHands ST-GCN) model.

TODO(manual-review): wire this to the real model loading + preprocessing once
the Exp-05 model code is migrated into ``experiments/exp_05_openhands/models``.
"""

from __future__ import annotations

from typing import List, Optional


class Predictor:
    """Load a trained model and run single-clip predictions."""

    def __init__(self, checkpoint_path: str, num_classes: int = 645,
                 device: str = "cpu") -> None:
        self.checkpoint_path = checkpoint_path
        self.num_classes = num_classes
        self.device = device
        self.model = None  # TODO(manual-review): load the model here.

    def predict(self, video_path: str, top_k: int = 5) -> List[dict]:
        """Return the top-k predictions for a single video clip."""

        raise NotImplementedError(
            "Predictor.predict is a placeholder; migrate the inference pipeline "
            "(extraction -> normalization -> conversion -> model) here."
        )
