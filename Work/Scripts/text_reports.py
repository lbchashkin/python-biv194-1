# -*- coding: utf-8 -*-
"""
Created on Wed May  6 16:40:47 2020

@author: Леонид (рабочий)
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

base = pd.read_csv('base.csv')


def kol_statistic(D, name):
    data = D[name]
    new_info = pd.DataFrame({'Переменные': data, 'Максимум': '', \
                             'Минимум': '', 'Среднее арифметическое': '', \
                             'Выборочная дисперсия': '', \
                             'Стандартное отклонение': ''})
    new_info.loc[0, 'Максимум'] = data.max()
    new_info.loc[0, 'Минимум'] = data.min()
    new_info.loc[0, 'Среднее арифметическое'] = data.mean()
    new_info.loc[0, 'Выборочная дисперсия'] = data.var()
    new_info.loc[0, 'Стандартное отклонение'] = data.std()
    return new_info

def kach_statistic(D, name):
    stat1 = D[name].value_counts()
    stat2 = D[name].value_counts(normalize = True)
    new_info = pd.DataFrame({'Переменные': stat1.index, \
                             'Частоты': stat1, 'Процент': stat2})
    return new_info

def small_table(D, rows_numbers, column_numbers):
    data = D.iloc[rows_numbers, column_numbers]
    return data


"""
Метод pivot_table (pandas.Dataframe)
values = значения для агрегирования
index = строки сводной таблицы
columns = столбцы сводной таблицы
aggfunc = функция агрегирования
Подробно с примерами:
    https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.pivot_table.html
base.pivot_table(values = 'Глюкоза, ммоль/л', index = ['Школа', 'Дата приёма'], columns = ['Прививка от гриппа'], aggfunc = len)
"""

"""
f = pd.ExcelWriter('1.xlsx')
kol_statistic(base, 'Глюкоза, ммоль/л').to_excel(f, index = False, sheet_name = 'Отчёт')
writer = f.sheets['Отчёт']
writer.set_column('A:F', 25)
f.save()
kach_statistic(base, 'Дата приёма').to_excel('2.xlsx', index = False)
"""


    

