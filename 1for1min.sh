#!/bin/sh

cd /home/pi/nyancontest
python3 getresult.py
git add .
git commit -m 'updated data'
python3 makeallhtml.py
git add .
git commit -m 'modified html'
git push origin master
