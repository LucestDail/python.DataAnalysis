#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from math import exp, log, sqrt
import re

# small testing about regular expression
string = "it is simple test string for regular expression test"
string_list = string.split()
pattern = re.compile(r"test",re.I)
count = 0
for word in string_list:
    if pattern.search(word):
        count += 1
print(f'output #r1: {count}')