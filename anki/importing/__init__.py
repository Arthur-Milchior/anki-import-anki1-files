from anki import importing
from .anki1 import Anki1Importer

old_importers = importing.importers

def importers(col):
    importers = list(old_importers(col))
    importers.append(("Anki 1.2 Deck (*.anki)", Anki1Importer))
    return tuple(importers)

importing.importers = importers

