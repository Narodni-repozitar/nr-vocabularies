#!/bin/bash

set -e

cd "$(dirname $0)"

# prepare virtualenv

MB_VENV=.venv-model-builder
MB_BIN=${MB_VENV}/bin
MB_PIP=${MB_BIN}/pip

if [ ! -d ${MB_VENV} ] ; then
  python3.10 -m venv ${MB_VENV}

  ${MB_PIP} install -U pip
  ${MB_PIP} install -U setuptools wheel

  # install model builder main package
  ${MB_PIP} install 'oarepo-model-builder>=1.0.0dev29'

  # install required plugins
  
fi

${MB_BIN}/oarepo-compile-model -vvv model_app.yaml --output-directory nr-vocabularies
 # --save-model model_included.yaml

cp nr-vocabularies/nr_vocabularies/models/inherited_model.json \
   nr-vocabularies-model-builder/nr_vocabularies_model_builder/models/model.json
