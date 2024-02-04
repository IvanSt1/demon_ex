import tkinter as tk
'''
простой вариант авторизации
'''
def on_button_click():
    if login.get()=='admin' and pswd.get()=='12345':
        label1.config(text='Удачная авторизация')
    else:
        label1.config(text='Неверный логин или пароль')

root = tk.Tk() # созданиее главное окна
root.title('Первая попытка в Tkinter') # метод title задает название для окна
root.geometry('500x600') # задает изначальный размер

login=tk.StringVar()
pswd=tk.StringVar()

login_lbl=tk.Label(root, text='Введите ваше имя:')
login_entry=tk.Entry(root,textvariable=login) # в переменную name сохраняется то что ввели

pswd_lbl=tk.Label(root, text='Введите ваше имя:')
pswd_entry=tk.Entry(root,textvariable=pswd) # в переменную name сохраняется то что ввели

btn=tk.Button(root,text='Подвердить', command=on_button_click)
label1=tk.Label(root,text='Ожидание ввода:')

login_lbl.pack()
login_entry.pack()
pswd_lbl.pack()
pswd_entry.pack()
btn.pack()
label1.pack()


root.mainloop()