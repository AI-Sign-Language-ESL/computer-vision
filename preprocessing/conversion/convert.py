"""Convert landmark tensors between experiment-specific layouts.

A common conversion in this project maps a ``(96, 75, 3)`` landmark sequence
(frames, keypoints, coords) into the ``(2, 96, 27)`` layout
(coords, frames, selected-keypoints) expected by the Decoupled ST-GCN model.

TODO(manual-review): confirm the exact 27-keypoint subset and ordering used by
the OpenHands ST-GCN experiment before treating this as production-ready.
"""

from __future__ import annotations

from typing import Sequence

# Placeholder keypoint selection (27 of 75). Replace with the real indices.
DEFAULT_STGCN_KEYPOINTS: Sequence[int] = tuple(range(27))


def to_stgcn_layout(landmarks, keypoints: Sequence[int] = DEFAULT_STGCN_KEYPOINTS):
    """Convert ``(T, 75, 3)`` landmarks to ``(2, T, len(keypoints))``.

    Only the ``(x, y)`` coordinates are kept (the ``z`` channel is dropped),
    matching the 2-channel ST-GCN input convention.
    """

    import numpy as np  # type: ignore

    arr = np.asarray(landmarks, dtype="float32")  # (T, 75, 3)
    selected = arr[:, list(keypoints), :2]         # (T, V, 2)
    return np.transpose(selected, (2, 0, 1))       # (2, T, V)
