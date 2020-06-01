# -*- coding: utf-8 -*-
# pylint: disable=C0103, E0110
"""
Модуль с функциями для работы программы
Версия 2.1
Дата: 01.06.2020 16:47
"""
import tkinter as tk
import os
import sys
import pandas as pd
import time
import re

def is_phone(s):
    '''
    Является ли строка телефоном
    Входные параметры:
        s - строка
    Выходные параметры:
        True/False
    '''
    if len(s) != 8 or not re.search(r'\d\d-\d\d-\d\d', s):
        x = False
    else:
        x = True
    return x
    
def check_num(s, k):
    '''
    Функция проверки значения глюкозы и инсулина в крови
    Входные параметры:
        s - строка
        k - коэффициент (1 - глюкоза, 2 - инсулин)
    Выходные параметры:
        True/False
    Автор: Чашкин Л.
    '''
    k = int(k)
    try:
        float(s)
    except ValueError:
        if s == '':
            x = True
        else:
            x = False
    else:
        if float(s) < 0 or float(s) > 15*k:
            x = False
        else:
            x = True
    finally:
        return x

def is_date(s):
    '''
    Функция проверки, что строка является датой
    Входные параметры:
        s - строка
    Выходные параметры:
        True/False
    Автор: Чашкин Л.
    '''
    try:
        if len(s) == 10:
            date = time.strptime(s, '%d.%m.%Y')
        else:
            raise ValueError
    except ValueError:
        x = False
    else:
        now = time.localtime()
        d = f'{now[2]:02}'
        m = f'{now[1]:02}'
        y = f'{now[0]:02}'
        now = int(f'{y}{m}{d}')
        d = date[2]
        m = date[1]
        y = date[0]
        date = int(f'{y}{m}{d}')
        past = 20000101
        if (date-past) < 0:
            x = False
        elif (now - date) < 0:
            x = False
        else:
            x = True
    return x

def is_color(s):
    '''
    Функция проверки, что строка является цветом
    Входные параметры:
        s - строка
    Выходные параметры:
        True/False - результат проверки
    Автор: Чашкин Л.
    '''
    try:
        #Попытка сделать фоном данную строку
        tk.Tk()['bg'] = s
    except tk.TclError:
        x = False
    else:
        x = True
    return x


def index2Excel(n):
    '''
    Функция перевода номера столбца в буквенное обозначение (как в Excel)
    Номера начинаются с нуля
    Входные данные:
        n - номер столбца
    Выходные данные:
        буквенное обозначение столбца в Excel
    Пример:
        0 -- A
        25 -- Z
        26 -- AA
    Автор: Чашкин Л.
    '''
    s = []
    #Перевод числа в 26-ричную систему, 0 - значащий разряд (01 != 1)
    while n // 26 != 0:
        s.append(n % 26)
        n = n // 26 - 1
    s.append(n % 26)
    s.reverse()
    return ''.join([chr(65 + i) for i in s])


def save_configurations(path, configurations):
    '''
    Функция сохранения настроек в файл
    Входные параметры:
        path (строка) - путь к файлу настроек
        configurations (кортеж) - 5 элементов настроек:
            [0] (строка) - место сохранения текстовых отчётов
            [1] (строка) - место сохранения графических отчётов
            [2] (строка) - шрифт
            [3] (строка) - цвет фона
            [4] (строка) - цвет кнопок
    Выходные параметры:
        -
    '''
    with open(path, 'w', encoding="utf-8") as f:
        f.write('"""\nФайл с настройками\n"""')
        f.write(f'\ntext_path = r"{configurations[0]}"')
        f.write(f'\ngraph_path = r"{configurations[1]}"')
        f.write(f'\nfont = "{configurations[2]}"')
        f.write(f'\ncfon = "{configurations[3]}"')
        f.write(f'\ncknop = "{configurations[4]}"')


