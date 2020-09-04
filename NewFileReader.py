#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from operator import itemgetter
import sys

input_file = sys.argv[1]
print("output : ")
with open(input_file, 'r', newline='') as filereader:
    for row in filereader:
        print("{}".format(row.strip()))