#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 17:43:09 2020

@author: oseunghyeon
"""

import sys
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)
print(data_frame)
data_frame.to_csv(output_file, index = False)