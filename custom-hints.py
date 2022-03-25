#!/usr/bin/env python3
"""
kitty -o 'map f1 kitten hints --customize-processing custom-hints.py'
When you press the F1 key you will be able to select a word to look it up in the Google dictionary.
https://sw.kovidgoyal.net/kitty/kittens/hints/#completely-customizing-the-matching-and-actions-of-the-kitten
ref https://github.com/kovidgoyal/kitty/blob/master/kitty/boss.py
ref https://github.com/kovidgoyal/kitty/blob/master/kittens/hints/main.py
"""

import re
from kitty.utils import set_primary_selection
from kitty.fast_data_types import  set_clipboard_string

def mark(text, args, Mark, extra_cli_args, *a):
    # This function is responsible for finding all
    # matching text. extra_cli_args are any extra arguments
    # passed on the command line when invoking the kitten.
    # We mark all individual word for potential selection
    for idx, m in enumerate(re.finditer(r'\s?([a-zA-Z0-9_.-]+\.(ini|yml|yaml|vim|toml|conf|lua|go|php|rs|py|js|vue|jsx|html|htm|md|mp3|wav|flac|mp4|mkv|dll|exe|sh|txt|log|gz|tar|rar|7z|zip|mod|sum))\s?', text)):
        start, end = m.span()
        mark_text = text[start:end].replace('\n', '').replace('\0', '')
        # The empty dictionary below will be available as groupdicts
        # in handle_result() and can contain arbitrary data.
        yield Mark(idx, start, end, mark_text, {})


def handle_result(args, data, target_window_id, boss, extra_cli_args, *a):
    # This function is responsible for performing some
    # action on the selected text.
    # matches is a list of the selected entries and groupdicts contains
    # the arbitrary data associated with each entry in mark() above
    matches, groupdicts = [], []
    for m, g in zip(data['match'], data['groupdicts']):
        if m:
            matches.append(m), groupdicts.append(g)
    for word, match_data in zip(matches, groupdicts):
        # Lookup the word in a dictionary, the open_url function
        # will open the provided url in the system browser
        # boss.open_url(f'https://www.google.com/search?q=define:{word}')
        # set_primary_selection(word)
        set_clipboard_string(word)

