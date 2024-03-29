# -*- coding: utf-8 -*-
# Copyright: Damien Elmes <anki@ichi2.net>
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html

import traceback, os, re
from anki.lang import _
from anki.importing.anki2 import Anki2Importer
from aqt.utils import showWarning

class Anki1Importer(Anki2Importer):

    dupeOnSchemaChange = True

    def run(self):
        from ..upgrade import Upgrader
        u = Upgrader()
        # check
        res = u.check(self.file)
        if res == "invalid":
            self.log.append(_(
                "File is invalid. Please restore from backup."))
            if (isinstance(u.cause, Exception)):
                raise u.cause
            raise Exception("invalidFile")
        # upgrade
        if res != "ok":
            self.log.append(
                "Problems fixed during upgrade:\n***\n%s\n***\n" % res)
        try:
            deck = u.upgrade()
        except:
            traceback.print_exc()
            self.log.append(traceback.format_exc())
            return
        # save the conf for later
        conf = deck.decks.confForDid(1)
        # merge
        deck.close()
        mdir = re.sub(r"\.anki2?$", ".media",  self.file)
        self.deckPrefix = re.sub(r"\.anki$", "", os.path.basename(self.file))
        self.file = deck.path
        Anki2Importer.run(self, mdir)
        # set imported deck to saved conf
        id = self.col.decks.confId(self.deckPrefix)
        conf['id'] = id
        conf['name'] = self.deckPrefix
        conf['usn'] = self.col.usn()
        self.col.decks.updateConf(conf)
        did = self.col.decks.id(self.deckPrefix)
        d = self.col.decks.get(did)
        self.col.decks.setConf(d, id)
        # While a qt action should NOT occur in a back-end importer;
        # it's far far simpler than to deal with a special case in front-end.
        # And anyway, the app should be restarted, so who cares.
        showWarning(_("""Please restart Anki when you are done importing ".anki" files. It is possible that using Anki without restarting may have unexpected results."""))