#!/bin/bash

pip install -U pip setuptools wheel

set -e

cp -r models nr-vocabularies-model-builder/nr_vocabularies_model_builder/

test -d dist && rm -rf dist

mkdir dist

export VERSION="$(git describe --tags --abbrev=0)"

if [ "a$VERSION" = "a" ] ; then
    echo "No version yet, setting it to 0.0.1"
    VERSION="0.0.1"
fi

export VERSION="__version__=\"$VERSION\""
echo "version will be: $VERSION"

# create library distribution
(
  cd nr-vocabularies
  echo "$VERSION" > nr_vocabularies/version.py
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
  echo "$VERSION" > nr_vocabularies_model_builder/version.py
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