def read_configurations(path):
    '''
    Функция чтения настроек из файла
    Входные параметры:
        path - путь к файлу настроек
    Выходные параметры:
        (text_dir, graph_dir, font, color1, color2) - кортеж настроек
        text_dir - место сохранения текстовых отчётов
        graph_dir - место сохранения графических отчётов
        font - шрифт
        color1 - цвет фона
        color2 - цвет кнопок
        Если что-то прочитать не удалось, то возвращается значение по умолчанию
        Значения по умолчанию:
            text_dir = '1'
            graph_dir = '2'
            font = 'Tahoma'
            color1 = '#1'
            color2 = '#2'
    Автор: Чашкин Л.
    '''
    text_dir = '1'
    graph_dir = '2'
    font = 'Tahoma'
    color1 = '#1'
    color2 = '#2'
    if os.path.exists(path):
        with open(path, 'r') as f:
            lines = f.readlines()
        try:
            #Текстовые отчёты
            if os.path.exists(lines[1][18:].rstrip('\n')):
                text_dir = lines[1][18:].rstrip('\n')
            #Графические отчёты
            if os.path.exists(lines[2][20:].rstrip('\n')):
                graph_dir = lines[2][20:].rstrip('\n')
            fonts = ('Tahoma', 'Arial', 'Times New Roman', 'Calibri')
            #Шрифт
            if lines[3][7:].rstrip('\n') in fonts:
                font = lines[3][7:].rstrip('\n')
            #Цвет фона
            if is_color(lines[4][11:].rstrip('\n')):
                color1 = lines[4][11:].rstrip('\n')
            #Цвет шрифта
            if is_color(lines[5][13:].rstrip('\n')):
                color2 = lines[5][13:].rstrip('\n')
        except IndexError:
            pass
    return (text_dir, graph_dir, font, color1, color2)


def check_system():
    '''
    Функция проверки запуска в нужной системе
    Входные параметры: -
    Выходные параметры:
        True/False
    Автор: Чашкин Л.
    '''
    ver = sys.version_info
    return sys.platform == 'win32' and ver.major == 3 and ver.minor == 7


def check_base(base):
    '''
    Функция проверки, что кортеж содержит 3 отношения pandas.DataFrame
    с нужными столбцами
    Входные параметры:
        base - кортеж
    Выходные параметры:
        True/False
    Автор: Чашкин Л.
    '''
    columns = [('Ученик', 'Школа', 'Дата приёма', 'Глюкоза, ммоль/л',
                'Инсулин, мкЕд/мл', 'Прививка от гриппа'),
               ('Школа', 'Врач', 'Номер телефона школы'),
               ('Ученик', 'Школа', 'Дата рождения')]
    x = True
    if not (isinstance(base, tuple) and len(base) == 3):
        x = False
    else:
        for i in range(3):
            if not isinstance(base[i], pd.DataFrame):
                x = False
            elif tuple(base[i].columns) != columns[i]:
                x = False
                print(1)
    return x


def load_base(path):
    '''
    Функция открытия базы данных из формата pickle
    Входные параметры:
        path - путь к базе данных (строка)
    Выходные параметры:
        Словарь вида {base: base, error: error}
        base - кортеж из 3 баз данных pandas.DataFrame/пустой кортеж
        error - код ошибки
        Коды ошибок:
            0 - успешное считывание
            1 - не удалось считать
            2 - удалось считать, но содержимое неожиданное
    Автор: Чашкин Л.
    '''
    if path.endswith('.pickle') and os.path.exists(path):
        base = pd.read_pickle(path)
        if not check_base(base):
            error = 2
        else:
            error = 0
    else:
        base = ()
        error = 1
    return {'base': base, 'error': error}


def save_base(path, base):
    '''
    Функция сохранения базы данных в формате pickle
    Входные параметры:
        path - путь к файлу (строка)
        base - кортеж из 3 баз данных pandas.DataFrame
    Выходные параметры:
        True/False - результат сохранения
    Автор: Чашкин Л.
    '''
    if path.endswith('.pickle') and check_base(base):
        try:
            pd.to_pickle(base, path)
            x = True
        except IOError:
            x = False
    else:
        x = False
    return x


