# -*- coding: utf-8 -*-
# pylint: disable=C0103
"""
Created on Sun May 17 01:50:49 2020

@author: Кретова Анна
Версия 2.1
Дата: 01.06.2020 16:47
"""

from tkinter import ttk
from tkinter import colorchooser
import tkinter as tk
import tkinter.messagebox as mb
import tkinter.filedialog as fd
import sys
import os
import pandas as pd
from settings import cfon, cknop, font, text_path, graph_path


path = os.getcwd()
os.chdir(os.path.abspath(os.path.join(path, '..')))
sys.path.append(os.path.join(os.getcwd(), 'Library'))
import functions
tah = (font, 12)

def merging(analyses, schools, students):
    """
    Функция объединения таблиц
    Входные данные: 3 таблицы
    Выходные данные: объединённая таблицы
    Автор: Чашкин Л.
    """
    COL1 = ['Ученик', 'Школа', 'Дата рождения', 'Врач', 'Номер телефона школы']
    COL2 = ['Ученик', 'Школа', 'Дата рождения', 'Глюкоза, ммоль/л', 'Инсулин, мкЕд/мл',
            'Прививка от гриппа', 'Дата приёма', 'Врач', 'Номер телефона школы']
    temp = pd.merge(students, schools, on='Школа', how='outer').fillna('—')[COL1]
    return pd.merge(analyses, temp, on=['Ученик', 'Школа'], how='outer').fillna('—')[COL2]

def delete_nan(DF):
    """
    Удаление строк с пропущенными значениями
    Входные данные: таблица с пропусками
    Выходные данные: таблица без пропусков
    Автор: Чашкин Л.
    """
    return DF.replace('—', pd.np.nan)

def help1():
    """
    Функция help1 создаёт окно со справкой
    @author: Кретова Анна
    """
    #Создание окна
    root1 = tk.Toplevel()
    root1.title("Справка")
    root1.geometry('320x250+450+220')
    root1.resizable(False, False)

    #Текст
    label1 = tk.Label(root1, text='О программе:', fg="Black", bd=3, font=tah)
    label2 = tk.Label( \
      root1, \
      text='Разработчики:\nКретова Анна\nНагайцева Кристина\nЧашкин Леонид\n\
      1 бригада, группа БИВ194', \
      fg="Black", bd=3, font=tah)
    label7 = tk.Label(root1, text='Руководитель: \nПоляков Константин Львович',
                      fg="Black", bd=3, font=tah)
    label8 = tk.Label(root1, text='МИЭМ НИУ ВШЭ\n2020', fg="Black", bd=3,
                      font=tah)

    #Положение элементов
    label1.grid(row=0, column=0, pady=3, padx=100)
    label2.grid(row=1, column=0, pady=3, padx=3)
    label7.grid(row=2, column=0, pady=3)
    label8.grid(row=3, column=0, pady=3)

def zav(canvas1, canvas2, combobox, entr1, entr2):
    """
    Функция zav возвращает заводские настройки
    @author: Кретова Анна
    """
    canvas1['bg'] = "#052F6D"
    canvas2['bg'] = "#6A94D4"
    combobox.set('Tahoma')
    entr1['state'] = 'normal'
    entr1.delete(0, tk.END)
    entr1.insert(0, os.path.abspath(os.path.join(path, 'Output')))
    entr1['state'] = 'readonly'
    entr2['state'] = 'normal'
    entr2.delete(0, tk.END)
    entr2.insert(0, os.path.abspath(os.path.join(path, 'Graphics')))
    entr2['state'] = 'readonly'

def cost():
    """
    Функция cost создаёт окно настроек
    @author: Кретова Анна
    """
    def zav1():
        zav(canvas1, canvas2, combobox, entr1, entr2)
    #Создание окна
    root2 = tk.Toplevel()
    root2.title("Настройки")
    root2.geometry('620x250+360+280')
    root2.resizable(False, False)
    root2.configure(bg=cfon)

    #Текст
    tk.Label(root2, text='Место хранения текстовых отчётов', bg=cfon,
             fg="White", bd=3, font=tah).grid(row=0, column=0, pady=1)
    tk.Label(root2, text='Место хранения графических отчётов', bg=cfon,
             fg="White", bd=3, font=tah).grid(row=1, column=0, pady=1)
    tk.Label(root2, text='Шрифт', bg=cfon, fg="White", bd=3, font=tah).grid(row=2, column=0, pady=1)
    tk.Label(root2, text='Цвет фона', bg=cfon,
             fg="White", bd=3, font=tah).grid(row=3, column=0, pady=1)
    tk.Label(root2, text='Цвет кнопок', bg=cfon,
             fg="White", bd=3, font=tah).grid(row=4, column=0, pady=1)

    #Квадратики с выбором цвета
    canvas1 = tk.Canvas(root2, width=20, height=20, bg=cfon)
    canvas1.grid(row=3, column=1, sticky='w')
    canvas2 = tk.Canvas(root2, width=20, height=20, bg=cknop)
    canvas2.grid(row=4, column=1, sticky='w')

    def fon():
        fon = colorchooser.askcolor()
        root2.lift()
        canvas1['bg'] = fon[1]

    def knop():
        knop = colorchooser.askcolor()
        root2.lift()
        canvas2['bg'] = knop[1]
    
    def dialog(path, entry):
        new_path = fd.askdirectory()
        root2.lift()
        if new_path:
            entry['state'] = 'normal'
            entry.delete(0, 'end')
            entry.insert(0, os.path.normpath(new_path))
            entry['state'] = 'readonly'
    def save_set():
        functions.save_configurations('.\Scripts\settings.py', (entr1.get(), entr2.get(), combobox.get(), canvas1['bg'], canvas2['bg']))
        root2.destroy()
    #Кнопки
    but1 = tk.Button(root2, text="...", bg=cknop, fg="Black", bd=3,
                     font=tah, command=lambda: dialog(text_path, entr1))
    but2 = tk.Button(root2, text="...", bg=cknop, fg="Black", bd=3,
                     font=tah, command=lambda: dialog(graph_path, entr2))
    but3 = tk.Button(root2, text="Выбрать цвет", bg=cknop, fg="Black", bd=3,
                     font=tah, command=fon)
    but4 = tk.Button(root2, text="Выбрать цвет", bg=cknop, fg="Black", bd=3,
                     font=tah, command=knop)
    but5 = tk.Button(root2, text="Настройки по умолчанию", bg=cknop, fg="Black", bd=3,
                     font=tah, command=zav1)
    but6 = tk.Button(root2, text="Сохранить", bg=cknop, fg="Black", bd=3,
                     font=tah, command = save_set)

    #Ввод данных
    entr1 = tk.Entry(root2, font=tah, width=30)
    entr1.insert(0, text_path)
    entr1['state'] = 'readonly'
    entr2 = tk.Entry(root2, font=tah, width=30)
    entr2.insert(0, graph_path)
    entr2['state'] = 'readonly'

    #Раскрывающийся список
    combobox = ttk.Combobox(root2, state='readonly', width=28, font=tah)
    combobox['values'] = ['Tahoma', 'Calibri', 'Times New Roman', 'Arial']
    combobox.set(font)

    entr1.grid(row=0, column=1)
    entr2.grid(row=1, column=1)
    but1.grid(row=0, column=2, padx=10)
    but2.grid(row=1, column=2, padx=10)
    but3.grid(row=3, column=1, padx=10)
    but4.grid(row=4, column=1, padx=10)
    but5.grid(row=5, column=0, padx=10)
    but6.grid(row=5, column=1, padx=10, sticky='e', pady=30)
    combobox.grid(row=2, column=1)

