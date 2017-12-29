#!/usr/bin/env python3
#!/bin/sh

import re
import sys
import matplotlib.pyplot as plt
from collections import defaultdict, Counter


word = sys.argv[1].lower()


def read_book():
    """ reads the book and creates a map with chapter num -> content. Chapter 0 is everything before the occourence of "CHAPTER 1" """
    chapters = defaultdict(lambda: "")
    with open('moby-dick.txt') as b:
        chapter = 0
        for line in b:
            if(re.match(r'CHAPTER \d*\..*', line)):
                chapter += 1
            chapters[chapter] = chapters[chapter] + line
    return chapters


def word_freq():
    book = read_book()
    freq = []
    for chapter, content in book.items():
        words = re.findall(r'\w+', content.lower())
        freq.append(Counter(words)[word] / len(words))

    plt.bar(range(len(freq)), freq, 1)
    plt.ylabel("relative occurrence")
    plt.xlabel("chapter")
    plt.show()


if __name__ == "__main__":
    word_freq()
