# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 15:10:37 2021

@author: dhtmd
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = "drinks.csv"
drinks = pd.read_csv(file_path)

total_mean = drinks.total_litres_of_pure_alcohol.mean()

continent_mean = drinks.groupby('continent')['total_litres_of_pure_alcohol'].mean()

continents = continent_mean.index.tolist()
continents.append('mean')
x_pos = np.arange(len(continents))
alcohol = continent_mean.tolist()
alcohol.append(total_mean)

bar_list = plt.bar(x_pos,alcohol, align='center',alpha=0.5)
bar_list[len(continents) - 1].set_color('r')
plt.plot([0.,6],[total_mean,total_mean],"k--")
plt.xticks(x_pos,continents)

plt.ylabel('total_litres_of_pure_alcohol')
plt.title('total_litres_of_pure_alcohol by Continent')
plt.show()