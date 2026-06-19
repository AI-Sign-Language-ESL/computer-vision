"""Top-k accuracy and related classification metrics.

These are framework-agnostic and operate on logits / probability arrays so they
can be reused by every experiment's ``evaluate.py``.
"""

from __future__ import annotations


def top_k_accuracy(logits, targets, k: int = 1) -> float:
    """Compute top-k accuracy.

    Parameters
    ----------
    logits:
        Array of shape ``(N, num_classes)``.
    targets:
        Integer array of shape ``(N,)`` with ground-truth class indices.
    k:
        The ``k`` in top-k.
    """

    import numpy as np  # type: ignore

    logits = np.asarray(logits)
    targets = np.asarray(targets)
    if logits.shape[0] == 0:
        return 0.0
    topk = np.argsort(-logits, axis=1)[:, :k]
    hits = (topk == targets[:, None]).any(axis=1)
    return float(hits.mean())
