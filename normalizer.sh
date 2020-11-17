#!/bin/bash
if [ $# -ne 1 ] ; then
  echo "usage: normalizer.sh filename > outputFilename"
  exit 1
fi
filename=$1
python3 normalizer.py "$filename"
