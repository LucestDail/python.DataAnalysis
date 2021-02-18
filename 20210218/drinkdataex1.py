# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 11:59:15 2021
drinkdataex1.py
@author: dhtmd
"""

import pandas as pd
import seaborn as sns
file_path = 'drinks.csv'
drinks = pd.read_csv(file_path)
print(drinks.info())
print(drinks.describe())
corr = drinks[['beer_servings','wine_servings']].corr(method = 'pearson')
print(corr)

cols = ["beer_servings","spirit_servings","wine_servings","total_litres_of_pure_alcohol"]
corr = drinks[cols].corr(method="pearson")
print(corr)

cols_view = ["beer", "spirit", "wine", "alcohol"]
sns.set(font_scale=1.5)
hm = sns.heatmap(corr.values, cbar=True, annot=True, square=True, fmt=".2f",annot_kws={'size':15},yticklabels=cols_view,xticklabels=cols_view)