def table_analyzes(buttons, tree, chart):
    """
    Функция table_analyzes выводит таблицу анализов
    @author: Кретова Анна
    """
    but4 = buttons[0]
    but5 = buttons[1]
    but6 = buttons[2]
    but7 = buttons[3]
    children = tree.get_children()
    for i in children:
        tree.delete(i)
    tree.grid_forget()
    #Таблица
    tree['columns'] = ['student', 'school', 'date', 'glucose', 'insulin', 'flu']
    tree.column('student', width=225, anchor=tk.CENTER)
    tree.column('school', width=200, anchor=tk.CENTER)
    tree.column('date', width=200, anchor=tk.CENTER)
    tree.column('glucose', width=150, anchor=tk.CENTER)
    tree.column('insulin', width=150, anchor=tk.CENTER)
    tree.column('flu', width=200, anchor=tk.CENTER)
    tree.heading('student', text='Ученик')
    tree.heading('school', text='Школа')
    tree.heading('date', text='Дата приёма')
    tree.heading('glucose', text='Глюкоза')
    tree.heading('insulin', text='Инсулин')
    tree.heading('flu', text='Прививка от гриппа')
    tree.grid(row=4, column=0, columnspan=7, sticky='nsew', padx=2)
    i = iter(chart.index)
    for item in chart.values:
        tree.insert('', 'end', next(i), values=list(item))
    #Скроллбар
    vscrollbar = tk.Scrollbar(orient='vert', command=tree.yview)
    tree['yscrollcommand'] = vscrollbar.set
    vscrollbar.grid(row=4, column=6, sticky='nse')

    #Цвет кнопки
    but4.configure(bg="White")
    but5.configure(bg=cknop)
    but6.configure(bg=cknop)
    but7.configure(bg=cknop)

def table_school(buttons, tree, chart):
    """
    Функция table_school выводит таблицу школ
    @author: Кретова Анна
    """
    but4 = buttons[0]
    but5 = buttons[1]
    but6 = buttons[2]
    but7 = buttons[3]
    children = tree.get_children()
    for i in children:
        tree.delete(i)
    tree.grid_forget()
    #Таблица
    tree['columns'] = ['school', 'doctor', 'phone']
    tree.column('school', width=375, anchor=tk.CENTER)
    tree.column('doctor', width=375, anchor=tk.CENTER)
    tree.column('phone', width=375, anchor=tk.CENTER)
    tree.heading('school', text='Школа')
    tree.heading('doctor', text='Врач')
    tree.heading('phone', text='Телефон')
    tree.grid(row=4, column=0, columnspan=7, sticky='nsew', padx=2)
    i = iter(chart.index)
    for item in chart.values:
        tree.insert('', 'end', next(i), values=list(item))
    #Скроллбар
    vscrollbar = tk.Scrollbar(orient='vert', command=tree.yview)
    tree['yscrollcommand'] = vscrollbar.set
    vscrollbar.grid(row=4, column=6, sticky='nse')

    #Цвет кнопки
    but4.configure(bg=cknop)
    but5.configure(bg="White")
    but6.configure(bg=cknop)
    but7.configure(bg=cknop)

def table_students(buttons, tree, chart):
    """
    Функция table_students выводит таблицу учеников
    @author: Кретова Анна
    """
    but4 = buttons[0]
    but5 = buttons[1]
    but6 = buttons[2]
    but7 = buttons[3]
    #Таблица
    children = tree.get_children()
    for i in children:
        tree.delete(i)
    tree.grid_forget()
    tree['columns'] = ['student', 'school', 'date']
    tree.column('student', width=375, anchor=tk.CENTER)
    tree.column('school', width=375, anchor=tk.CENTER)
    tree.column('date', width=375, anchor=tk.CENTER)
    tree.heading('student', text='Ученик')
    tree.heading('school', text='Школа')
    tree.heading('date', text='Дата рождения')
    tree.grid(row=4, column=0, columnspan=7, sticky='nsew', padx=2)
    i = iter(chart.index)
    for item in chart.values:
        tree.insert('', 'end', next(i), values=list(item))
    #Скроллбар
    vscrollbar = tk.Scrollbar(orient='vert', command=tree.yview)
    tree['yscrollcommand'] = vscrollbar.set
    vscrollbar.grid(row=4, column=6, sticky='nse')

    #Цвет кнопки
    but4.configure(bg=cknop)
    but5.configure(bg=cknop)
    but6.configure(bg="White")
    but7.configure(bg=cknop)

