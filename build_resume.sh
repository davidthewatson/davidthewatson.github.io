#!/usr/bin/env bash
 
while inotifywait -r -e close_write resume/
do
    mkdir -p docs/pdf
    python ./render_resume.py
    wkhtmltopdf -B 1.5cm -L 1.5cm -R 1.5cm -T 1.5cm http://localhost:8000/resume/david_watson_resume.html docs/pdf/david_watson_resume.pdf
    mkdir -p docs/txt
    python ./md2txt.py
    cp -rf static/* docs/.
done

