#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from operator import itemgetter
import sys

# file reader
print('output : ')
InputFile = sys.argv[1]
filereader = open(InputFile, 'r')
for row in filereader:
    print(row.strip())
filereader.close()