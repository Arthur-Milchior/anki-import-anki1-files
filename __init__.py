import sys
import pathlib
path = f"{pathlib.Path(__file__).parent.absolute()}/"
sys.path.append(path)
from anki import hooks
from .anki.importing.anki1 import Anki1Importer
from anki.importing.base import Importer

def add_anki1_importer(importers: list[tuple[str, type[Importer]]]):
    importers.append(("Anki 1.2 Deck (*.anki)", Anki1Importer))

hooks.importing_importers.append(add_anki1_importer)