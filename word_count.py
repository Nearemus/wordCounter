#!usr/bin/python

import sys

def count_words(data):
    words = data.split(" ")
    num_words = len(words)
    return num_words

def count_lines(data):
    lines = data.split("\n")
    for l in lines:
        if not l:
            lines.remove(l)
    return len(lines)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python word_count.py <file>")
        exit(1)

    
