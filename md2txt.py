
#!/usr/bin/env python3

# Convert markdown to plain text from https://stackoverflow.com/a/54923798

from markdown import Markdown
from io import StringIO


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
    md_file = open('docs/txt/david_watson_resume.md')
    txt = md_file.read()
    plain_txt = unmark(txt)
    n = open('docs/txt/david_watson_resume.txt', 'w')
    n.write(plain_txt)

if __name__ == '__main__':
    main()
    