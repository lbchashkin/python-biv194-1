# -*- coding: utf-8 -*-
"""
Created on Wed May  6 23:01:02 2020

@author: Леонид (рабочий)
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

base = pd.read_csv('base.csv')

def create_scatter(base, value_x, value_y, name):
    data = base.pivot_table(values = [value_x, value_y], index = name)
    fig, ax = plt.subplots(1, 1)
    for i in range(len(data.index)):
        ax.scatter(data.iloc[i, 0], data.iloc[i, 1])
    ax.legend(bbox_to_anchor=(1.05, 1), borderaxespad=0, labels = data.index, loc = 2)
    return fig

#my_fig = create_scatter(base, 'Глюкоза, ммоль/л', 'Инсулин, мкЕд/мл', 'Дата приёма')
#my_fig.savefig('1.png', bbox_inches = 'tight')
"""
data = base.iloc[:, [5, 4]].groupby('Прививка от гриппа').groups
fig, ax = plt.subplots(1, 1)
ax.boxplot([list(map(lambda x: base.iloc[x, 4], group)) for group in data.values()], labels = data.keys())
plt.show()
"""
