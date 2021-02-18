# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 14:07:16 2021

@author: dhtmd
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = "drinks.csv"
drinks = pd.read_csv(file_path)
result = drinks.groupby('continent').spirit_servings.agg(["mean","min","max","sum"])
print(result)

total_mean = drinks.total_litres_of_pure_alcohol.mean()
print(total_mean)


continent_mean = drinks.groupby('continent').mean()
print(continent_mean)

#대륙별 평균 술 양
continent_mean_a = drinks.groupby('continent').total_litres_of_pure_alcohol.mean()
print(continent_mean_a)

#평균보다 술 많이 먹는 나라
continent_mean_over = continent_mean_a[continent_mean_a>=total_mean]
print(continent_mean_over)

n_groups = len(result.index)
means = result['mean'].tolist()
mins = result['min'].tolist()
maxs = result['max'].tolist()
sums = result['sum'].tolist()

index = np.arange(n_groups)
bar_width = 0.1

rects1 = plt.bar(index,means, bar_width, color='r', label='Mean')
rects2 = plt.bar(index+bar_width,mins, bar_width, color='g', label='Min')
rects3 = plt.bar(index+bar_width*2,maxs, bar_width, color='b', label='Max')
rects4 = plt.bar(index+bar_width*3,sums, bar_width, color='y', label='Sum')

plt.xticks(index, result.index.tolist())
plt.legend()
plt.show()