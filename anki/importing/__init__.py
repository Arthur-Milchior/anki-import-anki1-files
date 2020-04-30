from anki import importing
from .anki1 import Anki1Importer
from anki.lang import _

importers = list(importing.Importers)
importers.append((_("Anki 1.2 Deck (*.anki)"), Anki1Importer))
importing.Importers = tuple(importers)

