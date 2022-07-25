#!/bin/bash

test -d .venv-model-builder && rm -rf .venv-model-builder
python3.10 -m venv .venv-model-builder

source .venv-model-builder/bin/activate

pip install -U pip setuptools wheel
pip install 'oarepo-model-builder>=1.0.0dev9' oarepo-vocabularies-model-builder

(
cd nr-vocabularies

# preserve the version
test -f nr_vocabularies/version.py && (
  mv nr_vocabularies/version.py >.version.tmp
)

rm -rf nr_vocabularies

oarepo-compile-model ../models/nr-vocabulary-model.yaml

cat .version.tmp >>nr_vocabularies/__init__.py
rm .version.tmp
)

cp -r models nr-vocabularies-model-builder/
pip install -e nr-vocabularies-model-builder

oarepo-compile-model --output-directory example models/example-model.yaml