def table(buttons, tree, chart):
    """
    Функция table выводит полный список
    @author: Кретова Анна
    """
    but4 = buttons[0]
    but5 = buttons[1]
    but6 = buttons[2]
    but7 = buttons[3]
    #Таблица
    children = tree.get_children()
    for i in children:
        tree.delete(i)
    tree.grid_forget()
    tree['columns'] = ['student', 'school', 'date_bir', 'glucose', 'insulin',
                       'flu', 'date', 'doctor', 'phone']
    tree.column('student', width=250, anchor=tk.CENTER)
    tree.column('date_bir', width=105, anchor=tk.CENTER)
    tree.column('school', width=100, anchor=tk.CENTER)
    tree.column('phone', width=113, anchor=tk.CENTER)
    tree.column('glucose', width=73, anchor=tk.CENTER)
    tree.column('insulin', width=70, anchor=tk.CENTER)
    tree.column('flu', width=70, anchor=tk.CENTER)
    tree.column('date', width=100, anchor=tk.CENTER)
    tree.column('doctor', width=245, anchor=tk.CENTER)
    tree.heading('student', text='Ученик')
    tree.heading('date_bir', text='Дата рождения')
    tree.heading('school', text='Школа')
    tree.heading('phone', text='Номер телефона школы')
    tree.heading('glucose', text='Глюкоза')
    tree.heading('insulin', text='Инсулин')
    tree.heading('flu', text='Прививка')
    tree.heading('date', text='Дата приёма')
    tree.heading('doctor', text='Врач')
    tree.grid(row=4, column=0, columnspan=7, sticky='nsew', padx=2)
    i = iter(chart.index)
    for item in chart.values:
        tree.insert('', 'end', next(i), values=list(item))

    #Скроллбар
    vscrollbar = tk.Scrollbar(orient='vert', command=tree.yview)
    tree['yscrollcommand'] = vscrollbar.set
    vscrollbar.grid(row=4, column=6, sticky='nse')

    #Цвет кнопки
    but4.configure(bg=cknop)
    but5.configure(bg=cknop)
    but6.configure(bg=cknop)
    but7.configure(bg="White")

def saving(base):
    """
    Сохранение базы данных
    Входные данные: кортеж из таблиц
    Выходные данные: -
    Автор: Чашкин Л.
    """
    path = fd.asksaveasfilename(initialdir=os.path.join(os.getcwd(), 'Data'), filetypes=[("Pickle (.pickle)", '*.pickle')],
                                defaultextension=".pickle")
    if path != '':
        if not functions.save_base(path, (base[0], base[1], base[2])):
            mb.showinfo('Предупреждение',
                        'К сожалению, базу данных не удалось сохранить.\
                        Пожалуйста, попробуйте ещё раз.')

def opening(base, buttons, tree):
    """
    Открытие базы данных
    Входные данные: кортеж из таблиц
    Выходные данные: -
    Автор: Чашкин Л.
    """
    path = fd.askopenfilename(initialdir=os.path.join(os.getcwd(), 'Data'), filetypes=[("Pickle (.pickle)", '*.pickle')],
                              defaultextension=".pickle")
    if path:
        temp = functions.load_base(path)
        if temp['error'] == 1:
            mb.showerror('Ошибка', 'Не удалось загрузить базу данных')
        elif temp['error'] == 2:
            mb.showerror('Ошибка', 'Неожиданное содержимое базы данных')
        else:
            base[0] = temp['base'][0]
            base[1] = temp['base'][1]
            base[2] = temp['base'][2]
            base[3] = merging(base[0], base[1], base[2])
            k = color(buttons[0], buttons[1], buttons[2])
            func = (table_analyzes, table_school, table_students,
                    table)[k - 1]
            func(buttons, tree, base[k - 1])


def menu(root, base, buttons, tree):
    """
    Функция menu создаёт меню в главном окне
    @author: Кретова Анна
    """
    men = tk.Menu(root)
    file_m = tk.Menu(men, tearoff=0)
    men.add_cascade(label='Файл', menu=file_m)
    file_m.add_command(label='Открыть...', command=lambda: opening(base, buttons, tree))
    file_m.add_command(label='Сохранить...', command=lambda: saving(base))
    men.add_command(label='Настройки', command=cost)
    men.add_command(label='Справка', command=help1)
    root.config(menu=men)

def color(but4, but5, but6):
    """
    Функция color узнаёт, какая таблица сейчас открыта
    @author: Кретова Анна
    """
    if but4['bg'] == "White":
        tek = 1
    elif but5['bg'] == "White":
        tek = 2
    elif but6['bg'] == "White":
        tek = 3
    else:
        tek = 4
    return tek

def edit_analyze(root, tree, base, info, num):
    '''
    Редактирование анализов
    '''
    root.destroy()
    if '' in info:
        mb.showinfo('Предупреждение', 'Запись не будет изменена, одно из полей пустое')
    elif info[3] <= 0 or info[4] <= 0:
        mb.showinfo('Предупреждение', 'Запись не будет изменена, ошибка в значения анализов')
    else:
        if not functions.is_date(info[2]):
            mb.showinfo('Предупреждение', 'Запись не будет изменена, неверный формат даты')
        elif (info[0], info[1]) not in map(tuple, list(base[2][["Ученик",
                                                                "Школа"]].drop(num).values)):
            mb.showinfo('Предупреждение', 'Запись не будет изменена, нет такого ученика')
        elif (info[0], info[1],
              info[2]) in map(tuple, list(base[0][["Ученик", "Школа",
                                                   "Дата приёма"]].drop(num).values)):
            mb.showinfo('Предупреждение',
                        'Запись не будет изменена, эта информация уже есть в базе данных')
        else:
            base[0].loc[num, 'Ученик'] = info[0]
            base[0].loc[num, 'Школа'] = info[1]
            base[0].loc[num, 'Дата приёма'] = info[2]
            base[0].loc[num, 'Глюкоза, ммоль/л'] = info[3]
            base[0].loc[num, 'Инсулин, мкЕд/мл'] = info[4]
            base[0].loc[num, 'Прививка от гриппа'] = info[5]
            children = tree.get_children()
            for i in children:
                tree.delete(i)
            i = iter(base[0].index)
            for item in base[0].values:
                tree.insert('', 'end', next(i), values=list(item))
            base[3] = merging(base[0], base[1], base[2])