def kol_statistic(data):
    '''
    Функция построения таблицы с количественной статистикой
    Входные данные:
        data - столбец со значениями количественной переменной (pandas.Series)
    Выходные данные:
        Словарь вида {'stat': new_info, 'error': error}
        new_info - таблица с количественной статистикой (pandas.DataFrame)
        error - код ошибки
        Коды ошибок:
            0 - успешное проведение анализа
            1 - анализ не был проведён (ошибка типа данных)
    Автор: Чашкин Л.
    '''
    if data.dtype == int or data.dtype == float:
        new_info = pd.DataFrame({'Переменные': data, 'Максимум': '',
                                 'Минимум': '', 'Среднее арифметическое': '',
                                 'Выборочная дисперсия': '',
                                 'Стандартное отклонение': ''})
        new_info.loc[0, 'Максимум'] = round(data.max(), 5)
        new_info.loc[0, 'Минимум'] = round(data.min(), 5)
        new_info.loc[0, 'Среднее арифметическое'] = round(data.mean(), 5)
        new_info.loc[0, 'Выборочная дисперсия'] = round(data.var(), 5)
        new_info.loc[0, 'Стандартное отклонение'] = round(data.std(), 5)
        error = 0
    else:
        new_info = pd.DataFrame()
        error = 1
    return {'stat': new_info, 'error': error}


def kach_statistic(data):
    '''
    Функция построения таблицы с количественной статистикой
    Входные данные:
        data - столбец со значениями качественной переменной (pandas.Series)
    Выходные данные:
        Словарь вида {'stat': new_info, 'error': error}
        new_info - таблица с качественной статистикой (pandas.DataFrame)
        error - код ошибки
        Коды ошибок:
            0 - успешное проведение анализа
            1 - анализ не был проведён (ошибка типа данных)
    Автор: Чашкин Л.
    '''
    if data.dtype == int or data.dtype == float:
        new_info = pd.DataFrame()
        error = 1
    else:
        stat1 = data.value_counts()
        stat2 = data.value_counts(normalize=True).round(5)
        new_info = pd.DataFrame({'Переменные': stat1.index,
                                 'Частоты': stat1, 'Процент': stat2})
        error = 0
    return {'stat': new_info, 'error': error}


def small_table(data, rows_numbers, column_names):
    '''
    Функция построения таблицы с определёнными столбцами и строками
    Входные данные:
        data - база данных (pandas.DataFrame)
    Выходные данные:
        Словарь вида {'table': table, 'error': error}
        table - таблица с заданными столбцами и номерами строк
        error - код ошибки
        Коды ошибок:
            0 - успешное построение таблицы
            1 - таблицу не удалось построить, ошибка в номерах строк
            2 - таблицу не удалось построить, ошибка в названии столбцов
    Автор: Чашкин Л.
    '''
    if not max(rows_numbers) < len(data) and min(rows_numbers) >= 0:
        table = pd.DataFrame()
        error = 1
    elif False in [(name in data) for name in column_names]:
        table = pd.DataFrame()
        error = 2
    else:
        table = data[column_names].iloc[rows_numbers]
        error = 0
    return {'table': table, 'error': error}


def pivot_table(data, values, index, columns=None):
    '''
    Функция построения сводной таблицы
    Входные данные:
        data - база данных (pandas.DataFrame)
        values - название столбца - значения для агрегирования
        index - название столбца - строка сводной таблицы
        columns - название столбца - столбец сводной таблицы
    Выходные данные:
        Словарь вида {'table': table, 'error': error}
        table - сводная таблица (pandas.DataFrame)
        error - код ошибки
        Коды ошибок:
            0 - успешное построение таблицы
            1 - таблицу не удалось построить, ошибка в названии столбцов
            2 - ошибка в типе столбца значений
    Автор: Чашкин Л.
    '''
    crit1 = values not in data #Нет 1 столбца
    crit2 = index not in data #Нет 2 столбца
    crit3 = columns is not None and columns not in data #Нет 3 столбца
    if crit1 or crit2 or crit3:
        error = 1
        table = pd.DataFrame()
    elif data[values].dtype == int or data[values].dtype == float:
        table = pd.pivot_table(data, values, index, columns, fill_value='-')
        error = 0
    else:
        table = pd.DataFrame()
        error = 2
    return {'table': table, 'error': error}


def w_column(data):
    '''
    Функция для вычисления оптимальной ширины столбца в Excel
    Входные данные:
        data - столбец с данными (pandas.Series)
    Выходные данные:
        Ширина столбца (int)
    Автор: Чашкин Л.
    '''
    #Составляем массив длин строк
    lengths = [len(str(s)) for s in data]
    lengths.append(len(str(data.name)))
    return max(lengths) + 5


