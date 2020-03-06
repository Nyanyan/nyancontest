#!/bin/sh

cd /home/pi/nyancontest
python3 sleeping.py
git add .
git commit -m 'sleep'
git push origin master
