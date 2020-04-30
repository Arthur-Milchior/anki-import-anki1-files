# Import .anki files
## Rationale

A long time ago, there was Anki 1. It used a file format called ".anki". Very
different from today's Anki2's ".anki2" format. You can still find on
the web some old decks, shared a decade ago, in this format. This
add-on allow to import them.

## Warning
You should probably restart anki once you're done importing
data. Importing .anki data essentially starts a copy of anki 2.0 which
itself starts a copy of anki 1.0; that's not things you want to keep
running and potentially interfering with your normal study. I can't
guarantee there won't be any interference (especially in hooks)

## Internal
The only new code is in `aqt/importing.py`, where I change the
"onImport" function in order to deal with ".anki" file. If importing
such a file is requested, it will import `anki/importing/__init__.py`,
which itself will add all the required codebase. It essentially is a
copy of the backend code and anki1 code, as it was before this feature
was removed in all
https://github.com/ankitects/anki/commit/1dce3eaaff649e2c1dbfd53bfe289cf42971045e#diff-c60e37732e601ec3d7f7e7146624b3a1
.

## Technical

My best guess is that anki 1 was in python 2. Dropping the importer
ensured that the code didn't have to be porter to python 3. I'm not
certain, because tools exists to do the port.

Anyway, to get code from anki 1, anki 2.0 did used anki1 code to
compute all cards. It actually simply opened this file as a collection
and then used the function which ports collection from 1 to 2.0. I
believe that there was no difference between decks and collection in
anki 1; which might explain why it used anki 2.0 can import a deck and
consider it as a collection.

## TODO

Remove all part of the code not actually useful for anki

## Links, licence and credits

Key         |Value
------------|-------------------------------------------------------------------
Copyright   | Arthur Milchior <arthur@milchior.fr>
Based on    | Anki code by Damien Elmes <anki@ichi2.net>
License     | GNU GPL, version 3 or later; http://www.gnu.org/licenses/gpl.html
Source in   | https://github.com/Arthur-Milchior/anki-import-anki1-files
Addon number| [175027074](https://ankiweb.net/shared/info/175027074)