def check_condition(table, condition):
    '''
    Функция проверки условия на правильность
    Входные данные:
        table - таблица pandas.DataFrame
        condition - условие - список из 3 элементов:
            1 элемент - название атрибута
            2 элемент - наименование способа сравнения
            3 элемент - значение для сравнения
    Выходные данные:
        True/False - корректность данных
    Автор: Чашкин Л.
    '''
    if condition[0] and condition[1] and condition[2]:
        if table[condition[0]].dtype == int or table[condition[0]].dtype == float:
            x = True
            try:
                condition[2] = float(condition[2])
            except ValueError:
                x = False
        elif condition[1] in ['равно', 'не равно']:
            x = True
        else:
            x = False
    else:
        x = False
    return x


def list2index(table, condition):
    '''
    Получение логического отбора строк из таблицы по условию
    Входные данные:
        table - таблица pandas.DataFrame
        condition - условие - список из 3 элементов:
            1 элемент - название атрибута
            2 элемент - наименование способа сравнения
            3 элемент - значение для сравнения
    Выходные данные:
        ind1 - pandas.Series, содержащий значения True при строках, подходящих
        под условие и False при неподходящих
    '''
    column = condition[0]
    value = condition[2]
    if condition[1] == 'равно':
        ind1 = table[column] == value
    elif condition[1] == 'не равно':
        ind1 = table[column] != value
    elif condition[1] == 'больше или равно':
        ind1 = table[column] >= value
    elif condition[1] == 'меньше или равно':
        ind1 = table[column] <= value
    elif condition[1] == 'больше':
        ind1 = table[column] > value
    else:
        ind1 = table[column] < value
    return ind1


def get_index(conditions, table):
    '''
    Получение общего логического отбора для 3 условий
    Входные данные:
        conditions - список условий вида condititon и способы объединения условий (И/ИЛИ)
            1 элемент - название атрибута
            2 элемент - наименование способа сравнения
            3 элемент - значение для сравнения
        table - база данных pandas.DataFrame
    Выходные данные:
        словарь вида {index: ind, error: error}
        ind - pandas.Series, содержащий значения True при строках, подходящих
        под условие и False при неподходящих
        error - код ошибки
        Коды ошибок:
            0 - успешный отбор строк
            1 - не удалось отборать строки
    '''
    ind = pd.Series([True for _ in range(len(table))])
    error = 0
    if check_condition(table, conditions[0]):
        #1 условие корректно
        ind = list2index(table, conditions[0])
        if check_condition(table, conditions[2]):
            #2 условие корректно
            if conditions[1] == 'И':
                ind = ind & list2index(table, conditions[2])
            else:
                ind = ind | list2index(table, conditions[2])
            if check_condition(table, conditions[4]):
                #3 условие корректно
                if conditions[3] == 'И':
                    ind = ind & list2index(table, conditions[4])
                else:
                    ind = ind | list2index(table, conditions[4])
    else:
        error = 1
    return {'index': ind, 'error': error}


def save_text(data, path, index_save):
    '''
    Функция сохранения текстового отчёта в файл Excel
    Входные данные:
        data - таблица (pandas.DataFrame)
        path - путь к папке для сохранения отчёта
        index_save - True/False (нужно ли сохранять индексы строк)
    Выходные данные:
        True/False - результат сохранения
    Автор: Чашкин Л.
    '''
    if os.path.exists(path):
        try:
            f = open(os.path.join(path, '1' + '.xlsx'), 'w')
            f.close()
            with pd.ExcelWriter(os.path.join(path, '1' + '.xlsx')) as f:
                data.to_excel(f, index=index_save, sheet_name='Отчёт')
                writer = f.sheets['Отчёт']
                if index_save:
                    #В первый столбец записываем индексы строк
                    writer.set_column('A:A', w_column(data.index))
                for i in range(len(data.columns)):
                    j = int(index_save) + i
                    s = index2Excel(j) #Название столбца
                    writer.set_column(':'.join([s, s]),
                                      w_column(data.iloc[:, i]))
                f.save()
            x = True
        except IOError:
            x = False
    else:
        x = False
    return x
