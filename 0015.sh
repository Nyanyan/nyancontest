#!/bin/sh

cd /home/pi/nyancontest
python3 updatecontents.py
python3 makeallhtml.py
git add .
git commit -m 'start contest'
git push origin master

