#!/bin/bash

LD_LIBRARY_PATH="$(pwd)/lib/raspberry:$(pwd)/lib/x86-64/"

echo "Please ensure you have run ./canableStart.sh or ./vcanEnable.sh before running this"

./builddir/ecvt
