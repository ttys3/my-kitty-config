#!/usr/bin/env python3
"""
this tool is used to convert Kitty session dump to Kitty session file which can be loaded by Kitty
"""

import json
import os
import sys


def env_to_str(env):
    """Convert an env list to a series of '--env key=value' parameters and return as a string."""
    s = ""
    for key in env:
        s += f"--env {key}={env[key]} "

    return s.strip()


def cmdline_to_str(cmdline):
    """Convert a cmdline list to a space separated string."""
    s = ""
    for e in cmdline:
        s += f"{e} "

    return s.strip()


def fg_proc_to_str(fg):
    """Convert a foreground_processes list to a space separated string."""
    s = ""
    fg = fg[0]

    # s += f"--cwd {fg['cwd']} {cmdline_to_str(fg['cmdline'])}"
    s += f"{cmdline_to_str(fg['cmdline'])}"

    if s == "kitty @ ls":
        return os.getenv("SHELL")
    return s


def convert(session):
    """Convert a kitty session dict, into a kitty session file and output it."""
    first = True
    for os_window in session:
        if first:
            first = False
        else:
            print("\nnew_os_window\n")

        for tab in os_window["tabs"]:
            print("\n")
            print(f"new_tab {tab['title']}")
            # print('enabled_layouts *)
            print(f"layout {tab['layout']}")
            # This is a bit of a kludge to set cwd for the tab, as
            # setting it in the launch command didn't work, for some reason?
            if tab["windows"]:
                print(f"cd {tab['windows'][0]['cwd']}")

            for w in tab["windows"]:
                # print(f"title {w['title']}")
                # skip dump "/usr/bin/kitty +hold command"
                if os.path.basename(w['foreground_processes'][0]['cmdline'][0]) == "kitty":
                    continue
                print(f"launch {env_to_str(w['env'])} {fg_proc_to_str(w['foreground_processes'])}")
                if w["is_focused"]:
                    print("focus")


if __name__ == "__main__":
    stdin = sys.stdin.readlines()
    session = json.loads("".join(stdin))
    convert(session)
