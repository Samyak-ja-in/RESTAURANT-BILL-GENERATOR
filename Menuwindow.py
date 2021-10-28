#IMPORTING NECESSARY PACKAGES AND LIBRARY
import tkinter as tk
from tkinter import *
from tkinter import messagebox

#DEFINING GRAPHICAL USER INTERFACE
Menu_window=Tk()
Menu_window.geometry("250x180")
Menu_window.title("Selection window")

#################################################		DEFINING FUNCTIONS			#####################################
def Logout():
	ans=messagebox.askyesnocancel("Logout","Are you sure want to logout?")
	if(ans==True):
		messagebox.showinfo("Logout Succesfull","Logged out Successfully")
		Menu_window.destroy()
		import Loginpage
	else:
		import Menuwindow

def function_Selection_Menu():
	Menu_window.destroy()
	import Selectionmenu

def function_Changing_prices():
	Menu_window.destroy()
	import Changingprices
	

##################################################			LABELS			##################################################
Label1=Label(Menu_window,text="For Bill Genration:",font=('arial',10,'bold'),bd=2)
Label1.grid(row=2,column=1)

Label2=Label(Menu_window,text="For Changing price:",font=('arial',10,'bold'),bd=2)
Label2.grid(row=3,column=1)


#################################################			BUTTONS			###################################################
Button1=Button(Menu_window,text="Press Here",command=function_Selection_Menu,bg="BLACK",activebackground="WHITE",fg="YELLOW",bd=2)
Button1.grid(row=2,column=2)

Button2=Button(Menu_window,text="Press Here",command=function_Changing_prices,bg="BLACK",activebackground="WHITE",fg="YELLOW",bd=2)
Button2.grid(row=3,column=2)

Button3=Button(Menu_window,text="Logout",command=Logout,bg="BLACK",activebackground="WHITE",fg="YELLOW",bd=2)
Button3.grid(row=5,column=2)

Menu_window.mainloop()