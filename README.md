# Zeitenwende im Wortfeld: Zielwort-Extraktion

## Übersicht

Topic-Analyse zur empirischen Selektion von Zielwörtern für die Untersuchung von semantischem
Wandel im Zusammenhang mit dem Ukraine-Konflikt.

Strategie: Mittels [BERTopic][1] werden Themenkomplexe aus Redebeiträgen aus dem
[Corpus der Plenarprotokolle des Deutschen Bundestages (CPP-BT)][2] im Zeitraum 2013 bis 2025
extrahiert. Die Sichtung der Themen-Labels zeigt ein ausgeprägtes Topic mit Beginn um den russischen
Einmarsch in die Ukraine im Jahr 2022.

Aus diesem sowie den 10 semantisch ähnlichsten Topics werden anschließend die jeweils 50 wichtigsten
Wörter als Kandidaten herangezogen. Das Ergebnis ist eine Liste von knapp 800 Zielwörtern als Basis
für die Untersuchung diachronen Wandels.

## Installation

### Mit `uv` (empfohlen, schneller)

```bash
uv sync
```

### Alternativ mit `pip`

```bash
python -m venv .venv

source .venv/bin/activate  # Unter Windows: .venv\Scripts\activate

pip install -e .
```

## Ausführung

```bash
uv run python -m keyword_selection
```

[1]: https://maartengr.github.io/BERTopic/index.html
[2]: https://zenodo.org/records/18177196
