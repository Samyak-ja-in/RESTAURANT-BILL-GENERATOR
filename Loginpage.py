														#USERNAME: Samyak
														#PASSWORD: 1234

#IMPORTING NECESSARY PACKAGES AND LIBRARY
import tkinter as tk
from tkinter import *
from tkinter import messagebox

#DEFINING GRAPHICAL USER INTERFACE
Login_window=Tk()
Login_window.title("Login page")
Login_window.geometry("620x220")


###################################################		DEFINING FUNCTIONS		#################################
def destroy():
	Login_window.destroy()
	
Var1=StringVar("")
Var2=StringVar()


def function_Successfull():
	Login_window.destroy()
	import Menuwindow
	

def function_Enter():
		if(Var1.get()=="Samyak" and Var2.get()=="1234"):
			messagebox.showinfo("Login Succesfull","Entering to the Menu window")
			function_Successfull()	
		else:
			messagebox.showerror("ERROR!!","Enter correct password or username")
			Var1.set("")
			Var2.set("")
		

################################################		LABELS		###############################################
top_label=Label(Login_window,text="\tSAMYAK GROUP OF\n\tRESTAURANTS",fg="ORANGE",bd=10,font=('arial',20,'bold'))
top_label.grid(row=1,column=1)

Login1_label=Label(Login_window,text="Please enter your login credentials",bd=2,font=('arial',10,'bold'),fg="DARK BLUE")
Login1_label.grid(row=2,column=1)

Login2_label=Label(Login_window,text="Username:",font=('arial',10,'bold'),bd=2)
Login2_label.grid(row=3,column=1)

Login3_label=Label(Login_window,text="Password:",font=('arial',10,'bold'),bd=2)
Login3_label.grid(row=4,column=1)


################################################		ENTRY FIELDS		########################################
Entry1=Entry(Login_window,textvariable=Var1,font=('arial',10,'bold'),bd=2,insertwidth=4,bg="powder blue")
Entry1.grid(row=3,column=2)

Entry2=Entry(Login_window,textvariable=Var2,show="*",font=('arial',10,'bold'),bd=2,insertwidth=4,bg="powder blue")
Entry2.grid(row=4,column=2)


#################################################			BUTTONS			#########################################
Button1=Button(Login_window,text="Enter",bg="STEEL BLUE",activebackground="Green",fg="YELLOW",bd=10,command=function_Enter)
Button1.grid(row=5,column=2)

Button2=Button(Login_window,text="Exit",bg="STEEL BLUE",activebackground="Green",fg="YELLOW",bd=10,command=destroy)
Button2.grid(row=5,column=1)

Login_window.mainloop()