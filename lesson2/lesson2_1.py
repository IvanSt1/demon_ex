
import csv
import tkinter as tk
from tkinter import ttk
class App:
    def __init__(self,root):
        self.root = root 
        self.root.title('Приложение') # метод title задает название для окна
        self.root.geometry('500x600') # задает изначальный размер
        self.frames={}
        self.init_login_frame()

    def init_login_frame(self):
        frame=tk.Frame(self.root)
        frame.pack(fill=tk.BOTH,expand=True)

        tk.Label(frame, text='Введите логин:').pack()
        self.login_entry=tk.Entry(frame) 
        self.login_entry.pack() 

        tk.Label(frame, text='Введите пароль:').pack()
        self.pswd_entry=tk.Entry(frame,show='*') # show заменяет все символы на то что указано
        self.pswd_entry.pack()

        tk.Button(frame,text='Подвердить', command=self.authenticate).pack()

        self.error_message=tk.Label(frame,text='Ожидание ввода:')
        self.error_message.pack()

        self.frames['логин']=frame

    def authenticate(self):
        login=self.login_entry.get()
        pswd=self.pswd_entry.get()
        with open('users.csv',mode='r',newline='',encoding='utf-8') as file:
            reader=csv.DictReader(file,delimiter=';')
            #проверка что такой логин и пароль есть в файлике а также что логин соответсвует номеру телефона (10 цифр)
            for row in reader:
                if login==row['Логин'] and pswd==row['Пароль'] and login.isdigit() and len(login)==10:  
                    self.user_role=row['Роль']
                    self.switching_frame(self.user_role.lower())

            self.error_message.config(text='Неверный ввод')

    def switching_frame(self,frame_name):
        for frame in self.frames.values():
            frame.pack_forget()
        if frame_name not in self.frames:
            if frame_name=='директор':
                self.init_director_frame()
            elif frame_name=='администратор':
                self.init_administrator_frame()
        self.frames[frame_name].pack(fill=tk.BOTH,expand=True)

    def init_director_frame(self):
        frame=tk.Frame(self.root)
        tk.Label(frame,text='ВЫ ДИРЕКТОР').pack()
        tk.Button(frame,text='Выйти',command= lambda : self.switching_frame('логин')).pack()
        self.frames['директор']=frame
    
    def init_administrator_frame(self):
        frame=tk.Frame(self.root)
        colums=['Логин','Имя пользователя','Роль']
        self.users_table=ttk.Treeview(frame,columns=colums,show='headings')
        for col in colums:
            self.users_table.heading(col,text=col)

        self.users_table.pack()
        self.update_users_table()

        tk.Button(frame,text='Выйти',command= lambda : self.switching_frame('логин')).pack()
        tk.Button(frame,text='Обновить',command= self.update_users_table).pack()
        self.frames['администратор']=frame

    def update_users_table(self):
        for el in self.users_table.get_children():
            self.users_table.delete(el)
        with open('users.csv',mode='r',newline='',encoding='utf-8') as file:
            reader=csv.DictReader(file,delimiter=';')
            for row in reader:
                self.users_table.insert('',tk.END,values=(row['Логин'],row['Имя пользователя'],row['Роль']))


if __name__=='__main__':
    root = tk.Tk()
    app=App(root)
    root.mainloop()