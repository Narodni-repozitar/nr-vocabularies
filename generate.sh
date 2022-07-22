#!/bin/bash

# preserve the version
cat nr_vocabularies/__init__.py | grep '__version__' >.version.tmp

rm -rf nr_vocabularies
source .venv-model-builder/bin/activate

oarepo-compile-model nr-vocabulary-model.yaml

cat .version.tmp >>nr_vocabularies/__init__.py
rm .version.tmp