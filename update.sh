#!/bin/sh
rm -rf COVID-19
git clone https://github.com/CSSEGISandData/COVID-19.git
rm -rf imgsrc
mkdir imgsrc
python3 coronavirus.py
git add -A;
git commit -m "Message";
git push