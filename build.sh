#!/usr/bin/env bash
 
while inotifywait -r -e close_write src/
do
    #staticjinja build --srcpath=src --outpath=docs
    ./md2html.py
    cp -rf static/* docs/.
    mkdir -p docs/pdf
    wkhtmltopdf -B 2cm -L 2cm -R 2cm -T 2cm http://localhost:5555/resume/david_watson_resume.html docs/pdf/david_watson_resume.pdf
    mkdir -p docs/txt
    python ./md2txt.py
done
