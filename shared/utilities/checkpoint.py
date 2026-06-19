"""Checkpoint save / load helpers shared across experiments.

TODO(manual-review): align this with the actual serialization format used by
the original experiment scripts once that code is migrated in.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict


def save_checkpoint(state: Dict[str, Any], path: str) -> str:
    """Persist a training state dictionary to ``path``."""

    import torch  # type: ignore

    Path(path).parent.mkdir(parents=True, exist_ok=True)
    torch.save(state, path)
    return path


def load_checkpoint(path: str, map_location: str = "cpu") -> Dict[str, Any]:
    """Load a checkpoint previously written by :func:`save_checkpoint`."""

    import torch  # type: ignore

    return torch.load(path, map_location=map_location)
