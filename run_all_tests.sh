#!/usr/bin/env bash
set -e

REQ_FILE="requirements.txt"
TEMP_DIR=$(mktemp --directory) 
echo Using directory: $TEMP_DIR

# Setup test environment
python3 -m venv $TEMP_DIR
source $TEMP_DIR/bin/activate
pip install -q -r $REQ_FILE

# Run all tests
python3 -m unittest discover -s tests/ -p '*_test.py'

# Exit test environment and remove temporary directory
deactivate
rm -rf $TEMP_DIR