def dob_analyzes(root, x, tree, base):
    """
    Функция dob_analyzes создаёт окно добавления записей для таблицы "Анализы"
    @author: Кретова Анна
    """
    #Создание окна
    root4 = tk.Toplevel(root)
    if x == 1:
        root4.title("Добавление новой записи")
    else:
        root4.title("Изменение записи")
    root4.geometry('600x185+350+200')
    root4.resizable(False, False)
    root4.configure(bg=cfon)

    #Раскрывающийся список
    combobox1 = ttk.Combobox(root4, state='readonly', width=31, font=tah)
    combobox1['values'] = list(base[2]['Ученик'].values)
    if list(base[2]['Ученик'].values):
        combobox1.current(0)
    combobox2 = ttk.Combobox(root4, state='readonly', width=31, font=tah)
    combobox2['values'] = list(base[1]['Школа'].values)
    if list(base[1]['Школа'].values):
        combobox2.current(0)

    #Спинбокс
    sp1 = tk.Spinbox(root4, from_=0, to=15, increment=0.01, font=tah, validate='key')
    sp1['validatecommand'] = (sp1.register(functions.check_num), '%P', '1')
    sp1.grid(row=3, column=1, pady=1)
    sp2 = tk.Spinbox(root4, from_=0, to=30, increment=0.01, font=tah, validate='key')
    sp2['validatecommand'] = (sp2.register(functions.check_num), '%P', '2')
    sp2.grid(row=4, column=1, pady=1)

    #Флажок
    var = tk.StringVar()
    var.set('-')
    tk.Checkbutton(root4, variable=var, onvalue='+', offvalue='-',
                   bg=cfon, activebackground=cfon).grid(row=5, column=1, pady=1, sticky="w")

    #Ввод текста
    entr3 = tk.Entry(root4, validate='all')
    entr3.insert(0, 'ДД.ММ.ГГГГ')
    def check(what):
        xxx = True
        if what == 'focusin' and entr3.get() == 'ДД.ММ.ГГГГ':
            entr3.delete(0, 'end')
            entr3.configure(validate='all')
        elif what == 'focusout' and entr3.get() == '':
            entr3.delete(0, 'end')
            entr3.insert(0, 'ДД.ММ.ГГГГ')
            entr3.configure(validate='all')
        return xxx
    entr3.configure(validatecommand=(entr3.register(check), '%V'))

    #Текст
    tk.Label(root4, text='Ученик', bg=cfon, fg="White", bd=3,
             font=tah).grid(row=0, column=0, pady=1, padx=5)
    tk.Label(root4, text='Школа', bg=cfon, fg="White", bd=3,
             font=tah).grid(row=1, column=0, pady=1, padx=5)
    tk.Label(root4, text='Дата приёма', bg=cfon, fg="White", bd=3,
             font=tah).grid(row=2, column=0, pady=1, padx=5)
    tk.Label(root4, text='Глюкоза', bg=cfon, fg="White", bd=3,
             font=tah).grid(row=3, column=0, pady=1, padx=5)
    tk.Label(root4, text='Инсулин', bg=cfon, fg="White", bd=3,
             font=tah).grid(row=4, column=0, pady=1, padx=5)
    tk.Label(root4, text='Прививка от гриппа', bg=cfon, fg="White", bd=3,
             font=tah).grid(row=5, column=0, pady=1, padx=5, sticky="w")

    #Кнопка
    but = tk.Button(root4, text="Ок", bg=cknop, fg="Black", bd=3,
                    font=tah, width=10, height=1)
    but['command'] = lambda: add_items(root4, tree, base, 0,
                                       [combobox1.get(), combobox2.get(),
                                        '' if entr3.get() == 'ДД.ММ.ГГГГ' else entr3.get(),
                                        float(sp1.get()), float(sp2.get()), var.get()])

    #Расположение элементов
    but.grid(row=3, column=2, pady=1, padx=20)
    combobox1.grid(row=0, column=1, pady=1)
    combobox2.grid(row=1, column=1, pady=1)
    entr3.grid(row=2, column=1, pady=1)
    if x != 1 and len(tree.selection()) != 1:
        root4.destroy()
        mb.showerror('Ошибка', 'Для редактирования записи надо выбрать одну запись')
    elif x != 1:
        num = int(tree.selection()[0])
        combobox1.set(base[0].loc[num]['Ученик'])
        combobox2.set(base[0].loc[num]['Школа'])
        sp1.delete(0, tk.END)
        sp1.insert(0, base[0].loc[num]['Глюкоза, ммоль/л'])
        sp2.delete(0, tk.END)
        sp2.insert(0, base[0].loc[num]['Инсулин, мкЕд/мл'])
        entr3.delete(0, tk.END)
        entr3.insert(0, base[0].loc[num]['Дата приёма'])
        var.set(base[0].loc[num]['Прививка от гриппа'])
        but['command'] = lambda: edit_analyze(root4, tree, base,
                                              [combobox1.get(), combobox2.get(),
                                               '' if entr3.get() == 'ДД.ММ.ГГГГ' else entr3.get(),
                                               float(sp1.get()), float(sp2.get()), var.get()], num)

def edit_school(root, tree, base, info, num):
    '''
    Редактирование школы
    '''
    root.destroy()
    if '' in info:
        mb.showinfo('Предупреждение', 'Запись не будет изменена, одно из полей пустое')
    elif not functions.is_phone(info[2]):
        mb.showinfo('Предупреждение', 'Запись не будет изменена. Неверный формат телефона')
    else:
        schools = list(base[1]['Школа'].values)
        schools.remove(schools[num])
        if info[0] in schools:
            mb.showinfo('Предупреждение', 'Запись не будет изменена, так как уже есть такая школа')
        else:
            phones = list(base[1]['Номер телефона школы'].values)
            phones.remove(phones[num])
            if info[2] in phones:
                mb.showinfo('Предупреждение',
                            'Запись не будет изменена. У разных школ разные телефоны')
            else:
                ind = base[0]['Школа'] == base[1].loc[num][0]
                for i in base[0][ind].index:
                    base[0].loc[i, 'Школа'] = info[0]
                ind = base[2]['Школа'] == base[1].loc[num][0]
                for i in base[2][ind].index:
                    base[2].loc[i, 'Школа'] = info[0]                
                base[1].loc[num, 'Школа'] = info[0]
                base[1].loc[num, 'Врач'] = info[1]
                base[1].loc[num, 'Номер телефона школы'] = info[2]
                children = tree.get_children()
                for i in children:
                    tree.delete(i)
                i = iter(base[1].index)
                for item in base[1].values:
                    tree.insert('', 'end', next(i), values=list(item))
                base[3] = merging(base[0], base[1], base[2])

