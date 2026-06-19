"""Modal serverless deployment for the TAFAHOM inference service.

Deploy with::

    modal deploy inference/modal/deploy.py

NOTE: never hard-code secrets here. Use ``modal.Secret`` references and provide
values via the Modal dashboard or CLI.

TODO(manual-review): port the real Modal image definition, GPU spec and model
mounting from the original deployment script.
"""

from __future__ import annotations

try:
    import modal  # type: ignore
except ImportError:  # pragma: no cover - modal optional at import time
    modal = None  # type: ignore


if modal is not None:
    app = modal.App("tafahom-inference")
    image = modal.Image.debian_slim().pip_install("torch", "numpy")

    @app.function(image=image, gpu="any")
    def predict_remote(payload: dict) -> dict:
        # TODO(manual-review): load model and run inference on Modal.
        return {"detail": "not_implemented"}
else:  # pragma: no cover
    app = None
