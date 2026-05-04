# This file runs the expanded model comparison used in the final project revision.
# It is kept as a notebook-style entry point for the course milestone.
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[1]
runpy.run_path(str(ROOT / "notebooks" / "ml_compare.py"), run_name="__main__")