def dob_school(root, x, tree, base):
    """
    Функция dob_school создаёт окно добавления записей для таблицы "Школа"
    @author: Кретова Анна
    """
    #Создание окна
    root4 = tk.Toplevel(root)
    if x == 1:
        root4.title("Добавление новой записи")
    else:
        root4.title("Изменение записи")
    root4.geometry('370x145+350+200')
    root4.resizable(False, False)
    root4.configure(bg=cfon)

    #Ввод текста
    entr1 = tk.Entry(root4, font=tah, width=30)
    entr2 = tk.Entry(root4, font=tah, width=30)
    entr3 = tk.Entry(root4, font=tah, width=30, validate='all')

    #Текст
    label1 = tk.Label(root4, text='Школа', bg=cfon, fg="White", bd=3,
                      font=tah)
    label2 = tk.Label(root4, text='Врач', bg=cfon, fg="White", bd=3,
                      font=tah)
    label3 = tk.Label(root4, text='Телефон', bg=cfon, fg="White", bd=3,
                      font=tah)

    #Кнопка
    but = tk.Button(root4, text="Ок", bg=cknop, fg="Black", bd=3,
                    font=tah, width=10, height=1,
                    command=lambda: add_items(root4, tree, base, 1,
                                              [entr1.get(), entr2.get(), entr3.get()]))
    entr3.insert(0, '00-00-00')
    def check(what):
        xxx = True
        if what == 'focusin' and entr3.get() == '00-00-00':
            entr3.delete(0, 'end')
            entr3.configure(validate='all')
        elif what == 'focusout' and entr3.get() == '':
            entr3.delete(0, 'end')
            entr3.insert(0, '00-00-00')
            entr3.configure(validate='all')
        return xxx
    entr3.configure(validatecommand=(entr3.register(check), '%V'))
    #Расположение элементов
    but.grid(row=3, column=0, pady=10, padx=20, columnspan=2)
    entr1.grid(row=0, column=1, pady=1)
    entr2.grid(row=1, column=1, pady=1)
    entr3.grid(row=2, column=1, pady=1)
    label1.grid(row=0, column=0, pady=1, padx=5)
    label2.grid(row=1, column=0, pady=1, padx=5)
    label3.grid(row=2, column=0, pady=1, padx=5)
    if x != 1 and len(tree.selection()) != 1:
        root4.destroy()
        mb.showerror('Ошибка', 'Для редактирования записи надо выбрать одну запись')
    elif x != 1:
        num = int(tree.selection()[0])
        entr1.delete(0, tk.END)
        entr1.insert(0, base[1].loc[num]['Школа'])
        entr2.delete(0, tk.END)
        entr2.insert(0, base[1].loc[num]['Врач'])
        entr3.delete(0, tk.END)
        entr3.insert(0, base[1].loc[num]['Номер телефона школы'])
        but['command'] = lambda: edit_school(root4, tree, base,
                                             [entr1.get(), entr2.get(), entr3.get()], num)

def edit_student(root, tree, base, info, num):
    '''
    Редактирование студента
    '''
    root.destroy()
    if '' in info:
        mb.showinfo('Предупреждение', 'Запись не будет изменена, одно из полей пустое')
    else:
        if not functions.is_date(info[2]):
            mb.showinfo('Предупреждение', 'Запись не будет изменена, неверный формат даты')
        elif (info[0], info[1]) in map(tuple, list(base[2][["Ученик", "Школа"]].drop(num).values)):
            mb.showinfo('Предупреждение',
                        'Запись не будет изменена, так как уже есть такой ученик')
        else:
            ind = (base[0]['Ученик'] == base[2].loc[num][0]) & (base[0]['Школа'] == base[2].loc[num][1])
            for i in base[0][ind].index:
                base[0].loc[i, 'Ученик'] = info[0]
                base[0].loc[i, 'Школа'] = info[1]
            base[2].loc[num, 'Ученик'] = info[0]
            base[2].loc[num, 'Школа'] = info[1]
            base[2].loc[num, 'Дата рождения'] = info[2]
            children = tree.get_children()
            for i in children:
                tree.delete(i)
            i = iter(base[2].index)
            for item in base[2].values:
                tree.insert('', 'end', next(i), values=list(item))
            base[3] = merging(base[0], base[1], base[2])

def dob_student(root, x, tree, database):
    """
    Функция dob_student создаёт окно добавления записей для таблицы "Ученики"
    @author: Кретова Анна
    """
    #Создание окна
    root4 = tk.Toplevel(root)
    if x == 1:
        root4.title("Добавление новой записи")
    else:
        root4.title("Изменение записи")
    root4.geometry('450x145+350+200')
    root4.resizable(False, False)
    root4.configure(bg=cfon)

    #Ввод текста
    entr1 = tk.Entry(root4, font=tah, width=33)
    entr3 = tk.Entry(root4, validate='all')
    entr3.insert(0, 'ДД.ММ.ГГГГ')
    def check(what):
        xxx = True
        if what == 'focusin' and entr3.get() == 'ДД.ММ.ГГГГ':
            entr3.delete(0, 'end')
            entr3.configure(validate='all')
        elif what == 'focusout' and entr3.get() == '':
            entr3.delete(0, 'end')
            entr3.insert(0, 'ДД.ММ.ГГГГ')
            entr3.configure(validate='all')
        return xxx
    entr3.configure(validatecommand=(entr3.register(check), '%V'))
    #Раскрывающийся список
    combobox1 = ttk.Combobox(root4, state='readonly', width=31, font=tah)
    combobox1['values'] = list(database[1]['Школа'].values)
    if list(database[1]['Школа'].values):
        combobox1.current(0)

    #Текст
    label1 = tk.Label(root4, text='Ученик', bg=cfon, fg="White", bd=3,
                      font=tah)
    label2 = tk.Label(root4, text='Школа', bg=cfon, fg="White", bd=3,
                      font=tah)
    label3 = tk.Label(root4, text='Дата рождения', bg=cfon, fg="White", bd=3,
                      font=tah)

    #Кнопка
    but = tk.Button(root4, text="Ок", bg=cknop, fg="Black", bd=3,
                    font=tah, width=10, height=1)
    but['command'] = lambda: add_items(root4, tree, database, 2,
                                       [entr1.get(), combobox1.get(),
                                        '' if entr3.get() == 'ДД.ММ.ГГГГ' else entr3.get()])
    #Расположение элементов
    but.grid(row=3, column=0, pady=10, padx=20, columnspan=2)
    entr1.grid(row=0, column=1, pady=1)
    combobox1.grid(row=1, column=1, pady=1)
    entr3.grid(row=2, column=1, pady=1)
    label1.grid(row=0, column=0, pady=1, padx=5)
    label2.grid(row=1, column=0, pady=1, padx=5)
    label3.grid(row=2, column=0, pady=1, padx=5)
    if x != 1 and len(tree.selection()) != 1:
        root4.destroy()
        mb.showerror('Ошибка', 'Для редактирования записи надо выбрать одну запись')
    elif x != 1:
        num = int(tree.selection()[0])
        entr1.delete(0, tk.END)
        entr1.insert(0, database[2].loc[num]['Ученик'])
        combobox1.set(database[2].loc[num]['Школа'])
        entr3.delete(0, tk.END)
        entr3.insert(0, database[2].loc[num]['Дата рождения'])
        but['command'] = lambda: edit_student(root4, tree, database,
                                              [entr1.get(), combobox1.get(),
                                               '' if entr3.get() == 'ДД.ММ.ГГГГ' else entr3.get()],
                                              num)

