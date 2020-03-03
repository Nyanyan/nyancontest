#!/bin/sh

cd /home/pi/nyancontest
python3 scramblegenerator.py
git add scramble.csv
git commit -m 'update scramble'
python3 deletedata.py
git add clock/data.csv
git commit -m 'deleted data'
git push origin master
