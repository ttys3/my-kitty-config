#!/usr/bin/env bash

set -eou pipefail

kitty @ ls | ./kitty-convert-dump.py > session.conf


