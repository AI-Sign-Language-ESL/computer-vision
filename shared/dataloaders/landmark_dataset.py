"""Landmark-sequence dataset shared by landmark-based experiments.

TODO(manual-review): replace the placeholder ``__getitem__`` with the real
loading / decoding logic from the original BiLSTM, Transformer and SPOTER
experiment code once it is available.
"""

from __future__ import annotations

from pathlib import Path
from typing import List, Tuple

try:  # torch is optional at import time so the package stays importable
    from torch.utils.data import Dataset  # type: ignore
except ImportError:  # pragma: no cover
    class Dataset:  # type: ignore
        """Minimal stand-in used when torch is not installed."""


class LandmarkSequenceDataset(Dataset):
    """Dataset of MediaPipe landmark sequences for sign classification.

    Parameters
    ----------
    root:
        Directory containing per-sample landmark files.
    split:
        One of ``"train"``, ``"val"`` or ``"test"``.
    """

    def __init__(self, root: str, split: str = "train") -> None:
        self.root = Path(root)
        self.split = split
        self.samples: List[Tuple[Path, int]] = self._index_samples()

    def _index_samples(self) -> List[Tuple[Path, int]]:
        # TODO(manual-review): build the (path, label) index from the dataset
        # manifest used by the original experiments (e.g. a CSV split file).
        return []

    def __len__(self) -> int:
        return len(self.samples)

    def __getitem__(self, index: int):  # noqa: D401 - placeholder
        raise NotImplementedError(
            "LandmarkSequenceDataset.__getitem__ is a placeholder. "
            "Migrate the real landmark loading logic here."
        )
