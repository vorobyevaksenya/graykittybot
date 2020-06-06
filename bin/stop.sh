#! /usr/bin/env bash

__FILE__="$(readlink -e "${BASH_SOURCE[0]}")"
__DIR__="$(dirname "${__FILE__}")"

screen -S graykittybot -X quit
