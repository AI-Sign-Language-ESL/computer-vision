"""Training entry point for Exp-02 — Transformer.

Model: Transformer
Input: MediaPipe landmarks
Reported results: Top-1 6.56%, Top-5 22.40% (status: Rejected).

TODO(manual-review): this is a runnable skeleton. Migrate the original training
loop (loss, optimizer schedule, logging, checkpointing) for this experiment.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from shared.configs import load_config
from shared.utilities import get_logger, set_seed

LOGGER = get_logger("exp_02_transformer.train")
DEFAULT_CONFIG = str(Path(__file__).parent / "configs" / "default.yaml")


def main() -> None:
    parser = argparse.ArgumentParser(description="Train Transformer.")
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
        "exp_02_transformer/train.py is a runnable skeleton; migrate the real training loop."
    )


if __name__ == "__main__":
    main()
