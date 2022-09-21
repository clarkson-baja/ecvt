#!/bin/bash

set -e

if [ ! -d ./builddir ]; then
    meson builddir
fi

ninja -C ./builddir

# g++ example.cpp -Iinclude -Llib/raspberry -l:libCTRE_Phoenix.so -l:libCTRE_PhoenixCCI.so
