#!/bin/bash

SLIDES="0_Introduction 1_Project 2_Distribution 3_Test 4_Documentation"
BUILD_DIR="build"

pushd $( dirname $0 )

mkdir -p ${BUILD_DIR}

for DIR in ${SLIDES}; do
    pushd "${DIR}"
    echo "Build ${DIR}"
    landslide --embed --destination=../${BUILD_DIR}/${DIR}.html index.rst
    popd
done

# Extra files
cp 3_Test/parametric_testcase.py ${BUILD_DIR}/

popd
