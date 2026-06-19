"""Base experiment configuration shared across all experiments.

Each experiment can subclass :class:`BaseConfig` or load a YAML file that maps
onto these fields. Keeping a single source of truth here avoids duplicating the
same hyper-parameter plumbing in every ``experiments/*/configs`` folder.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Dict, Optional


@dataclass
class BaseConfig:
    """Common training / evaluation configuration.

    Fields intentionally cover the union of settings used by the landmark,
    skeleton and RGB-video experiments. Experiment-specific configs may extend
    this dataclass with extra fields.
    """

    # Experiment identity
    experiment_name: str = "experiment"
    seed: int = 42

    # Data
    dataset_root: str = "datasets/sample_data"
    num_classes: int = 645
    batch_size: int = 32
    num_workers: int = 4

    # Optimisation
    epochs: int = 100
    learning_rate: float = 1e-3
    weight_decay: float = 1e-4

    # Runtime
    device: str = "cuda"
    output_dir: str = "outputs"

    # Free-form extras for experiment-specific knobs.
    extra: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


def load_config(path: Optional[str] = None, **overrides: Any) -> BaseConfig:
    """Load a :class:`BaseConfig` from an optional YAML file plus overrides.

    Parameters
    ----------
    path:
        Optional path to a YAML config file. If ``None``, defaults are used.
    overrides:
        Keyword overrides applied on top of file / default values.
    """

    data: Dict[str, Any] = {}
    if path is not None:
        # Imported lazily so the package can be imported without PyYAML present.
        import yaml  # type: ignore

        with open(Path(path), "r", encoding="utf-8") as handle:
            data = yaml.safe_load(handle) or {}

    known = {f for f in BaseConfig.__dataclass_fields__}  # type: ignore[attr-defined]
    extra = {k: v for k, v in {**data, **overrides}.items() if k not in known}
    base_kwargs = {k: v for k, v in {**data, **overrides}.items() if k in known}
    cfg = BaseConfig(**base_kwargs)
    cfg.extra.update(extra)
    return cfg
