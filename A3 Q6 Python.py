import tkinter as tk
from tkinter import ttk
import sqlite3
con=sqlite3.connect('Sales Company.db')
cur=con.cursor()

def getResults():
    ee=cur.execute("Select amount,ID from Sales where salesDate= ? and region=?",(ent.get(),ent2.get()))
    Result= ee.fetchone()  
    if Result is not None:
        AmountVar.set(str(Result[0])) 
        IdVar.set(str(Result[1]))
    else:
        AmountVar.set("") 
        IdVar.set("")
        Popup=tk.Toplevel(window)
        Popup.geometry("250x250")
        tk.Label(Popup,text="No Data").pack(padx=20,pady=100)
        

def SaveAmount():
    if IdVar.get() and AmountVar.get():
        cur.execute("update sales set Amount=? where id=?",(AmountVar.get(),IdVar.get()))
        con.commit()

    
def wompwomp():
    window.destroy()  

window=tk.Tk()
Label=tk.Label(text="Enter date and region to get sales amount.")
dateLabel=tk.Label(text="Date: ")
ent=tk.Entry()
regionLabel=tk.Label(text="Region: ")
ent2=tk.Entry()
amountLable=tk.Label(text="Amount: ")
AmountVar=tk.StringVar()
IdVar=tk.StringVar()
ent3=tk.Entry(textvariable=AmountVar)
idLabel=tk.Label(text="ID: ")
ent4=tk.Entry(state="readonly",textvariable=IdVar)


Amount=tk.Button(text="Get Amount",command=getResults)
Save=tk.Button(text="Save Changes",command=SaveAmount)
Exit=tk.Button(text="Exit",width=12,pady=4,command=wompwomp)
Label.grid(row=0,column=0)
dateLabel.grid(row=1,column=0)
ent.grid(row=1,column=1)
regionLabel.grid(row=2,column=0)
ent2.grid(row=2,column=1)
amountLable.grid(row=3,column=0)
ent3.grid(row=3,column=1)
idLabel.grid(row=4,column=0)
ent4.grid(row=4,column=1)

Amount.grid(row=2,column=2)
Save.grid(row=5, column=0)
Exit.grid(row=5, column=1)


  

window.mainloop()