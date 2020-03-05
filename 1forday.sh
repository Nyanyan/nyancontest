#!/bin/sh

cd /home/pi/nyancontest
python3 scramblegenerator.py
git add scramble.csv
git commit -m 'update scramble'
python3 deletedata.py
git add clock/data.csv
git add clock/data_yesterday.csv
git commit -m 'updated data'
python3 dateupdate.py
git add date.txt
git commit -m 'updated date'
git push origin master
