"""Training entry point for Exp-03 — VideoMAE.

Model: VideoMAE
Input: RGB videos
Reported results: Top-1 22.40%, Top-5 55.00% (status: Baseline).

TODO(manual-review): this is a runnable skeleton. Migrate the original training
loop (loss, optimizer schedule, logging, checkpointing) for this experiment.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from shared.configs import load_config
from shared.utilities import get_logger, set_seed

LOGGER = get_logger("exp_03_videomae.train")
DEFAULT_CONFIG = str(Path(__file__).parent / "configs" / "default.yaml")


def main() -> None:
    parser = argparse.ArgumentParser(description="Train VideoMAE.")
    parser.add_argument("--config", default=DEFAULT_CONFIG)
    parser.add_argument("--epochs", type=int, default=None)
    args = parser.parse_args()

    overrides = {}
    if args.epochs is not None:
        overrides["epochs"] = args.epochs
    cfg = load_config(args.config, **overrides)
    set_seed(cfg.seed)

    LOGGER.info("Loaded config for %s: %s", cfg.experiment_name, cfg.to_dict())
    # TODO(manual-review): build model from .models, build dataloaders from
    # shared.dataloaders, and run the training loop.
    raise SystemExit(
        "exp_03_videomae/train.py is a runnable skeleton; migrate the real training loop."
    )


if __name__ == "__main__":
    main()
