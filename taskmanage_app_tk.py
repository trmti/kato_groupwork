import tkinter as tk
from taskmanager import *

win = tk.Tk()
win.title('taskmanager')
win.geometry('500x250')
#--------------label-------------------
label = tk.Label(win, text='タスク')
label.pack()

label_2 = tk.Label(win, text='|やることリスト|',font=("",15))
label_2.place(x=10,y=70)

#--------------label-------------------
text = tk.Entry(win)
text.pack()

def ok_click():
    s = text.get()
    t = todo(s)
    label = tk.Label(win, text=list(), anchor='w')
    label.pack()

Button = tk.Button(win, text=u"新規追加", command=ok_click)
Button.pack()
win.mainloop()
