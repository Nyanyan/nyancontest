#!/bin/sh

cd /home/pi/nyancontest
python3 getresult.py
git add clock
git commit -m 'upodated data'
git push origin master
