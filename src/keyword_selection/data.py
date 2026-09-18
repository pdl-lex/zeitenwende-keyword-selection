from pathlib import Path

import pandas as pd
import requests
from tqdm import tqdm

CORPUS_FILE = "CPP-BT_2026-01-17_DE_PQT_Reden_Gesamt.parquet"
CORPUS_URL = f"https://zenodo.org/records/18177196/files/{CORPUS_FILE}?download=1"
DATA_PATH = Path(__file__).parents[2].resolve() / "data"
CORPUS_PATH = DATA_PATH / CORPUS_FILE


def ensure_corpus() -> Path:
    """Check if the corpus is present in DATA_PATH and fetch if not."""
    if not CORPUS_PATH.exists():
        DATA_PATH.mkdir(parents=True, exist_ok=True)
        response = requests.get(CORPUS_URL, stream=True)
        response.raise_for_status()
        total_size = int(response.headers.get("content-length", 0))

        with (
            open(CORPUS_PATH, "wb") as f,
            tqdm(
                desc="Downloading corpus",
                total=total_size,
                unit="iB",
                unit_scale=True,
                unit_divisor=1024,
            ) as bar,
        ):
            for chunk in response.iter_content(chunk_size=1024 * 1024):
                size = f.write(chunk)
                bar.update(size)

    return CORPUS_PATH


def load_corpus() -> pd.DataFrame:
    path = ensure_corpus()

    return pd.read_parquet(path)
