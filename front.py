from tkinter import *
import back

def display_com():#connects display function to display_button 
    lb.delete(0,END)#clears listbox 
    for i in back.display():
        lb.insert(END,i)

def search_com():#connects search fucntion
    lb.delete(0,END)
    for i in back.search(e1_val.get(),e2_val.get(),e3_val.get(),e4_val.get()):
        lb.insert(END,i)

def add_com():
    back.insert(e1_val.get(),e2_val.get(),e3_val.get(),e4_val.get())
    lb.delete(0,END)
    lb.insert(END,(e1_val.get(),e2_val.get(),e3_val.get(),e4_val.get()))

def get_row(event):#to return selectd row in listbox
    try:
        global sel_tup
        index = lb.curselection()[0]#index of selected row
        sel_tup = lb.get(index)#tuple of that index
        e1.delete(0,END)          #to display selectd in entry box
        e1.insert(END,sel_tup[1])
        e2.delete(0,END)
        e2.insert(END,sel_tup[2])
        e3.delete(0,END)
        e3.insert(END,sel_tup[3])
        e4.delete(0,END)
        e4.insert(END,sel_tup[4])
        return(sel_tup)
    except IndexError:#for clicking on empty listbox
        pass

def del_com():
    back.dele(sel_tup[0])#paasing id to dele fucntion

def up_com():
    back.update(sel_tup[0],e1_val.get(),e2_val.get(),e3_val.get(),e4_val.get())#passing id and updated values


win = Tk()
win.title("Telephone directory")

#labels 
l1 = Label(win,text = "Name")
l1.grid(row = 0,column = 0,padx = 5)

l2 = Label(win,text = "Surname")
l2.grid(row = 0,column = 2,padx = 5)

l3 = Label(win,text = "Tele/Mobile")
l3.grid(row = 1,column = 2,padx = 5)

l4 = Label(win,text = "Residential")
l4.grid(row = 1,column = 0,padx = 5)

#Entry windows
e1_val = StringVar()
e1 = Entry(win,textvariable = e1_val,width = 25)
e1.grid(row = 0,column = 1)

e2_val = StringVar()
e2 = Entry(win,textvariable = e2_val,width = 25)
e2.grid(row = 0,column = 3)

e3_val = StringVar()
e3 = Entry(win,textvariable = e3_val,width = 25)
e3.grid(row = 1,column = 1)

e4_val = StringVar()
e4 = Entry(win,textvariable = e4_val,width = 25)
e4.grid(row = 1,column = 3)

#listbox
lb = Listbox(win,heigh = 12,width = 40)
lb.grid(row = 2,column = 0,rowspan = 6,columnspan = 2)

#Scrollbars
sb1 = Scrollbar(win)
sb2 = Scrollbar(win,orient = 'horizontal')
sb1.grid(row = 2,column =2,rowspan = 6)
sb2.grid(row = 8,column = 0,columnspan = 2)

#assigning scroll bars to listbox
lb.configure(xscrollcommand = sb2.set)
sb2.configure(command = lb.xview)

lb.configure(yscrollcommand = sb1.set)
sb1.configure(command = lb.yview)

#binds selected row of listbox
lb.bind('<<ListboxSelect>>',get_row)

#Buttons
b1 = Button(win,text = "Veiw All",width = 15,command = display_com)
b1.grid(row = 2,column =3,pady = 5)

b2 = Button(win,text = "Search",width = 15,command = search_com)
b2.grid(row = 3,column =3,pady = 5)

b3 = Button(win,text = "Add",width = 15,command = add_com)
b3.grid(row = 4,column =3,pady = 5)

b4 = Button(win,text = "Update Selected",width = 15,command = up_com)
b4.grid(row = 5,column =3,pady = 5)

b5 = Button(win,text = "Delete Selected",width = 15,command = del_com)
b5.grid(row = 6,column =3,pady = 5)

b6 = Button(win,text = "Close",width = 15,command = win.destroy)
b6.grid(row = 7,column =3,pady = 5)

win.mainloop()