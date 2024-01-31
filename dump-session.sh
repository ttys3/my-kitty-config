#!/usr/bin/env bash

set -eou pipefail

#kitty @ ls | ./kitty-convert-dump.py > session.conf

kitty @ ls |  $HOME/.config/kitty/kitty-convert-dump.py > $HOME/.config/kitty/session.conf

echo "kitty session dumped"

echo; read -r -p "Press Enter to exit"; echo ""



