"""Confusion-matrix visualization helper.

TODO(manual-review): align styling (class label ordering, figure size, colour
map) with whatever the original evaluation scripts produced.
"""

from __future__ import annotations

from typing import Optional, Sequence


def plot_confusion_matrix(y_true, y_pred, labels: Optional[Sequence[str]] = None,
                          output_path: Optional[str] = None):
    """Render a confusion matrix and optionally save it to ``output_path``."""

    import matplotlib.pyplot as plt  # type: ignore
    import numpy as np  # type: ignore
    from sklearn.metrics import confusion_matrix  # type: ignore

    cm = confusion_matrix(y_true, y_pred)
    fig, ax = plt.subplots(figsize=(10, 10))
    im = ax.imshow(cm, interpolation="nearest", cmap="Blues")
    fig.colorbar(im, ax=ax)
    ax.set_xlabel("Predicted")
    ax.set_ylabel("True")
    if labels is not None:
        ax.set_xticks(np.arange(len(labels)))
        ax.set_yticks(np.arange(len(labels)))
        ax.set_xticklabels(labels, rotation=90)
        ax.set_yticklabels(labels)
    if output_path is not None:
        fig.savefig(output_path, bbox_inches="tight", dpi=150)
    return fig
