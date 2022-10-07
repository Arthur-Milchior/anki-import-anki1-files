from aqt import importing
import os
import anki.importing as importing
from aqt.utils import getFile, showWarning
from aqt.importing import *
from anki.lang import _

def onImport(mw):
    extensions = [x[0] for x in importing.importers(mw.col)]
    if ".anki" not in extensions:
        extensions.append(".anki")
    filt = ";;".join(extensions)
    file = getFile(mw, _("Import"), None, key="import", filter=filt)
    if not file:
        return
    file = str(file)

    head, ext = os.path.splitext(file)
    ext = ext.lower()
    if ext == ".anki":
        from ..anki import importing as i
        # this ensure Anki1Importer get added; the content of the module is not used
    if ext == ".anki2":
        showInfo(
            _(
                ".anki2 files are not directly importable - please import the .apkg or .zip file you have received instead."
            )
        )
        return

    importFile(mw, file)
    if ext == ".anki":
        showWarning(_("""Please restart anki when you are done importing ".anki" files. It
is possible that using anki without restarting may have unexpected
result."""))
    
aqt.importing.onImport = onImport
