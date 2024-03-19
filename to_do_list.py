from tkinter import *
from tkinter import ttk
from tkinter import messagebox
m=Tk()
def Add():
    try:
        k=e.get()
        if (k==''):
            print(k/0)
        treeview.insert("",'end',text=k)
        e.delete(0, 'end')
    except:
        messagebox.showinfo("Enter something")
def Delete():
    try:
        selection=treeview.selection()[0]
        treeview.delete(selection)
    except:
        messagebox.showinfo("Select something to delete")

m.geometry('800x500')
treeview=ttk.Treeview(m,height=15,xscrollcommand=True,yscrollcommand=True,selectmode='browse')
treeview.pack()
b1=Button(m,text='ADD',font=('Arial Black',10),bg='white',command=Add)
b1.place(x=300,y=350)
b2=Button(m,text='Delete',font=('Arial Black',10),bg='white',command=Delete)
b2.place(x=430,y=350)

e=Entry(m,width=33)
e.focus()
e.place(x=298,y=330)
m.mainloop()