def vibor(notebook1, notebook2):
    """
    Функция vibor перемещает выбранные столбцы из notebook1 в notebook2
    @author: Кретова Анна
    """
    if notebook1.curselection():
        str_num = notebook1.curselection()[0]
        stroka = notebook1.get(str_num)
        notebook2.insert('end', stroka)
        notebook1.delete(str_num)

def vibor2(notebook1, notebook2):
    """
    Функция vibor перемещает выбранные столбцы из notebook2 в notebook1
    @author: Кретова Анна
    """
    if notebook2.curselection():
        str_num = notebook2.curselection()[0]
        stroka = notebook2.get(str_num)
        notebook1.insert('end', stroka)
        notebook2.delete(str_num)

def create_PTO(notebook2):
    """
    Функция create_PTO создаёт окно простого текстого отчёта
    """
    #Создание окна
    root = tk.Toplevel()
    root.title("Простой текстовый отчёт")
    root.geometry('585x205+300+220')
    root.resizable(False, False)
    root.configure(bg=cfon)


    if True:
        VAL2 = list(notebook2.get(0, 8))
        combobox1 = ttk.Combobox(root, state='readonly', values=VAL2, width=20, font=tah)
        combobox1.set('')
        combobox2 = ttk.Combobox(root, state='readonly',
                                 values=['равно', 'не равно', 'больше или равно', 'больше',
                                         'меньше или равно', 'меньше'], width=20, font=tah)
        combobox2.set('')
    
        entr1 = tk.Entry(root, font=tah, width=20)
        combobox1.place(x=10, y=5)
        combobox2.place(x=210, y=5)
        entr1.place(x=410, y=5)
    
        combobox3 = ttk.Combobox(root, state='readonly', values=VAL2, width=20, font=tah)
        combobox3.set('')
        combobox4 = ttk.Combobox(root, state='readonly',
                                 values=['равно', 'не равно', 'больше или равно', 'больше',
                                         'меньше или равно', 'меньше'], width=20, font=tah)
        combobox4.set('')
        entr2 = tk.Entry(root, font=tah, width=20)
        combobox3.place(x=10, y=65)
        combobox4.place(x=210, y=65)
        entr2.place(x=410, y=65)
    
        combobox5 = ttk.Combobox(root, state='readonly', values=VAL2, width=20, font=tah)
        combobox5.set('')
        combobox6 = ttk.Combobox(root, state='readonly',
                                 values=['равно', 'не равно', 'больше или равно', 'больше',
                                         'меньше или равно', 'меньше'], width=20, font=tah)
        combobox6.set('')
        entr3 = tk.Entry(root, font=tah, width=20)
        combobox5.place(x=10, y=125)
        combobox6.place(x=210, y=125)
        entr3.place(x=410, y=125)
        tk.Button(root, text="Сформировать отчёт", bg=cknop, fg="Black", bd=3,
                  font=tah).place(x=225, y=160)
        #Флажок
        var1 = tk.IntVar()
        var1 = 1
        tk.Radiobutton(root, variable=var1, value=6, bg=cfon, activebackground=cfon).place(x=340, y=35)
        radio = tk.Radiobutton(root, variable=var1, value=5, bg=cfon, activebackground=cfon)
        radio.place(x=260, y=35)
        radio.select()
        tk.Label(root, text='И', bg=cfon, fg="White",
                 font=tah).place(x=240, y=35)
        tk.Label(root, text='ИЛИ', bg=cfon, fg="White",
                 font=tah).place(x=300, y=35)
        var2 = tk.IntVar()
        var2 = 3
        tk.Radiobutton(root, variable=var2, value=4, bg=cfon, activebackground=cfon).place(x=340, y=95)
        radio = tk.Radiobutton(root, variable=var2, value=3, bg=cfon, activebackground=cfon)
        radio.place(x=260, y=95)
        radio.select()
        tk.Label(root, text='И', bg=cfon, fg="White",
                 font=tah).place(x=240, y=95)
        tk.Label(root, text='ИЛИ', bg=cfon, fg="White",
                 font=tah).place(x=300, y=95)

def analiz(combobox, notebook2):
    """
    Функция analiz создаёт окно анализа таблицы
    @author: Кретова Анна
    """
    if combobox.get() == 'Простой текстовый отчёт':
        create_PTO(notebook2)
    elif ((combobox.get() == 'Текстовый статистический отчёт') or
          (combobox.get() == 'Сводная таблица')):
        #Создание окна
        root5 = tk.Toplevel()
        root5.title("Текстовый отчёт")
        root5.geometry('600x300+450+220')
        root5.resizable(False, False)
        root5.configure(bg=cfon)

        tree = ttk.Treeview(root5, height=11, show='headings')
        tree['columns'] = ['student', 'school']
        tree.column('student', width=295, anchor=tk.CENTER)
        tree.column('school', width=296, anchor=tk.CENTER)
        tree.heading('student', text='Ученик')
        tree.heading('school', text='Школа')
        tree.grid(row=0, column=0, columnspan=2, sticky='nsew', padx=2)

        #Скроллбары
        scrollbar = tk.Scrollbar(root5, orient='horizontal', command=tree.xview)
        tree['xscrollcommand'] = scrollbar.set
        vscrollbar = tk.Scrollbar(root5, orient='vert', command=tree.yview)
        tree['yscrollcommand'] = vscrollbar.set
        vscrollbar.grid(row=0, column=1, sticky='nse')
        scrollbar.grid(row=0, column=0, sticky='sew')
        root5.rowconfigure(0, weight=1)
        root5.columnconfigure(0, weight=1)

        tk.Button(root5, text="Сохранить отчёт", bg=cknop, fg="Black", bd=3,
                  font=tah).grid(row=2, column=0, pady=10, padx=5, columnspan=2)
    else:
        #Создание окна
        root5 = tk.Toplevel()
        root5.title("Графический отчёт")
        root5.geometry('600x300+450+220')
        root5.resizable(False, False)
        root5.configure(bg=cfon)

        can = tk.Canvas(root5, width=600, height=240)
        can.grid(row=0, column=0)

        tk.Button(root5, text="Сохранить отчёт", bg=cknop, fg="Black", bd=3,
                  font=tah).grid(row=1, column=0, pady=10, padx=5)

