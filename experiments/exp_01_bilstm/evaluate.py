"""Evaluation entry point for Exp-01 — BiLSTM.

Computes Top-1 / Top-5 accuracy on the EgSL-5K test split.
Reported results for this experiment: Top-1 2.19%, Top-5 7.10% (Rejected).

TODO(manual-review): migrate the original evaluation loop and metric reporting.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from evaluation.metrics import top_k_accuracy
from shared.configs import load_config
from shared.utilities import get_logger

LOGGER = get_logger("exp_01_bilstm.evaluate")
DEFAULT_CONFIG = str(Path(__file__).parent / "configs" / "default.yaml")


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate BiLSTM.")
    parser.add_argument("--config", default=DEFAULT_CONFIG)
    parser.add_argument("--checkpoint", required=False)
    args = parser.parse_args()

    cfg = load_config(args.config)
    LOGGER.info("Evaluating %s with config %s", cfg.experiment_name, cfg.to_dict())
    # TODO(manual-review): load checkpoint, run inference on the test split and
    # report metrics, e.g.:
    #     acc1 = top_k_accuracy(logits, targets, k=1)
    #     acc5 = top_k_accuracy(logits, targets, k=5)
    _ = top_k_accuracy
    raise SystemExit(
        "exp_01_bilstm/evaluate.py is a runnable skeleton; migrate the real eval loop."
    )


if __name__ == "__main__":
    main()
