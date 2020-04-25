# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 11:22:40 2020

@author: Чашкин Леонид
"""
import tkinter as tk
from tkinter import ttk

"""
Функция изменения цвета кнопок
"""
def clck(all_buttons):
	all_buttons[0].config(bg = 'yellow')
	for i in range(1, len(all_buttons)):
		all_buttons[i].config(bg = 'SystemButtonFace')

"""
Функция main_window - создаёт главное окно
Автор: Чашкин Л.
"""
def main_window():
    root = tk.Tk() #Создание окна, называется root
    root.title('Главное окно') #Название окна
    root.geometry('682x638+52+52')
    root.minsize(682,638) #Минимальные размеры окна
    
    #Меню
    menu = tk.Menu(root)
    submenu = tk.Menu(menu, tearoff = 0)
    submenu.add_checkbutton(label = 'Сортировка')
    menu.add_cascade(label = 'Вид', menu = submenu)
    menu.add_command(label = 'Настройки')
    root.config(menu = menu)
    
    #Текст
    label1 = tk.Label(root, text = 'Операции над базой данных') 
    label2 = tk.Label(root, text = 'Анализ') 
    label3 = tk.Label(root, text = 'Выбранные поля')
    
    #Кнопки
    button1 = tk.Button(root, text = 'Удалить выбранные записи')
    button2 = tk.Button(root, text = 'Добавить запись')
    button3 = tk.Button(root, text = 'Редактировать запись')
    button4 = tk.Button(root, text = 'Сохранить базу данных')
    button5 = tk.Button(root, text = 'Загрузить базу данных')
    button6 = tk.Button(root, text = 'Сформировать отчёт')
    table_analiz = tk.Button(root, text = 'Анализы')
    table_analiz['command'] = lambda: clck((table_analiz, table_schools, table_students, all_tables))
    table_schools = tk.Button(root, text = 'Школа', bg = "yellow")
    table_schools['command'] = lambda: clck((table_schools, table_analiz, table_students, all_tables))
    table_students = tk.Button(root, text = 'Ученики')
    table_students['command'] = lambda: clck((table_students, table_analiz, table_schools, all_tables))
    all_tables = tk.Button(root, text = 'Полный список')
    all_tables['command'] = lambda: clck((all_tables, table_students, table_analiz, table_schools))
    
    #Таблица
    tree = ttk.Treeview(root, columns = ('school', 'doctor', 'phone'), selectmode = "browse", height = 20, show = 'headings')
    tree.heading('school', text = 'Школа')
    tree.heading('doctor', text = 'Врач')
    tree.heading('phone', text = 'Телефон')
    tree.insert('', 'end', values = ['Школа 1', 'Иванова', '123'])
    tree.insert('', 'end', values = ['Школа 1', 'Иванова', '123'])
    tree.insert('', 'end', values = ['Школа 1', 'Иванова', '123'])
    tree.insert('', 'end', values = ['Школа 1', 'Иванова', '123'])
    tree.insert('', 'end', values = ['Школа 1', 'Иванова', '123'])
    
    #Раскрывающийся список
    listbox = ttk.Combobox(root, state = 'readonly', width = 45)
    listbox['values'] = ['Простой текстовый отчёт', 'Текстовый статистический отчёт', 'Сводная таблица', \
    'Кластеризованная столбчатая диаграмма', 'Категоризированная гистограмма', 'Категоризированная диаграмма Бокса-Вискера', \
    'Категоризированная диаграмма рассеивания']
    listbox.current(0)
    
    #Текстовое поле
    notebook = tk.Listbox(root)
    notebook.insert('end', 'Школа')
    notebook.insert('end', 'Врач')
    notebook.insert('end', 'Телефон')
    notebook.configure(state = 'disabled')
    
    #Положение элементов, row - строка, column - столбец, columnspan - объединение строк, rowspan - объединение столбцов
    label1.grid(row = 0, column = 0, columnspan = 4) 
    label2.grid(row = 0, column = 4, columnspan = 2)
    button1.grid(row = 1, column = 0, columnspan = 4)
    button2.grid(row = 2, column = 0, columnspan = 4)
    button3.grid(row = 3, column = 0, columnspan = 4)
    button4.grid(row = 4, column = 0, columnspan = 4)
    button5.grid(row = 5, column = 0, columnspan = 4)
    button6.grid(row = 4, column = 5)
    table_analiz.grid(row = 6, column = 0)
    table_schools.grid(row = 6, column = 1)
    table_students.grid(row = 6, column = 2)
    all_tables.grid(row = 6, column = 3)
    tree.grid(row = 7, column = 0, columnspan = 6, sticky = 'nsew')
    listbox.grid(row = 3, column = 5) 
    label3.grid(row = 1, column = 4)
    notebook.grid(row = 2, column = 4, rowspan = 5)
    
    #Настройки расширения элементов (элементы должны расширяться вместе с окном)
    for i in range(8):
        root.rowconfigure(i, weight=1)
    for i in range(6):
        root.columnconfigure(i, weight=1)
    
    #Запуск приложения
    root.mainloop()
	
main_window()
