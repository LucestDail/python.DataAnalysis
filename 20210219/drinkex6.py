# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 09:44:42 2021

@author: dhtmd
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = "drinks.csv"
drinks = pd.read_csv(file_path)

drinks['total_servings'] = drinks['beer_servings'] + drinks['wine_servings'] + drinks['spirit_servings']
drinks['alcohol_rate'] = drinks['total_litres_of_pure_alcohol'] / drinks['total_servings']
drinks['alcohol_rate'] = drinks['alcohol_rate'].fillna(0)
country_with_rank = drinks[['country','alcohol_rate']]
country_with_rank = country_with_rank.sort_values(by=['alcohol_rate'],ascending=0)
print(country_with_rank.head(5))

country_list = country_with_rank.country.tolist()
x_pos = np.arange(len(country_list))
rank = country_with_rank.alcohol_rate.tolist()

bar_list = plt.bar(x_pos,rank)
bar_list[country_list.index("South Korea")].set_color("r")
plt.ylabel("alcohol rate")
plt.title("liquor drink rank by country")
plt.axis([0,200,0,0.3])
korea_rank = country_list.index("South Korea")
korea_alc_rate = country_with_rank[country_with_rank["country"] == "South Korea"]["alcohol_rate"].values[0]
plt.annotate("South Korea : " + str(korea_rank + 1), xy = (korea_rank, korea_alc_rate), xytext=(korea_rank+10,korea_alc_rate+0.05),arrowprops=dict(facecolor="red", shrink=0.05))
plt.show()