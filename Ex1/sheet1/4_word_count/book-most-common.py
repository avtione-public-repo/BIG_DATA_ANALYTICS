#!/usr/bin/env python3
#!/bin/sh
import re
from collections import Counter


def most_common():
    words = re.findall(r'\w+', open('moby-dick.txt').read().lower())
    print(Counter(words).most_common(10))

if __name__ == "__main__":
    most_common()
