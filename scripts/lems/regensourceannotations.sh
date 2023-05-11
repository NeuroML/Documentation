#!/bin/bash

# Copyright 2023 NeuroML contributors
# File :  scripts/lems/regensourceannotations.sh
#
# Regenerate sourceannotations.xml, and then generate ast.
#

echo "Regenerating sourceannotations.xml"

curdir=$(pwd)
tempdir=$(mktemp --directory)
pushd ${tempdir}

git clone --branch development https://github.com/LEMS/LEMS.git --single-branch --depth 4
git clone --branch development https://github.com/LEMS/jLEMS.git --single-branch --depth 4

pushd jLEMS
mvn install
popd

pushd LEMS/docgeneration
ant -p
ant
ls -alt html
popd

popd

cp "${tempdir}/LEMS/docgeneration/extractedannotations/sourceannotations.xml" . -v

echo "Regenerating AST sources"
python3 ./xml2md.py
