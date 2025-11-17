#! /usr/bin/env bash

set -e
set -x

# drop db tables
python ./app/scripts/dropdb.py

