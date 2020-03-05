#!/bin/sh

cd /home/pi/nyancontest
python3 scramblegenerator.py
git add scramble.csv
git commit -m 'update scramble'
python3 deletedata.py
git add Clock/data.csv
git add Clock/data_yesterday.csv
git add Mirror3x3/data.csv
git add Mirror3x3/data_yesterday.csv
git commit -m 'updated data'
python3 dateupdate.py
git add date.txt
git commit -m 'updated date'
git push origin master
