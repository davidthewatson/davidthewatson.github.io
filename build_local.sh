#!/usr/bin/env bash
 
while inotifywait -r -e close_write src/
do
    #staticjinja build --srcpath=src --outpath=docs
    ./make_index.py
    ./md2html.py
    cp -rf static/* docs/.
done
