'''
работа с csv авторизация по данным из файла
'''
import csv



import tkinter as tk
'''
простой вариант авторизации
'''
def on_button_click():
    with open('users.csv',mode='r',newline='',encoding='utf-8') as file:
        reader=csv.DictReader(file,delimiter=';')
        #проверка что такой логин и пароль есть в файлике а также что логин соответсвует номеру телефона (10 цифр)
        if any(login.get()==row['Логин'] and pswd.get()==row['Пароль'] for row in reader) and login.get().isdigit() and len(login.get())==10:  
            label1.config(text='Удачная авторизация')
        else:
            label1.config(text='Неверный логин или пароль')

root = tk.Tk() # созданиее главное окна
root.title('Первая попытка в Tkinter') # метод title задает название для окна
root.geometry('500x600') # задает изначальный размер

login=tk.StringVar()
pswd=tk.StringVar()

login_lbl=tk.Label(root, text='Введите логин:')
login_entry=tk.Entry(root,textvariable=login) # 

pswd_lbl=tk.Label(root, text='Введите пароль:')
pswd_entry=tk.Entry(root,textvariable=pswd,show='*') # show заменяет все символы на то что указано

btn=tk.Button(root,text='Подвердить', command=on_button_click)
label1=tk.Label(root,text='Ожидание ввода:')

login_lbl.pack()
login_entry.pack()
pswd_lbl.pack()
pswd_entry.pack()
btn.pack()
label1.pack()
tk.Button(root,text='Выход',command=root.destroy).pack()

root.mainloop()
