#!/bin/bash

./scripts/version_patch.py
git add .
git commit -m `cat version.txt`
