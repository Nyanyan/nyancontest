#!/bin/sh

python3 scramblegenerator.py
python3 deletedata.py
git add scramble.csv
git commit -m 'update scramble'
git add clock/data.csv
git commit -m 'deleted data'
git push origin master
