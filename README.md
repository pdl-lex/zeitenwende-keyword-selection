# Zeitenwende im Wortfeld: Zielwort-Extraktion

Topic-Analyse zur empirischen Selektion von Zielwörtern für die Untersuchung von semantischem
Wandel im Zusammenhang mit dem Ukraine-Konflikt.

## Vorgehen

Mittels [BERTopic][1] werden Topics aus Redebeiträgen aus dem
[Corpus der Plenarprotokolle des Deutschen Bundestages (CPP-BT)][2] im Zeitraum 2014 bis 2025
extrahiert. Dabei zeigt sich der Ukraine-Konflikt als ein ausgeprägtes Topic. Aus diesem sowie
weiteren, semantisch ähnlichen Topics werden anschließend die jeweils wichtigsten Begriffe je Topic
als Ausgangsbasis für eine kuratierte Liste von Zielwörtern als Basis für die Untersuchung
diachronen Wandels zusammengestellt.

## Quickstart

Zum Ausführen wird [uv][3] benötigt.

```bash
uv sync
uv run python -m jupyter notebook ./notebooks
```

Im Browser (oder alternativ direkt in VS Code o.ä.) zunächst die Vorverarbeitung und das
Training von BERTopic ([01_model_training.ipynb](./notebooks/01_model_training.ipynb)) und
anschließend die Keyword-Extraktion
([02_target_word_extraction.ipynb](./notebooks/02_target_word_extraction.ipynb)) durchführen.
Weitere Details sind in den jeweiligen Notebooks dokumentiert.

[1]: https://maartengr.github.io/BERTopic/index.html
[2]: https://zenodo.org/records/18177196
[3]: https://docs.astral.sh/uv/
