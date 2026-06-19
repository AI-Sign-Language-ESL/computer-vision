"""Training entry point for Exp-05 — OpenHands Decoupled ST-GCN.

Model: Decoupled ST-GCN
Input: Skeleton data
Reported results: Top-1 22.67%, Top-5 52.79% (status: Final).

TODO(manual-review): this is a runnable skeleton. Migrate the original training
loop (loss, optimizer schedule, logging, checkpointing) for this experiment.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from shared.configs import load_config
from shared.utilities import get_logger, set_seed

LOGGER = get_logger("exp_05_openhands.train")
DEFAULT_CONFIG = str(Path(__file__).parent / "configs" / "default.yaml")


def main() -> None:
    parser = argparse.ArgumentParser(description="Train Decoupled ST-GCN.")
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
        "exp_05_openhands/train.py is a runnable skeleton; migrate the real training loop."
    )


if __name__ == "__main__":
    main()
