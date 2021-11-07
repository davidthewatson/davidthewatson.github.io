#!/usr/bin/env python3

import os
import glob

def main():
    os.chdir('src')
    s = ''
    html = ''
    lis = []
    for md in glob.glob('[!index]*.md'):
        title_chunks = md[:-3].split('_') or md[:-3]
        print(title_chunks)
        title = ' '.join(title_chunks).title()
        print(title)
        lis.append(f'<li><a href="{md[:-3]}.html">{title}</a></li>')
    lis.sort()
    ul = ''.join(lis)
    html = f'<ul>{ul}</ul>'
    f = open('index.md', 'w')
    f.writelines(html)
    f.close()

if __name__ == '__main__':
    main()