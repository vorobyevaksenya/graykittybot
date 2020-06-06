#! /usr/bin/env bash

__FILE__="$(readlink -e "${BASH_SOURCE[0]}")"
__DIR__="$(dirname "${__FILE__}")"

env python3 "${__DIR__}/ourbot.py"
