import tkinter as t 
from tkinter import ttk

window=t.Tk()
window.title('WWII Battles')


def safc():
   T.insert("Battle of Moscow",[0])

Moskau=ttk.Button(text='Battle of Moscow',command=safc)
Battle=ttk.Entry(state="readonly")
l=ttk.Label(text="Battle")


T=t.Entry(state="readonly")
Moskau.grid(row=4, column=1)
l.grid(row=2,column=1)
Battle.grid(row=2,column=2)
#Battle.grid(row=2,column=2)



window.mainloop()