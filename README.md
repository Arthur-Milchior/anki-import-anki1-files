# Import .anki files
## Rationale

A long time ago, there was Anki 1. It used a file format called ".anki". Very
different from today's Anki2's ".anki2" format. You can still find on
the web some old decks, shared a decade ago, in this format. This
add-on allow to import them.

## Warning
You should probably deactivate this add-on when you don't use it. It
essentially install a copy of anki 2.0 which itself install a copy of
anki 1.0; that's not things you want to use everyday. I can't
guarantee there won't be any interference (especially in hooks)

## Internal
In
https://github.com/ankitects/anki/commit/1dce3eaaff649e2c1dbfd53bfe289cf42971045e#diff-c60e37732e601ec3d7f7e7146624b3a1
, the code for importing anki was removed. I checked out this branch
and essentially put all the relevant code (and probably a lot of
irelevant code too) in this add-on.

I thus of course had to import all code removed in the
above-mentionned commit. In particular it contained `oldanki` which I
believe to be anki 1's code. It contained anki2.0 importer for anki 1,
and "upgrade" which transform Anki 1 into anki 2 format.

I then realized that most of this code could actually not use todays
collection; so I had to copy the old version of the collection file,
and then media, models, decks... so that everything gets
compatible. (To be precise, current collection uses a weakref; when a
manager want to access it, it does not found it in the old collection,
and raised an exception. Thus I had to copy all old managers.)

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
