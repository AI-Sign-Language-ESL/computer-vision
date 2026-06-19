"""Single-sample inference entry point for Exp-03 — VideoMAE.

TODO(manual-review): migrate the original inference / preprocessing pipeline for
this model.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from shared.configs import load_config
from shared.utilities import get_logger

LOGGER = get_logger("exp_03_videomae.inference")
DEFAULT_CONFIG = str(Path(__file__).parent / "configs" / "default.yaml")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run VideoMAE inference.")
    parser.add_argument("--config", default=DEFAULT_CONFIG)
    parser.add_argument("--input", required=True, help="Path to input sample.")
    parser.add_argument("--checkpoint", required=False)
    parser.add_argument("--top-k", type=int, default=5)
    args = parser.parse_args()

    cfg = load_config(args.config)
    LOGGER.info("Running inference for %s on %s", cfg.experiment_name, args.input)
    # TODO(manual-review): load model + checkpoint and return top-k predictions.
    raise SystemExit(
        "exp_03_videomae/inference.py is a runnable skeleton; migrate the real pipeline."
    )


if __name__ == "__main__":
    main()
