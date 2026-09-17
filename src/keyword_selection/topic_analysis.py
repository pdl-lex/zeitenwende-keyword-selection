from pathlib import Path

import requests
from tqdm import tqdm

CORPUS_URL = "https://zenodo.org/records/18177196/files/CPP-BT_2026-01-17_DE_PQT_Reden_Gesamt.parquet?download=1"
CORPUS_PATH = Path(__file__).parent.resolve() / "CPP-BT_2026-01-17_DE_PQT_Reden_Gesamt.parquet"


def ensure_corpus() -> Path:
    if not CORPUS_PATH.exists():
        response = requests.get(CORPUS_URL, stream=True)
        response.raise_for_status()
        total_size = int(response.headers.get("content-length", 0))

        with open(CORPUS_PATH, "wb") as f, tqdm(
            desc="Downloading corpus",
            total=total_size,
            unit="iB",
            unit_scale=True,
            unit_divisor=1024,
        ) as bar:
            for chunk in response.iter_content(chunk_size=1024 * 1024):
                size = f.write(chunk)
                bar.update(size)

    return CORPUS_PATH


ensure_corpus()