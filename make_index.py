#!/usr/bin/env python3

import os
import glob

def main():
    os.chdir('src')
    s = ''
    html = ''
    lis = []
    for md in glob.glob('*.md'):
        title_chunks = md[:-3].split('_')
        title = ' '.join(title_chunks).title()
        lis.append(f'<li><a href="{md[:-3]}.html">{title}</a></li>')
    for li in lis:
        html += f'<ul>{li}</ul>'
    f = open('index.md', 'w')
    f.writelines(html)
    f.close()

if __name__ == '__main__':
    main()