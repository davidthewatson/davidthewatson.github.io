#!/usr/bin/env bash
 
while inotifywait -r -e close_write src/
do
    staticjinja build --srcpath=src --outpath=docs
    cp -rf static/* docs/.
    mkdir -p docs/pdf
    wkhtmltopdf -B 2cm -L 2cm -R 2cm -T 2cm http://localhost:5555/resume/david_watson_resume.html docs/pdf/david_watson_resume.pdf
    mkdir -p docs/txt
    html2text docs/resume/david_watson_resume.html >docs/txt/david_watson_resume.md
    python ./md2txt.py
done
