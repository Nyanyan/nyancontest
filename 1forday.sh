#!/bin/sh

python3 scramblegenerator.py
git add scramble.csv
git commit -m 'update scramble'
git push origin master
