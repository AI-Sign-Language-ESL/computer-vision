"""Spatial and temporal normalization of landmark sequences.

TODO(manual-review): confirm the reference keypoint and scaling convention used
by the original experiments (e.g. centering on the neck/torso, scaling by
shoulder width) before relying on these implementations.
"""

from __future__ import annotations


def normalize_landmarks(landmarks):
    """Center and scale a ``(T, K, C)`` landmark array.

    The default convention centers each frame on the mean keypoint position and
    scales by the per-frame standard deviation. Adjust to match the original
    experiment preprocessing.
    """

    import numpy as np  # type: ignore

    arr = np.asarray(landmarks, dtype="float32")
    if arr.size == 0:
        return arr
    center = arr.mean(axis=1, keepdims=True)
    scale = arr.std(axis=1, keepdims=True) + 1e-6
    return (arr - center) / scale


def temporal_sample(landmarks, num_frames: int = 96):
    """Uniformly resample a sequence to exactly ``num_frames`` frames."""

    import numpy as np  # type: ignore

    arr = np.asarray(landmarks)
    if arr.shape[0] == 0:
        return arr
    idx = np.linspace(0, arr.shape[0] - 1, num=num_frames).round().astype(int)
    return arr[idx]
