#!/bin/bash

g++ example.cpp -Iinclude -Llib/raspberry -l:libCTRE_Phoenix.so -l:libCTRE_PhoenixCCI.so
