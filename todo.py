#=================================================importing required packages=============================================
from tkinter import*

#=================================================defining root(window) layout============================================
root=Tk()
root.geometry("450x620+450+50")
root.resizable(False,False)
root.title("To Do List:By Samiksha Mishra")
root.iconbitmap("1.ico")
root.configure(bg="deep sky blue2",border=10,relief=RIDGE)

#===================================defining function for giving placeholder in entry widget==============================
def focusin(event):
    if input.get() == "Enter Task":
        input.delete(0, END)
        input.config(fg='black',font="verdana 15 bold",justify=RIGHT,bg="gold")

def focusout(event):
    if input.get() == "":
        input.insert(0, "Enter Task")
        input.config(fg='grey',font="verdana 15 bold",justify=CENTER,bg="gold")

#===============================================defining function for add button==========================================
def add(event):
    global task
    if task.get()=="Enter Task":
        pass
    else:
        t=str(task.get())
        lbx.insert(END,f"{t}")                                #inserting in the listbox
        with open('task.txt','a') as task_file:               #opening a text file in append mode and writing the task into it
            t=t+"\n"
            task_file.write(t)
            task_file.seek(0)
            task_file.close()
        input.delete(0,END)                                   #clearing the entry widget for next entry
    
#============================================defining function for delete button==========================================
def delete(event):
    selected_index = lbx.curselection()
    if selected_index:
        lbx.delete(selected_index)
        with open('task.txt', 'r') as task_file:
            lines = task_file.readlines()
        with open('task.txt', 'w') as task_file:
            for i, line in enumerate(lines):
                if i != selected_index[0]:
                    task_file.write(line)

def delete_all(lbx):
    total = lbx.size()
    lbx.delete(0, total - 1)
    with open('task.txt', 'w'):
        pass

#======================defining function for displaying the data that is previously stored ===============================
def load_tasks():
    try:
        with open('task.txt', 'r') as task_file:
            tasks = task_file.readlines()
            for task in tasks:
                lbx.insert(END, task.strip())
    except FileNotFoundError:
        pass


#======================================defining variable name and its data type===========================================
task=StringVar()

#====================================making a frame to place all the widgets inside it====================================
main_frame=Frame(root,background="white")

#====================================inserting a .png image at the top position of frame==================================
photo=PhotoImage(file="To Do.png")
top=Label(main_frame,image=photo)
top.grid(column=0,row=0,columnspan=4)

#=======================================================Entry widget======================================================
input=Entry(main_frame,textvariable=task,width=24,fg="grey",font="verdana 15 bold",justify=CENTER,bg="gold",border=5,relief=SUNKEN)
entry_placeholder = "Enter Task"
input.insert(0, entry_placeholder)                                 #displaying the placeholder text
input.bind("<FocusIn>", focusin)                                   #placeholder text disappears when clicked to give input
input.bind("<FocusOut>", focusout)                                 #placeholder text appears when focus out
input.grid(row=1,column=0,columnspan=4,pady=20)

#==================================================Add Task Button widget=================================================
add_btn=Button(main_frame,text="ADD TASK",height=1,width=20,bg="green3",fg="white",font="system 10 bold",border=5,relief=RAISED,cursor="hand2")
add_btn.bind("<Button-1>",add)
add_btn.grid(row=2,column=0,columnspan=2,padx=5)

#================================================Delete Task Button widget================================================
del_btn=Button(main_frame,text="DELETE TASK",height=1,width=20,bg="red1",fg="white",font="system 10 bold",border=5,relief=RAISED,cursor="hand2")
del_btn.bind("<Button-1>",delete)
del_btn.grid(row=2,column=2,columnspan=2,padx=5)

del_all_btn=Button(main_frame,text="DELETE ALL",height=1,width=20,bg="red1",fg="white",font="system 10 bold",border=5,relief=RAISED,cursor="hand2",command=lambda: delete_all(lbx),padx=95)
del_all_btn.grid(row=3,column=0,columnspan=4,padx=5,pady=5)

#======================================================Listbox widget=====================================================
lbx=Listbox(main_frame,height=11,width=20,bg="deep sky blue2",relief=SUNKEN,border=5,font="verdana 16 bold")
lbx.grid(row=4,column=0,columnspan=3,pady=10,padx=10)

#================================================Vertical scroll bar  widget==============================================
vscrollbar = Scrollbar(main_frame, command=lbx.yview)
vscrollbar.grid(row=4, column=3, sticky='ns',pady=10,padx=10)
lbx.config(yscrollcommand=vscrollbar.set)

#===============================================Horizontal scroll bar  widget=============================================
hscrollbar = Scrollbar(main_frame, command=lbx.xview,orient="horizontal")
hscrollbar.grid(row=5, column=0,columnspan=4, sticky='we',padx=10)
lbx.config(xscrollcommand=hscrollbar.set)

load_tasks()                                     #function call to display previously added tasks that are not deleted yet
main_frame.grid(padx=25,pady=18)
root.mainloop()
#=====================================================END of mainloop=====================================================