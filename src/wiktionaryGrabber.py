# -*- coding: utf-8 -*-

# WiktionaryGrabber add-on for Anki
#
# Copyright (C) 2015  Maira Carvalho
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Entry point for WiktionaryGrabber add-on from Anki


"""
from __future__ import print_function
import sys
def warning(*objs):
    print("WARNING: ", *objs, file=sys.stderr)

__all__ = []


if __name__ == "__main__":
    warning(
        "WiktionaryGrabber is an add-on for Anki.\n"
        "It is not intended to be run directly.\n"
        "To learn more or download Anki, please visit <http://ankisrs.net>.\n"
    )
    exit(1)

import os
from anki.hooks import addHook
from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QIcon, QAction
from anki.hooks import wrap
from aqt.editor import Editor
from anki.utils import json
from aqt import mw
from aqt.utils import showInfo
from aqt import browser

# import wiktionarygrabber module with the actual code
import wiktionarygrabber

def wiktionaryGrabber(self):
    """ Utility function that fetches info from Wiktionary to add to the notes."""
    ipa_field = 'IPA'
    plural_field = "Plural"
    gender_field = "Gender"
    self.saveNow();
    self.mw.checkpoint(_("Get info from wiktionary on the current note"))

    if not 'Dutch' in mw.col.models.fieldNames(self.note.model()):
        warning('This add-on requires a field called "Dutch" (mind the capitalization) to work.')
    else:
        entry = self.note['Dutch']
    
        #Call the grabber method
        myWord = wiktionarygrabber.get_wiktionary_fields(entry, "Dutch")
    
        if myWord:
            for name in mw.col.models.fieldNames(self.note.model()):
                if name==ipa_field:
                    self.note[ipa_field] = myWord.ipa
                if name==plural_field:
                    self.note[plural_field] = myWord.plural
                if name==gender_field:
                    self.note[gender_field] = myWord.gender
                    
            self.stealFocus = True;
            self.saveNow();
            self.loadNote();
        else:
            warning("Failed to find word '%s' in Dutch. Please check if Wiktionary has it: %s" % (entry, "https://en.wiktionary.org/wiki/"+entry))

def setupButtons(self):
    """ Adds word wrap keyboard shortcut and button to the note editor. """
    icons_dir = os.path.join(mw.pm.addonFolder(), 'wiktionarygrabber', 'icons')
    b = self._addButton("wiktionaryButton", lambda s=self: wiktionaryGrabber(self),
            text=" ", tip="Add fields with Wiktionary data")
    b.setIcon(QIcon(os.path.join(icons_dir, 'wiktionary.png')))
    
Editor.setupButtons = wrap(Editor.setupButtons, setupButtons)