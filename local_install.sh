#!/bin/bash

cd $(dirname $0)

source .venv/bin/activate

(
  cd nr-vocabularies
  pip install -e '.[tests,elasticsearch7,postgresql]'
)
