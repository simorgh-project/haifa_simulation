#!/usr/bin/env bash

# get current file directory
DIR="$(realpath $( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd ))"
cd $DIR
source $DIR/include.sh

print_help() {
    echo "{ help under construction }"
}

REQUIRED_ARGS=1

# print help and exit if not enough args given
[[ $# -ge ${REQUIRED_ARGS} ]] || {
    print_help
    exit 1
}

# parse args
NAME="$1"

# ===================================================== #

SCP "$DIR/scripts" "$NAME:"

SSH $NAME "scripts/run-malish.sh"