def delete_items(tree, database, number):
    """
    Удаление строк
    """
    items = tree.selection()
    if not items:
        mb.showerror('Ошибка', 'Не выбрана ни одна запись')
    else:
        for item in items:
            tree.delete(item)
            if number == 1:
                ind = database[0]['Школа'] == database[1].loc[int(item)][0]
                database[0] = database[0].drop(database[0][ind].index)
                ind = database[2]['Школа'] == database[1].loc[int(item)][0]
                database[2] = database[2].drop(database[2][ind].index)
            elif number == 2:
                ind = (database[0]['Ученик'] == database[2].loc[int(item)][0]) & (database[0]['Школа'] == database[2].loc[int(item)][1])
                database[0] = database[0].drop(database[0][ind].index)
            elif number == 3:
                student = database[3]['Ученик'][int(item)]
                school = database[3]['Школа'][int(item)]
                date = database[3]['Дата приёма'][int(item)]
                if student == '—':
                    ind = database[1]['Школа'] == school
                    database[1] = database[1].drop(database[1][ind].index)
                elif date == '—':
                    ind = (database[2]['Ученик'] == student) & (database[2]['Школа'] == school)
                    database[2] = database[2].drop(database[2][ind].index)
                else:
                    ind = (database[0]['Ученик'] ==
                           student) & (database[0]['Школа'] == school) & (database[0]['Дата приёма'] ==
                                                                          date)
                    database[0] = database[0].drop(database[0][ind].index)
        database[number] = database[number].drop(map(int, items))
        database[3] = merging(database[0], database[1], database[2])
        children = tree.get_children()
        for i in children:
            tree.delete(i)
        i = iter(database[number].index)
        for item in database[number].values:
            tree.insert('', 'end', next(i), values=list(item))

def add_schools(tree, database, info):
    '''
    Добавление школы
    '''
    if info[0] in database[1]['Школа'].values:
        mb.showinfo('Предупреждение', 'Запись не будет добавлена, так как уже есть такая школа')
    elif not functions.is_phone(info[2]):
        mb.showinfo('Предупреждение', 'Запись не будет добавлена. Неверный формат телефона')
    elif info[2] in database[1]['Номер телефона школы'].values:
        mb.showinfo('Предупреждение',
                    'Запись не будет добавлена, так как у разных школ различные телефоны')
    else:
        info = {'Школа': info[0], 'Врач': info[1], 'Номер телефона школы': info[2]}
        info = pd.Series(info)
        database[1] = database[1].append(info, ignore_index=True)
        database[3] = merging(database[0], database[1], database[2])
        children = tree.get_children()
        for i in children:
            tree.delete(i)
        i = iter(database[1].index)
        for item in database[1].values:
            tree.insert('', 'end', next(i), values=list(item))

def add_students(tree, database, info):
    '''
    Добавление ученика
    '''
    if not functions.is_date(info[2]):
        mb.showinfo('Предупреждение', 'Запись не будет добавлена, неверный формат даты')
    elif (info[0], info[1]) in map(tuple, list(database[2][["Ученик", "Школа"]].values)):
        mb.showinfo('Предупреждение',
                    'Запись не будет добавлена, так как уже есть такой ученик')
    else:
        info = {'Ученик': info[0], 'Школа': info[1], 'Дата рождения': info[2]}
        info = pd.Series(info)
        database[2] = database[2].append(info, ignore_index=True)
        database[3] = merging(database[0], database[1], database[2])
        children = tree.get_children()
        for i in children:
            tree.delete(i)
        i = iter(database[2].index)
        for item in database[2].values:
            tree.insert('', 'end', next(i), values=list(item))

def add_analyses(tree, database, info):
    '''
    Добавление анализов
    '''
    if not functions.is_date(info[2]):
        mb.showinfo('Предупреждение', 'Запись не будет добавлена, неверный формат даты')
    elif info[3] <= 0 or info[4] <= 0:
        mb.showinfo('Предупреждение', 'Запись не будет добавлена, неверное значение анализов')
    elif (info[0], info[1]) not in map(tuple, list(database[2][["Ученик", "Школа"]].values)):
        mb.showinfo('Предупреждение', 'Запись не будет добавлена, нет такого ученика')
    elif (info[0], info[1], info[2]) in map(tuple, list(database[0][["Ученик", "Школа",
                                                                     "Дата приёма"]].values)):
        mb.showinfo('Предупреждение',
                    'Запись не будет добавлена, эта информация уже есть в базе данных')
    else:
        info = {'Ученик': info[0], 'Школа': info[1], 'Дата приёма': info[2],
                'Глюкоза, ммоль/л': info[3], 'Инсулин, мкЕд/мл': info[4],
                'Прививка от гриппа': info[5]}
        info = pd.Series(info)
        database[0] = database[0].append(info, ignore_index=True)
        database[3] = merging(database[0], database[1], database[2])
        children = tree.get_children()
        for i in children:
            tree.delete(i)
        i = iter(database[0].index)
        for item in database[0].values:
            tree.insert('', 'end', next(i), values=list(item))

def add_items(root, tree, database, number, info):
    """
    Добавление сущности
    """
    root.destroy()
    if '' in info:
        mb.showinfo('Предупреждение', 'Запись не будет добавлена, так как одно из полей пустое')
    elif number == 1:
        add_schools(tree, database, info)
    elif number == 2:
        add_students(tree, database, info)
    elif number == 0:
        add_analyses(tree, database, info)
    database[3] = merging(database[0], database[1], database[2])

