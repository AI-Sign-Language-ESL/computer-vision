"""Shared, reusable components for the TAFAHOM Egyptian Sign Language project.

This package collects code that is common across multiple experiments so that
individual experiment folders avoid duplicating logic. Sub-packages:

- ``shared.configs``: base configuration dataclasses and loaders.
- ``shared.dataloaders``: dataset / dataloader abstractions for landmark,
  skeleton and RGB-video inputs.
- ``shared.utilities``: logging, seeding, checkpoint and metric helpers.
"""
