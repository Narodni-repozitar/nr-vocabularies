#!/bin/bash

set -e

cp nr-vocabularies/nr_vocabularies/version.py nr-vocabularies-model-builder/nr_vocabularies_model_builder/

cp nr-vocabulary-model.yaml nr-vocabularies-model-builder/nr_vocabularies_model_builder/

test -d dist && rm -rf dist

mkdir dist

export VERSION="__version__=\"$(git describe --tags --abbrev=0)\""

# create library distribution
(
  cd nr-vocabularies
  echo $VERSION > version.py
  test -d dist && rm -rf dist
  cp ../README.rst .
  cat setup.cfg
  python setup.py sdist bdist_wheel
  cp dist/*.tar.gz  ../dist/
  cp dist/*.whl  ../dist/
)

# create model builder extension package
(
  cd nr-vocabularies-model-builder
  echo $VERSION > version.py
  test -d dist && rm -rf dist
  cp ../README.rst .
  cat setup.cfg
  python setup.py sdist bdist_wheel
  cp dist/*.tar.gz  ../dist/
  cp dist/*.whl  ../dist/
)

# build example
(
  cd example
  test -d dist && rm -rf dist
  cp ../README.rst .
  cat setup.cfg
  python setup.py sdist bdist_wheel
)

# just list created stuff
ls -la dist

for i in dist/*.tar.gz; do
  echo
  echo Listing $i
  tar -tf $i
done

