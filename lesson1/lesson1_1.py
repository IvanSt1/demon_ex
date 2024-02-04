import tkinter as tk
'''
программа считающая количество нажатий кнопки
'''
count=[0]
def on_button_click():
    count[0]+=1
    labl_count_clicks.config(text=f'Сделали нажатие {count[0]}')
    print('Кнопку нажали')

root = tk.Tk() # созданиее главное окна
root.title('Первая попытка в Tkinter') # метод title задает название для окна
root.geometry('500x600') # задает изначальный размер

# Создаем текст 
text=tk.Label(root,text='Hello World!')
text.pack()
text1=tk.Label(root,text='Hello 123')
text1.pack()
text2=tk.Label(root,text='Hello 542')
text2.pack()

# Создаем кнопку
btn=tk.Button(root,text='Нажми на меня',command=on_button_click)
btn.pack()

labl_count_clicks=tk.Label(root,text='Ничего не нажали')
labl_count_clicks.pack()

root.mainloop()