def knopki(root, combobox, base, notebook2):
    """
    Функция knopki создаёт кнопки и таблицу на главном окне
    @author: Кретова Анна
    """
    def func1(func, param):
        table0 = base[param]
        func([but4, but5, but6, but7], tree, table0)
        if param < 3:
            but2['command'] = lambda: (dob_analyzes, dob_school,
                                       dob_student)[param](root, 1, tree, base)
            but3['command'] = lambda: (dob_analyzes, dob_school,
                                       dob_student)[param](root, 0, tree, base)
        else:
            but2['command'] = lambda: mb.showinfo('Предупреждение', 'В полную таблицу нельзя добавлять данные. Пользуйтесь другими таблицами для добавления')
            but3['command'] = lambda: mb.showinfo('Предупреждение', 'В полной таблице нельзя делать изменения. Пользуйтесь другими таблицами для редактирования')

    def analiz1():
        analiz(combobox, notebook2)

    #Кнопки
    but1 = tk.Button(root, text="Удалить выбранные записи", bg=cknop, fg="Black", bd=3,
                     font=tah,
                     command=lambda: delete_items(tree, base, color(but4, but5, but6) - 1))
    but2 = tk.Button(root, text="Добавить запись", bg=cknop, fg="Black", bd=3,
                     font=tah)
    but3 = tk.Button(root, text="Редактировать запись", bg=cknop, fg="Black", bd=3,
                     font=tah)
    but4 = tk.Button(root, text="Анализы", bg=cknop, fg="Black", bd=3,
                     font=tah, command=lambda: func1(table_analyzes, 0))
    but5 = tk.Button(root, text="Школа", bg=cknop, fg="Black", bd=3,
                     font=tah, command=lambda: func1(table_school, 1))
    but6 = tk.Button(root, text="Ученики", bg=cknop, fg="Black", bd=3,
                     font=tah, command=lambda: func1(table_students, 2))
    but7 = tk.Button(root, text="Полный список", bg=cknop, fg="Black", bd=3,
                     font=tah, command=lambda: func1(table, 3))
    but8 = tk.Button(root, text="Проанализировать", bg=cknop, fg="Black", bd=3,
                     font=tah, command=analiz1)
    but1.grid(row=0, column=0, columnspan=4, pady=1)
    but2.grid(row=1, column=0, columnspan=4, pady=1)
    but3.grid(row=2, column=0, columnspan=4, pady=1)
    but4.grid(row=3, column=0, padx=2, pady=20)
    but5.grid(row=3, column=1, padx=1)
    but6.grid(row=3, column=2, padx=1)
    but7.grid(row=3, column=3, padx=1)
    but8.grid(row=2, column=5, columnspan=4, padx=25)
    #Таблица
    tree = ttk.Treeview(root, selectmode="extended", height=20, show='headings')
    func1(table_analyzes, 0)
    return [but4, but5, but6, but7, tree]

def system_error(root):
    """
    Ошибка версии Python/ОС
    """
    mb.showerror('Ошибка', 'Приложение не может быть запущено в данной системе')
    root.destroy()
    sys.exit()

def main_window():
    """
    Функция main_window создаёт главное окно
    @author: Кретова Анна
    """
    def vibor_1(ev):
        if str(ev.type) == 'ButtonPress':
            vibor(notebook1, notebook2)
    def vibor_2(ev):
        if str(ev.type) == 'ButtonPress':
            vibor2(notebook1, notebook2)

    #Создание окна
    root = tk.Tk()
    root.title("Главное окно")
    root.geometry('1135x610+60+10')
    root.resizable(False, False)
    root.configure(bg=cfon)
    #if not functions.check_system():
    #    system_error(root)
    temp = functions.load_base(os.path.join(os.getcwd(), 'Data','database.pickle'))
    columns = [('Ученик', 'Школа', 'Дата рождения'),
               ('Ученик', 'Школа', 'Дата приёма', 'Глюкоза, ммоль/л',
                'Инсулин, мкЕд/мл', 'Прививка от гриппа'),
               ('Школа', 'Врач', 'Номер телефона школы')]
    analyses = pd.DataFrame(columns=columns[1])
    schools = pd.DataFrame(columns=columns[2])
    students = pd.DataFrame(columns=columns[0])
    if temp['error'] == 1:
        mb.showerror('Ошибка', 'Не удалось загрузить базу данных')
    elif temp['error'] == 2:
        mb.showerror('Ошибка', 'Неожиданное содержимое базы данных')
    else:
        analyses = temp['base'][0]
        schools = temp['base'][1]
        students = temp['base'][2]
    all_tables = merging(analyses, schools, students)
    base = [analyses, schools, students, all_tables]
    #Выбор столбцов
    notebook1 = tk.Listbox(root, height=9, width=23)
    columns = ('Ученик', 'Школа', 'Дата приёма', 'Глюкоза, ммоль/л',
               'Инсулин, мкЕд/мл', 'Прививка от гриппа', 'Номер телефона школы',
               'Врач', 'Дата рождения')
    for column in columns:
        notebook1.insert('end', column)
    notebook1.bind('<Double-1>', vibor_1)
    notebook2 = tk.Listbox(root, height=9, width=23, selectmode=tk.EXTENDED)
    notebook2.bind('<Double-1>', vibor_2)

    #Раскрывающийся список
    combobox = ttk.Combobox(root, state='readonly', width=42, font=tah)
    combobox['values'] = ['Простой текстовый отчёт', 'Текстовый статистический отчёт', \
            'Сводная таблица', 'Кластеризованная столбчатая диаграмма', \
            'Категоризированная гистограмма', 'Категоризированная диаграмма Бокса-Вискера', \
            'Категоризированная диаграмма рассеивания']
    combobox.set('Простой текстовый отчёт')

    #Кнопки
    buttons = knopki(root, combobox, base, notebook2)

    #Меню
    menu(root, base, buttons[:4], buttons[4])

    #Надписи
    tk.Label(root, text='Ваш выбор:', bg=cfon, fg="White", font=tah).grid(row=0, column=5, padx=20)
    tk.Label(root, text='Выберите столбцы:', bg=cfon, fg="White", font=tah).grid(row=0, column=4, padx=20)

    #Расположение элементов
    notebook1.grid(row=1, rowspan=3, column=4, padx=20)
    notebook2.grid(row=1, rowspan=3, column=5, padx=20)
    combobox.grid(row=1, column=6, columnspan=4)

    root.mainloop()

main_window()
sys.path.pop()
