#!/bin/bash

set -e

OAREPO_VERSION="${OAREPO_VERSION:-12}"
export PIP_EXTRA_INDEX_URL=https://gitlab.cesnet.cz/api/v4/projects/1408/packages/pypi/simple
export UV_EXTRA_INDEX_URL=https://gitlab.cesnet.cz/api/v4/projects/1408/packages/pypi/simple

VENV=".venv"

if test -d $VENV ; then
  rm -rf $VENV
fi

python3 -m venv $VENV
. $VENV/bin/activate
pip install -U setuptools pip wheel

echo "Installing oarepo version $OAREPO_VERSION"
pip install pytest-invenio==2.*
pip install "oarepo[tests,rdm]==${OAREPO_VERSION}.*"
pip install -e ".[tests]"

pip uninstall -y uritemplate
pip install uritemplate

invenio index destroy --force --yes-i-know || true

pytest tests
