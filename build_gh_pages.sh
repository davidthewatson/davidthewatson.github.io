#!/usr/bin/env bash
 
./make_index.py
./md2html.py
rm src/index.md
cp -rf static/* docs/.
mkdir -p docs/pdf
cd docs
httpwatcher &w
cd ..
sleep 5
wkhtmltopdf -B 2cm -L 2cm -R 2cm -T 2cm http://localhost:5555/resume/david_watson_resume.html docs/pdf/david_watson_resume.pdf
pkill httpwatcher
mkdir -p docs/txt
./md2txt.py
