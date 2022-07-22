#!/bin/bash

test -d .venv-model-builder && rm -rf .venv-model-builder
python3.10 -m venv .venv-model-builder

source .venv-model-builder/bin/activate

pip install -U pip setuptools wheel
pip install 'oarepo-model-builder>=1.0.0dev9' oarepo-vocabularies-model-builder

# preserve the version
test -f nr_vocabularies/__init__.py && (
  cat nr_vocabularies/__init__.py | grep '__version__' >.version.tmp
)

rm -rf nr_vocabularies

oarepo-compile-model nr-vocabulary-model.yaml

cat .version.tmp >>nr_vocabularies/__init__.py
rm .version.tmp