"""BiLSTM model definition for Exp-01 — BiLSTM.

TODO(manual-review): replace this placeholder with the original BiLSTM
implementation. The constructor signature mirrors the experiment config so that
``train.py`` / ``evaluate.py`` can build it directly from the loaded config.
"""

from __future__ import annotations

try:
    import torch.nn as nn  # type: ignore
    _BASE = nn.Module
except ImportError:  # pragma: no cover - torch optional at import time
    class _BASE:  # type: ignore
        pass


class BiLSTMClassifier(_BASE):
    """Placeholder BiLSTM classifier.

    Parameters are accepted as keyword arguments matching the experiment config.
    """

    def __init__(self, num_classes: int = 645, **kwargs) -> None:
        super().__init__()
        self.num_classes = num_classes
        self.hparams = kwargs
        # TODO(manual-review): define the real layers here.

    def forward(self, x):  # noqa: D401 - placeholder
        raise NotImplementedError(
            "BiLSTMClassifier.forward is a placeholder; migrate the real architecture."
        )
