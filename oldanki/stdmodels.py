# -*- coding: utf-8 -*-
# Copyright: Damien Elmes <oldanki@ichi2.net>
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html

"""\
Standard Models.
==============================================================

Plugins can add to the 'models' dict to provide more standard
models.
"""

from oldanki.models import Model, CardModel, FieldModel
from oldanki.lang import _

models = {}

def byName(name):
    fn = models.get(name)
    if fn:
        return fn()
    raise ValueError("No such model available!")

def names():
    return list(models.keys())

# Basic
##########################################################################

def BasicModel():
    m = Model(_('Basic'))
    m.addFieldModel(FieldModel('Front', True, True))
    m.addFieldModel(FieldModel('Back', False, False))
    m.addCardModel(CardModel('Forward', '%(Front)s', '%(Back)s'))
    m.addCardModel(CardModel('Reverse', '%(Back)s', '%(Front)s',
                             active=False))
    m.tags = "Basic"
    return m

models['Basic'] = BasicModel

# Recovery
##########################################################################

def RecoveryModel():
    m = Model(_('Recovery'))
    m.addFieldModel(FieldModel('Question', False, False))
    m.addFieldModel(FieldModel('Answer', False, False))
    m.addCardModel(CardModel('Single', '{{{Question}}}', '{{{Answer}}}'))
    m.tags = "Recovery"
    return m
