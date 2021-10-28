#IMPORTING NECESSARY PACKAGES AND LIBRARY
import tkinter as tk
from tkinter import *
import time
from tkinter import messagebox
import datetime

#DEFINING GRAPHICAL USER INTERFACE
Change=Tk()
Change.geometry("600x400")
Change.title("Changing prices") 

#DEFINING Frames
Frame1= Frame(Change)
Frame1.pack(side=TOP)

frame2=Frame(Change)
frame2.pack(side=TOP)

frame3=Frame(Change)
frame3.pack(side=TOP)


###########################################################	VARIABLES	##################################################
#Frame2 Variables

Samosa_Variable=StringVar()
Kachori_Variable=StringVar()
Mirchivada_Variable=StringVar()
Breadpakoda_Variable=StringVar()
Jalebi_Variable=StringVar()

#Variable
now=(datetime.datetime.now().strftime("\n    Date=%d-%m-%y\tTime=%H:%M:%S"))


#Price Variables
with open("Prices.txt","r") as f:
			line=f.readlines()
			Samosa_p=float(line[2])
			Kachori_p=float(line[4])
			Mirchivada_p=float(line[6])
			Breadpakoda_p=float(line[8])
			Jalebi_p=(float(line[10]))

#Inititalizing entry fields
Samosa_Variable.set(str(Samosa_p))
Kachori_Variable.set(str(Kachori_p))
Mirchivada_Variable.set(str(Mirchivada_p))
Breadpakoda_Variable.set(str(Breadpakoda_p))
Jalebi_Variable.set(str(Jalebi_p))


######################################################## 	FUNCTIONS and COMMANDS	#################################################
def Back():
	ans=messagebox.askyesnocancel("BACK","Are you sure want to Back to the Menu window?")
	if(ans==True):
		Change.destroy()
		import Menuwindow
	else:
		Change.destroy()
		import Changingprices 
		
def Reset():
	Samosa_Variable.set("12")
	Kachori_Variable.set("10")
	Mirchivada_Variable.set("20")
	Breadpakoda_Variable.set("25")
	Jalebi_Variable.set("180")
	
def Update():
	f=open("Prices.txt","w")
	f.write("\tCURRENT PRICES ARE\n")
	f.write("Samosa\n")
	
	f.write(Samosa_Variable.get())
	
	f.write("\nKachori\n")
	f.write(Kachori_Variable.get())
	
	f.write("\nMirchivada\n")
	f.write(Mirchivada_Variable.get())
	
	f.write("\nBreadpakoda\n")
	f.write(Breadpakoda_Variable.get())

	f.write("\nJalebi\n")
	f.write(Jalebi_Variable.get())

	f.write("\n\tPrices last updated on")
	f.write(now)
	
	f.close()

	messagebox.showinfo("SUCCESSFULL","PRICES HAVE BEEN CHANGED SUCCESSFULLY")


#######################################################		FRAME1		######################################
	
#DEFINING FRAME1 LABELS
label_info = Label(Frame1, font = ('arial',50,'bold'), text ="CHANGE PRICE", fg = "BLUE", bd = 10, anchor = 'w')
label_info.grid(row = 0, column = 0)

local_time = time.asctime(time.localtime(time.time()))

label_info = Label(Frame1, font = ('arial',20,'bold'), text = local_time, fg = "ORANGE", bd = 10, anchor = 'w')
label_info.grid(row = 1, column = 0)


########################################################	FRAME2 		########################################
#DEFINING FRAME2 LABELS
Item_Label4=Label(frame2,text="ITEM",font=('arial',12))
Item_Label4.grid(row=1,column=1)

Quantity_Label5=Label(frame2,text="NEW PRICE",font=('arial',12))
Quantity_Label5.grid(row=1,column=2)

#Samosa
Samosa_Label=Label(frame2,text="Samosa")
Samosa_Label.grid(row=2,column=1)
Entry1=Entry(frame2,textvariable=Samosa_Variable,font=('arial',10,'bold'),bd=2,insertwidth=4,bg="powder blue",justify='right')
Entry1.grid(row=2,column=2)

#Kachori
Kachori_Label=Label(frame2,text="Kachori")
Kachori_Label.grid(row=3,column=1)
Entry2=Entry(frame2,textvariable=Kachori_Variable,font=('arial',10,'bold'),bd=2,insertwidth=4,bg="powder blue",justify='right')
Entry2.grid(row=3,column=2)

#Mirchivada
Mirchivada_Label=Label(frame2,text="Mirchivada")
Mirchivada_Label.grid(row=4,column=1)
Entry3=Entry(frame2,textvariable=Mirchivada_Variable,font=('arial',10,'bold'),bd=2,insertwidth=4,bg="powder blue",justify='right')
Entry3.grid(row=4,column=2)

#Breadpakoda
Breadpakoda_Label=Label(frame2,text="Breadpakoda")
Breadpakoda_Label.grid(row=5,column=1)
Entry4=Entry(frame2,textvariable=Breadpakoda_Variable,font=('arial',10,'bold'),bd=2,insertwidth=4,bg="powder blue",justify='right')
Entry4.grid(row=5,column=2)

#Jalebi
Jalebi_Label=Label(frame2,text="Jalebi")
Jalebi_Label.grid(row=6,column=1)
Entry5=Entry(frame2,textvariable=Jalebi_Variable,font=('arial',10,'bold'),bd=2,insertwidth=4,bg="powder blue",justify='right')
Entry5.grid(row=6,column=2)

###############################	FRAME2 BUTTONS	###########################

Back_Button=Button(frame3,text="BACK",fg="yellow",bg="black",activebackground="yellow",width=10,bd=5,command=Back)
Back_Button.grid(row=2,column=1)

Reset_Button=Button(frame3,text="RESET",fg="yellow",bg="black",activebackground="yellow",width=10,bd=5,command=Reset)
Reset_Button.grid(row=2,column=2)

Update_Button=Button(frame3,text="UPDATE",fg="yellow",bg="black",activebackground="yellow",width=10,bd=5,command=Update)
Update_Button.grid(row=2,column=3)

Change.mainloop()