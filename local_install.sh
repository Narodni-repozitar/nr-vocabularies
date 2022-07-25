#!/bin/bash

cd $(dirname $0)

source .venv/bin/activate

(
  cd oarepo-vocabularies
  pip install -e '.[tests,elasticsearch7,postgresql]'
)

(
  cd oarepo-vocabularies-basic
  pip install -e .
)

