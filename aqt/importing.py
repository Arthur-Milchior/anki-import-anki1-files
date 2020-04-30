from aqt import importing
import os
import anki.importing as importing
from aqt.utils import getFile
from aqt.importing import *
from anki.lang import _

def onImport(mw):
    filt = ";;".join([x[0] for x in importing.Importers])
    file = getFile(mw, _("Import"), None, key="import", filter=filt)
    if not file:
        return
    file = str(file)

    head, ext = os.path.splitext(file)
    ext = ext.lower()
    if ext == ".anki2":
        showInfo(
            _(
                ".anki2 files are not directly importable - please import the .apkg or .zip file you have received instead."
            )
        )
        return

    importFile(mw, file)
aqt.importing.onImport = onImport
