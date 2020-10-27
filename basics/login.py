from tkinter import  *
import tkinter.messagebox as mb

class loginak(Frame):
        def __init__(self,master):
            super().__init__(master)
            self.label_username=Label(self,text="username",font=("Times new roman",15))
            self.label_password=Label(self,text="username",font=("Times new roman",15))

            self.entry_usesrname=Entry(self)
            self.entry_password=Entry(self)
            
            self.label_username.grid(row=0,sticky=E)
            self.label_password.grid(row=1,sticky=E)

            self.entry_usesrname.grid(row=0,column=1)
            self.entry_password.grid(row=1,column=1)

            self.button=Button(self,text='login',command=self.login)
            self.button.grid(columnspan=2)

            self.pack()

        def login(self): 
                  username=self.entry_usesrname.get() 
                  password=self.entry_password.get()

                  if (username=="SK" and password=="Admin"):
                      mb.showinfo("Login","sucessfull")
                  else:
                      mb.showinfo('Login',"failed")

sk=Tk()
login=loginak(sk)
sk.mainloop()