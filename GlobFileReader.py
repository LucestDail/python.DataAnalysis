#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from operator import itemgetter
import sys
import glob
import os

print("glob output : ")
inputPath = sys.argv[1]
for input_file in glob.glob(os.path.join(inputPath, '*.txt')):
    with open(input_file, 'r', newline='') as filereader:
        for row in filereader:
            print("{}".format(row.strip()))
