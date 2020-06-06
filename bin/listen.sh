#! /usr/bin/env bash

__FILE__="$(readlink -e "${BASH_SOURCE[0]}")"
__DIR__="$(dirname "${__FILE__}")"

APP_ROOT="$(dirname "${__DIR__}")"

env python "${APP_ROOT}/ourbot.py"
