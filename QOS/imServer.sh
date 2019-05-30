#!/usr/bin/env bash

port_num=${1+x}||8000

python -m SimpleHTTPServer $port_num
