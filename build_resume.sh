#!/usr/bin/env bash
 
while inotifywait -r -e close_write resume/
do
    mkdir -p docs/pdf
    python ./render_resume.py
    wkhtmltopdf -B 2cm -L 2cm -R 2cm -T 0.5cm http://localhost:8000/resume/david_watson_resume.html docs/pdf/david_watson_resume.pdf
    mkdir -p docs/txt
    python ./md2txt.py
    cp -rf static/* docs/.
done

