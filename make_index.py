#!/usr/bin/env python3

import glob
import os

def main():
    os.chdir('src')
    s = ''
    html = ''
    lis = []
    for md in glob.glob('*.md'):
        lis.append(f'<li><a href="{md[:-3]}.html">{md}</a></li>')
    for li in lis:
        html += f'<ul>{li}</ul>'
    f = open('index.md', 'w')
    f.writelines(html)
    f.close()
if __name__ == '__main__':
    main()