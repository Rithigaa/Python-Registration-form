from tkinter import *
window=Tk()
window.title("Login")
window.geometry('600x470')
window.resizable(False,False)

def register():
    name_info=nameValue.get()
    phn_info=phnValue.get()
    gen_info=genValue.get()
    email_info=emailValue.get()
    
    #creating file for entered data
    file=open(name_info+ ".txt","w")
    file.write(name_info+"\n")
    file.write(phn_info+"\n")
    file.write(gen_info+"\n")
    file.write(email_info+"\n")
    file.close()

    #clear box after one registration
    #nameEntry.delete(0,END)
    #phnEntry.delete(0,END)
    #genEntry.delete(0,END)
    #emailEntry.delete(0,END)
    #diplay registered
    Label(text="Registeration success",fg="green",font=("calibri",11)).place(x=250,y=430)
#heading
Label(window,text="Python registration",font="arial 25").pack(pady=50)
#text
Label(text="UserName",font=23).place(x=100,y=150)
Label(text="Phone",font=23).place(x=100,y=200)
Label(text="Gender",font=23).place(x=100,y=250)
Label(text="Email",font=23).place(x=100,y=300)
#entry
nameValue=StringVar()
phnValue=StringVar()
genValue=StringVar()
emailValue=StringVar()
#box
nameEntry=Entry(window,textvariable=nameValue,width=30,bd=2,font=20).place(x=200,y=150)
phnEntry=Entry(window,textvariable=phnValue,width=30,bd=2,font=20).place(x=200,y=200)
genEntry=Entry(window,textvariable=genValue,width=30,bd=2,font=20).place(x=200,y=250)
emailEntry=Entry(window,textvariable=emailValue,width=30,bd=2,font=20).place(x=200,y=300)

#check button
checkValue=IntVar
checkbtn=Checkbutton(text="remember me?",variable=checkValue)
checkbtn.place(x=200,y=340)

Button(text="Register",font=20,width=11,height=2,command=register).place(x=250,y=380)

window.mainloop()