"""Shared dataset / dataloader abstractions.

Three broad input representations are used across the experiments:

- landmark sequences (MediaPipe), used by BiLSTM / Transformer / SPOTER;
- skeleton graphs, used by the OpenHands Decoupled ST-GCN experiment;
- RGB video clips, used by VideoMAE.

The concrete dataset classes below are deliberately thin placeholders. Migrate
the real loading logic from the original experiment scripts and wire it in here
so experiments share a single, tested implementation.
"""

from shared.dataloaders.landmark_dataset import LandmarkSequenceDataset

__all__ = ["LandmarkSequenceDataset"]
