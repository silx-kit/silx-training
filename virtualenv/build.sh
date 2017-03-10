#!/bin/bash

BUILD_DIR="build"


mkdir -p ${BUILD_DIR}

landslide --embed --destination=${BUILD_DIR}/venv.html index.rst

