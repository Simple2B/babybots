#!/usr/bin/env bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd $SCRIPT_DIR
source .venv/bin/activate
echo `date` >> run-script.log
flask launch-script 2>> run-script.err >> run-script.out
