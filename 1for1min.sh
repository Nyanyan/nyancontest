#!/bin/sh

cd /home/pi/nyancontest
python3 getresult.py
git add Clock/data.csv
git add Mirror3x3/data.csv
git commit -m 'upodated data'
python3 makeallhtml.py
git add Clock/index.html
git add Mirror3x3/index.html
git commit -m 'modified html'
git push origin master
