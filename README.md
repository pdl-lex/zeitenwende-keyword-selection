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

## Quickstart

Zum Ausführen wird [uv][3] benötigt.

```bash
uv sync
uv run python -m jupyter notebook ./notebooks
```

Im Browser (oder alternativ direkt in VS Code o.a. IDEs) zunächst die Vorverarbeitung und das
Training von BERTopic ([01_model_training.ipynb](./notebooks/01_model_training.ipynb)) und
anschließend die Keyword-Extraktion
([02_target_word_extraction.ipynb](./notebooks/02_target_word_extraction.ipynb)) durchführen.
Weitere Details sind in den Notebooks dokumentiert.

[1]: https://maartengr.github.io/BERTopic/index.html
[2]: https://zenodo.org/records/18177196
[3]: https://docs.astral.sh/uv/
