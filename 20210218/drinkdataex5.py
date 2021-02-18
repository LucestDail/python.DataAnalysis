# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 16:00:17 2021

@author: dhtmd
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
file_path = "drinks.csv"
drinks = pd.read_csv(file_path)
drinks["total_servings"] = drinks["beer_servings"] + drinks["wine_servings"] + drinks["spirit_servings"]
print(drinks)

#alcohol_rate = total_litres_of_pure_alcohol / total_servings
drinks["alcohol_rate"] = drinks["total_litres_of_pure_alcohol"] / drinks["total_servings"]
print(drinks.info())

#alcohol_rate null 인 경우 0 으로 변경
drinks["alcohol+rate"] = drinks["alcohol_rate"].fillna(0)