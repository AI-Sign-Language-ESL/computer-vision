"""Preprocessing pipeline for the EgSL-5K dataset.

Sub-packages:

- ``preprocessing.mediapipe_extraction``: extract pose / hand landmarks from raw
  videos using MediaPipe.
- ``preprocessing.normalization``: spatial / temporal normalization of
  landmark sequences.
- ``preprocessing.conversion``: tensor layout conversions between experiments,
  e.g. ``(96, 75, 3) -> (2, 96, 27)`` for the ST-GCN family.
"""
