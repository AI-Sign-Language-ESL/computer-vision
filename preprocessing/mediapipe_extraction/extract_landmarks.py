"""Extract MediaPipe Holistic landmarks from EgSL-5K videos.

This module produces per-frame landmark arrays (pose + both hands) for each
input video. The output is a ``(T, 75, 3)`` array per clip by default, i.e.
``T`` frames, 75 keypoints, ``(x, y, z)`` coordinates.

TODO(manual-review): port the exact MediaPipe configuration (model complexity,
confidence thresholds, keypoint selection) from the original extraction script.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import List


def extract_landmarks(video_path: str) -> "object":
    """Return a ``(T, 75, 3)`` landmark array for a single video.

    Notes
    -----
    Heavy dependencies (``mediapipe``, ``opencv-python``, ``numpy``) are
    imported lazily so importing this module does not require them.
    """

    import cv2  # type: ignore
    import mediapipe as mp  # type: ignore
    import numpy as np  # type: ignore

    holistic = mp.solutions.holistic.Holistic(static_image_mode=False)
    capture = cv2.VideoCapture(str(video_path))

    frames: List["np.ndarray"] = []
    try:
        while True:
            ok, frame = capture.read()
            if not ok:
                break
            # TODO(manual-review): convert MediaPipe results into the exact
            # 75-keypoint layout used by the downstream experiments.
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            _ = holistic.process(rgb)
            frames.append(np.zeros((75, 3), dtype="float32"))
    finally:
        capture.release()
        holistic.close()

    return np.stack(frames) if frames else np.zeros((0, 75, 3), dtype="float32")


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract MediaPipe landmarks.")
    parser.add_argument("--input", required=True, help="Input video file or dir.")
    parser.add_argument("--output", required=True, help="Output directory.")
    args = parser.parse_args()

    out_dir = Path(args.output)
    out_dir.mkdir(parents=True, exist_ok=True)
    # TODO(manual-review): iterate over the dataset and persist landmark arrays.
    raise SystemExit(
        "extract_landmarks CLI is a placeholder; migrate batch extraction here."
    )


if __name__ == "__main__":
    main()
