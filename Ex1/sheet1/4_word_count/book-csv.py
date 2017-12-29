#!/usr/bin/env python3
#!/bin/sh
import re
import json
from collections import Counter, OrderedDict


def read_book():
    """ reads the book and creates a map with chapter num -> content. Chapter 0 is everything before the occourence of "CHAPTER 1" """
    chapters = OrderedDict()
    with open('moby-dick.txt') as b:
        chapter = 'Prolog'
        for line in b:
            if(re.match(r'CHAPTER \d*\..*', line)):
                chapter = re.sub(r'CHAPTER \d*\. ', '', line).replace('\n', '')
            append_line(chapters, chapter, line)
    return chapters


def append_line(chapters, chapter, line):
    if chapter in chapters:
        chapters[chapter] = chapters[chapter] + line
    else:
        chapters[chapter] = line


def aggregation():
    """creates a book.csv. the chapter length is given in words"""
    book = read_book()
    with open('aggregation.csv', 'w') as out:
        out.write('chapter-name,chapter-length,word-occurences')
        for k, content in book.items():
            words = re.findall(r'\w+', content.lower())
            counted = Counter(words)
            out.write('%s, % d, %s\n' % (k, len(words), str(json.dumps(dict(counted)))))
        out.close()


aggregation()
