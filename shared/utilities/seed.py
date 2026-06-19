"""Reproducibility helpers shared by all experiments."""

from __future__ import annotations

import os
import random


def set_seed(seed: int = 42, deterministic: bool = True) -> None:
    """Seed Python, NumPy and (if available) PyTorch RNGs.

    Heavy ML dependencies are imported lazily so this helper works even in a
    minimal environment that only has the standard library installed.
    """

    os.environ["PYTHONHASHSEED"] = str(seed)
    random.seed(seed)

    try:
        import numpy as np  # type: ignore

        np.random.seed(seed)
    except ImportError:  # pragma: no cover - numpy optional at import time
        pass

    try:
        import torch  # type: ignore

        torch.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
        if deterministic:
            torch.backends.cudnn.deterministic = True
            torch.backends.cudnn.benchmark = False
    except ImportError:  # pragma: no cover - torch optional at import time
        pass
