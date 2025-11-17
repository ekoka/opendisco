#! /usr/bin/env bash

set -e
set -x

# Create db tables
python app/scripts/createdb.py

## Run migrations
#alembic upgrade head
#
## Create initial data in DB
#python app/initial_data.py
