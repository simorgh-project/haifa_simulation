#!/usr/bin/env bash

# get current file directory
DIR="$(realpath $( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd ))"
cd $DIR

# parse input port
port_num=8000
[[ -z ${1+x} ]] || port_num="$1"

cd $DIR/web
python -m SimpleHTTPServer ${port_num}
