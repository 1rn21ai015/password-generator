from tkinter import *
from tkinter import ttk
import random , string

root=Tk()
root.geometry("400x280")
root.title("password Genrertor")

#intro text
title =StringVar()
Label=Label(root,textvariable=title).pack()
title.set("The Stength of Password :")

def selection():
    selection=choice.get()

choice =IntVar()
R1=Radiobutton(root,text="POOR",varible=choice,value=1,command= selection).pack(anchor=CENTER)
R1=Radiobutton(root,text="AVERAGE",varible=choice,value=2,command= selection).pack(anchor=CENTER)
R1=Radiobutton(root,text="ADVANCED",varible=choice,value=3,command= selection).pack(anchor=CENTER)
labelchoice=Label(root)
labelchoice.pack()

lenlable = StringVar()
lenlable.set("password length")
lentitle=Label(root,textvariable=lenlable).pack()

val =IntVar()
spinlenght=Spinbox(root, from_=8, to_=24, textvariable=val, width=13).pack()

def callback():
    lsum.config(text=passgen())

passgenButton=Button(root, text="Generate Password", bd=5,height=2,command=callback,pady=3)
passgenButton.pack()
password=str(callback)

lsum=Label(root, text="")
lsum.pack(side=BOTTOM)

#logic
poor=string.ascii_uppercase+string.ascii_lowercase
average=string.ascii_lowercase+string.ascii_uppercase+string.digits
symbols="""`~!@#%^&*()_-+={}\|[];:'"<>,.?/"""
advance=poor+average+symbols

def passgen():
    if choice.get()==1:
        return "".join(random.sample(poor,val.get()))
    elif choice.get()==2:
         return "".join(random.sample(average,val.get()))
    elif choice.get()==2:
         return "".join(random.sample(advance,val.get()))
    
    
    
