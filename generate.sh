#!/bin/bash

set -e

deactivate || true

test -d .venv-model-builder && rm -rf .venv-model-builder
python3.10 -m venv .venv-model-builder

source .venv-model-builder/bin/activate

pip install -U pip setuptools wheel
pip install 'oarepo-model-builder>=1.0.0dev9' 'oarepo-vocabularies-model-builder>=0.0.5'

(
  cd nr-vocabularies
  rm -rf nr_vocabularies
  oarepo-compile-model ../models/nr-vocabularies.yaml
)

cp -r models nr-vocabularies-model-builder/
pip install -e nr-vocabularies-model-builder

(
  cd example
  test -d example && rm -rf example
  oarepo-compile-model ../tests/example-model.yaml
)
