"""FastAPI application exposing the TAFAHOM inference endpoint.

Run locally with::

    uvicorn inference.api.app:app --reload

TODO(manual-review): load the real checkpoint path from configuration / env and
replace the placeholder predictor wiring.
"""

from __future__ import annotations

import os

try:
    from fastapi import FastAPI, UploadFile  # type: ignore
except ImportError:  # pragma: no cover - fastapi optional at import time
    FastAPI = None  # type: ignore
    UploadFile = None  # type: ignore

from inference.utils.predict import Predictor

CHECKPOINT_PATH = os.environ.get("TAFAHOM_CHECKPOINT", "outputs/exp_05_final.pt")


def create_app():
    """Construct and return the FastAPI app instance."""

    if FastAPI is None:  # pragma: no cover
        raise RuntimeError("fastapi is not installed; `pip install fastapi`.")

    app = FastAPI(title="TAFAHOM Egyptian Sign Language API")
    predictor = Predictor(CHECKPOINT_PATH)

    @app.get("/health")
    def health() -> dict:
        return {"status": "ok"}

    @app.post("/predict")
    async def predict(file: "UploadFile"):  # type: ignore[valid-type]
        # TODO(manual-review): persist the upload to a temp file and call
        # predictor.predict on it.
        return {"detail": "not_implemented", "filename": file.filename}

    return app


app = create_app() if FastAPI is not None else None
