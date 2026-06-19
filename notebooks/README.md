# Notebooks

Exploratory and analysis notebooks (EDA, landmark visualization, error
analysis, ablations).

Keep notebooks lightweight and reproducible:

- Clear outputs before committing (`jupyter nbconvert --clear-output`).
- Import shared logic from `shared/`, `preprocessing/` and `evaluation/` rather
  than copy-pasting code, so notebooks stay in sync with the library.
- Do not embed large data or media; reference files under `datasets/` instead.
