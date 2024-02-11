#=================================================importing required packages=============================================
from tkinter import*
import customtkinter as c
from PIL import Image
import random
import time

#=================================================defining root(window) layout============================================
c.set_appearance_mode("dark")
root=c.CTk()
root.geometry("600x200+400+250")
root.resizable(False,False)
root.iconbitmap("3.ico")
root.title("Password Generator:By Samiksha Mishra")

#===================================defining function for giving placeholder in entry widget==============================
def focusin(event):
    if t1.get() == "Enter desired length":
        t1.delete(0, END)
        t1.configure(fg_color='#030637',font=("Arial",16 ,"bold"),text_color="gold")

def focusout(event):
    if t1.get() == "":
        t1.insert(0, "Enter desired length")
        t1.configure(font=("Arial",16 ,"bold"),text_color="grey")

#============================================defining function for generate button========================================
def gen(event):
    global entvar
    lower='abcdefghijklmnopqrstuvwxyz'
    upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    number='1234567890'
    special_char='!@#$%^&*()._'
    try:
        length=int(entvar.get())
        if int(numvar.get())==1:
            if int(specvar.get())==1:
                string=lower+upper+number+special_char
            else:
                string=lower+upper+number
        elif int(specvar.get())==1:
            string=lower+upper+special_char
        else:
            string=lower+upper
        password="".join(random.sample(string,length))
        t1.delete(0,END)
        t2.delete(0,END)
        t2.insert(0,password)
    except:
        t1.insert(0,"Invalid Input")
        time.sleep(2)
        t1.delete(0,END)
    specvar.set(0)
    numvar.set(0)

#===============================================defining function for copy button=========================================
def copy(event):
    password = t2.get()
    root.clipboard_clear()  
    root.clipboard_append(password)  
    root.update()  
    t2.delete(0,END)

#======================================defining variable name and its data type===========================================
numvar=IntVar()
specvar=IntVar()
entvar=StringVar()

#==================================inserting a .png image at the left side in root window=================================
pic=c.CTkImage(dark_image=Image.open("pass.png"),size=(200,200))
left=c.CTkLabel(root,image=pic,text="")
left.grid(row=0,column=0,rowspan=5)

#===========================================Entry widget for input and output=============================================
t1=c.CTkEntry(root,textvariable=entvar,font=("Arial",16,"bold"),width=350,justify=CENTER,fg_color="#030637",text_color="grey",border_color="gold",border_width=2,corner_radius=80)
entry_placeholder = "Enter desired length"
t1.insert(0, entry_placeholder)                                 #displaying the placeholder text
t1.bind("<FocusIn>", focusin)                                   #placeholder text disappears when clicked to give input
t1.bind("<FocusOut>", focusout)
t1.grid(row=0,column=1,columnspan=4,padx=20)

t2=c.CTkEntry(root,font=("Arial",16,"bold"),width=250,justify=RIGHT,fg_color="snow",text_color="#030637",border_color="gold",border_width=2)
t2.grid(row=3,column=1,columnspan=3,padx=5)

#============================Checkbox widgets to include special characters and numbers===================================
num=c.CTkCheckBox(root,text="Numbers",variable=numvar,border_color='gold',border_width=2,font=("Arial",12,"bold"),hover_color="#030637",checkmark_color="gold",corner_radius=60,text_color="gold")
num.grid(row=1,column=1,columnspan=2)

spec=c.CTkCheckBox(root,text="Special Characters",variable=specvar,border_color='gold',border_width=2,font=("Arial",12,"bold"),hover_color="#030637",checkmark_color="gold",corner_radius=60,text_color="gold")
spec.grid(row=1,column=3,columnspan=2)

#========================================================Button widgets===================================================
g_img=c.CTkImage(dark_image=Image.open("g_btn.png"),size=(150,50))
g_btn=c.CTkButton(root,image=g_img,text="",font=("Arial",12,"bold"),corner_radius=50,fg_color="transparent",width=150,cursor="hand2")
g_btn.grid(row=2,column=2,columnspan=2)
g_btn.bind("<Button-1>", gen)

c_img=c.CTkImage(dark_image=Image.open("c_btn.png"),size=(100,30))
c_btn=c.CTkButton(root,text="",image=c_img,font=("Arial",12,"bold"),fg_color="transparent",width=120,cursor="hand2")
c_btn.grid(row=3,column=4)
c_btn.bind("<Button-1>", copy)
root.mainloop()
#=====================================================END of mainloop=====================================================