#=================================================importing required packages=============================================
from tkinter import*
import time
#=================================================defining root(window) layout============================================
root=Tk()
root.geometry("450x570+400+80")
root.resizable(False,False)
root.title("Calculator:By Samiksha Mishra")
root.iconbitmap("2.ico")
root.configure(bg="Black",border=8,relief=RIDGE)

#================================================defining click() function================================================
def click(event):
    global scvalue
    text=event.widget.cget("text")
    if text=="=":
        if scvalue.get().isdigit():                                                          #if only number is entered
            value=int(scvalue.get())
        elif scvalue.get()=="":                                                              #if no input is entered
            value="Missing Inputs"
            scvalue.set(value) 
            screen.update()
            time.sleep(2)
            value=""
        else:
            try:                                                                             #if the expression is valid
                value=eval(screen.get())
            except:                                                                          #if the expression is invalid
                value="Syntax Error"
                scvalue.set(value) 
                screen.update()
                time.sleep(2)
                value=""
        scvalue.set(value)                                                                  #display the result on screen 
        screen.update()  
    elif text=="C":                                                                         #if clear(C) button pressed
        scvalue.set("")
        screen.update()
    else:                                               
        scvalue.set(scvalue.get()+text)                                                     #screenvalue in any other case
        screen.update()

#=================================================defining backspace() function===========================================
def back(event):
    current_text = screen.get()
    if current_text and screen['state'] == 'readonly':
        screen.configure(state='normal')
        screen.delete(len(current_text) - 1, END)
        screen.configure(state='readonly')

#======================================defining variable and setting its default value====================================
scvalue=StringVar()
scvalue.set("")

#=======================================================Entry widget======================================================
screen=Entry(root,width=15,textvariable=scvalue,state='readonly',font='Fixedsys 32 normal',border=25,relief=SUNKEN,justify=RIGHT,fg="black",readonlybackground="blue2")
screen.grid(row=0,column=0,columnspan=4,padx=10,pady=15)

#========================================================Button widgets===================================================
button_values = [
    ("C", "red", "white"),
    ("(", "blue2", "black"),
    (")", "blue2", "black"),
    ("/", "blue2", "black"),
    ("7", "grey15", "blue2"),
    ("8", "grey15", "blue2"),
    ("9", "grey15", "blue2"),
    ("*", "blue2", "black"),
    ("4", "grey15", "blue2"),
    ("5", "grey15", "blue2"),
    ("6", "grey15", "blue2"),
    ("-", "blue2", "black"),
    ("1", "grey15", "blue2"),
    ("2", "grey15", "blue2"),
    ("3", "grey15", "blue2"),
    ("+", "blue2", "black"),
    ("0", "grey13", "blue2"),
    (".", "grey2", "white"),
    ("Back", "grey2", "white"),
    ("=", "darkorange", "white")]

row_num, col_num = 1, 0
for value, bg_color, fg_color in button_values:
    button = Button(root, text=value,height=1,width=4, font="helvetica 24 bold", bg=bg_color, fg=fg_color,
                    border=8, relief=GROOVE)
    if value == "Back":
        button.config(padx=15, pady=15, font="helvetica 14 bold")
        button.bind("<Button-1>", back)
    else:
        button.bind("<Button-1>", click)
    button.grid(row=row_num, column=col_num, padx=3, pady=3)
    col_num += 1
    if col_num > 3:
        col_num = 0
        row_num += 1


root.mainloop() 
#=====================================================END of mainloop=====================================================