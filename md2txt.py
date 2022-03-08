#!/usr/bin/env python3

# Convert markdown to plain text from https://stackoverflow.com/a/54923798

from markdown import Markdown
from io import StringIO
import glob
import html


def unmark_element(element, stream=None):
    if stream is None:
        stream = StringIO()
    if element.text:
        stream.write(element.text)
    for sub in element:
        unmark_element(sub, stream)
    if element.tail:
        stream.write(element.tail)
    return stream.getvalue()


# patch markdown module
Markdown.output_formats["plain"] = unmark_element
__md = Markdown(output_format="plain")
__md.stripTopLevelTags = False


def unmark(text):
    return __md.convert(text)


def main():
    print('Rendering plain text')
    for md in glob.glob('src/**/**[!404]*.md', recursive=True):

        print(md)
        f = open(md, 'r')
        txt = f.read()
        # massive hack; must remove
        if "david_watson_resume.md" in md:
            print(md)
            txt = txt[700:]
            txt = f'david@davidwatson.org\n{txt}'
        txt_with_html = unmark(txt)
        txt_without_entities = html.unescape(txt_with_html)
        new_name = md.replace('src', 'docs')
        new_name = new_name.replace('md', 'txt')
        print(new_name)
        n = open(new_name, 'w')
        n.write(txt_without_entities)

if __name__ == '__main__':
    main()
