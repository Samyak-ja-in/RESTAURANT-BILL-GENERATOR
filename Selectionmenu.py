#IMPORTING NECESSARY PACKAGES AND LIBRARY
import tkinter as tk
from tkinter import *
import datetime
from tkinter import messagebox
import re
import pandas as pd
import numpy as np
import csv

#DEFINING GRAPHICAL USER INTERFACE
Selection_menu=Tk()
Selection_menu.title("BILL GENRATOR")
Selection_menu.geometry("620x420")


#######################################################		FRAME VARIABLES		#####################################################
#Frame2 Variables
Name_Var=StringVar()
Gender_Var=IntVar()
Gender_Var.set(2)

#Frame3 Variables

Samosa_Variable=StringVar()
Kachori_Variable=StringVar()
Mirchivada_Variable=StringVar()
Breadpakoda_Variable=StringVar()
Jalebi_Variable=StringVar()
total_quantity=StringVar()
GST_Variable=StringVar()
Totalprice=StringVar()
Netprice_Variable=StringVar()
totalprice=StringVar()


#Price variables

Samosa_p=DoubleVar()
Kachori_p=DoubleVar()
Mirchivada_p=DoubleVar()
Breadpakoda_p=DoubleVar()
Jalebi_p=DoubleVar()

#INITIALIZING

Samosa_Variable.set("0")
Kachori_Variable.set("0")
Mirchivada_Variable.set("0")
Breadpakoda_Variable.set("0")
Jalebi_Variable.set("0")
total_quantity.set("0")
GST_Variable.set("0")
Totalprice.set("0")
Netprice_Variable.set("0")



#FOR TAKING CURRENT DATE and TIME
now=(datetime.datetime.now().strftime("Date=%d-%m-%y\tTime=%H:%M:%S"))
date_data= datetime.datetime.now()

#CURRENT DATE
date=date_data.strftime("%d-%m-%Y")


####################################################		DEFINING FRAME		################################################
	
#CREATION OF FRAME
frame1=Frame(Selection_menu)
frame1.pack(side=TOP)

frame2=Frame(Selection_menu)
frame2.pack(side=TOP)

frame3=Frame(Selection_menu)
frame3.pack(side=LEFT)

frame4=Frame(Selection_menu)
frame4.pack(side=LEFT)

frame5=Frame(Selection_menu)
frame5.pack(side=RIGHT)


###########################################################		FUNCTIONS		##############################################
b=0
c=0
def Createdatabase():
	try:
		with open(f"Database{date}.csv","r",newline="") as file:
			a=file.read()
		global b
		b=2
		c=b
		
	except:
			row=['NAME','GENDER','SAMOSA','KACHORI','MIRCHIVADA','BREADPAKODA','JALEBI','TOTALQUANTITY','TOTALCOST','GST','TOTALPRICE']
			with open(f"Database{date}.csv","w",newline="") as f:
				write=csv.writer(f)
				write.writerow(row)
			messagebox.showinfo("Created database successfully")
	
	
	if(b==2):
			messagebox.showinfo("Warning","Dont try to overwrite to database Database created previousely")
		


def Calculate():
	global c
	if(c==0):
		try:
			with open(f"Database{date}.csv","r",newline="") as file:
				a=file.read()
			
			c=2
		
		except:
			
			row=['NAME','GENDER','SAMOSA','KACHORI','MIRCHIVADA','BREADPAKODA','JALEBI','TOTALQUANTITY','TOTALCOST','GST','TOTALPRICE']
			with open(f"Database{date}.csv","w",newline="") as f:
				write=csv.writer(f)
				write.writerow(row)
			messagebox.showinfo("Created database successfully")
			c=2
		
		

	if(Name_Var.get()==""):
		messagebox.showinfo("Mandatory","Name field is Mandatory")
	else:
		if Jalebi_Variable.get()=='0':
			total_quantity.set(str(float(Samosa_Variable.get())+float(Kachori_Variable.get())+float(Mirchivada_Variable.get())+float(Breadpakoda_Variable.get())))
			
		else:
			total_quantity.set(str(float(Samosa_Variable.get())+float(Kachori_Variable.get())+float(Mirchivada_Variable.get())+float(Breadpakoda_Variable.get())+float(int('1'))))



		with open("Prices.txt","r") as f:
				line=f.readlines()
				Samosa_p=float(line[2])
				Kachori_p=float(line[4])
				Mirchivada_p=float(line[6])
				Breadpakoda_p=float(line[8])
				Jalebi_p=(float(line[10])/1000)
				
		try:
			totalprice=str(float(Samosa_Variable.get())*Samosa_p+float(Kachori_Variable.get())*Kachori_p+float(Mirchivada_Variable.get())*Mirchivada_p+float(Breadpakoda_Variable.get())*Breadpakoda_p+float(Jalebi_Variable.get())*Jalebi_p)
		except:
			messagebox.showerror("ALERT!!","Please enter a valid value")
		
		y=round(float(totalprice),3)
		Totalprice.set(y)
		#GST=(float(totalprice)*0.18)
		GST=round(float(totalprice)*0.18,3)
		GST_Variable.set(GST)
		Netprice_Variable.set(round(GST+float(totalprice),3))
		
		if(Gender_Var.get()==1):
			gender="Male"
		elif(Gender_Var.get()==2):
			gender="Female"
		
		data=[f"{Name_Var.get()}",gender,f"{Samosa_Variable.get()}",f"{Kachori_Variable.get()}",f"{Mirchivada_Variable.get()}",f"{Breadpakoda_Variable.get()}",f"{Jalebi_Variable.get()}",f"{total_quantity.get()}",f"{Totalprice.get()}",f"{GST_Variable.get()}",f"{Netprice_Variable.get()}"]
		
		with open(f"Database{date}.csv","a",newline="") as f:
			write=csv.writer(f)
			write.writerow(data)
	
def Reset():
	Name_Var.set("")
	Gender_Var.set(1)
	Samosa_Variable.set("0")
	Kachori_Variable.set("0")
	Mirchivada_Variable.set("0")
	Breadpakoda_Variable.set("0")
	Jalebi_Variable.set("0")
	total_quantity.set("0")
	GST_Variable.set("0")
	Totalprice.set("0")
	Netprice_Variable.set("0")

def Back():
	Selection_menu.destroy()
	import Menuwindow
	
def Genrate_Invoice():
	if(Name_Var.get()==""):
		messagebox.showinfo("Mandatory","Name field is Mandatory")
	else:

		with open(f"Invoice {Name_Var.get()}.txt","w") as f:
			f.write("\t\t\tSAMYAK GROUP OF RESTAURANTS\n")
			f.write("\t\t\t\tINVOICE\n")
			f.write(now)
			f.write("\n")
			f.write(f"Name:{Name_Var.get()}")
			f.write("\nITEM\t     QUANTITY\t\n")
			f.write("----------------------\n")
			Item_Dictionary={"Samosa     ":Samosa_Variable.get(),"Kachori    ":Kachori_Variable.get(),"Mirchivada ":Mirchivada_Variable.get(),"Breadpakoda":Breadpakoda_Variable.get(),f"Jalebi({Jalebi_Variable.get()}gm)":Jalebi_Variable.get(),"Total Quantity":total_quantity.get(),"Totalprice ":Totalprice.get(),"GST        ":GST_Variable.get(),"Netprice ":Netprice_Variable.get()}
			
			
				
			
			for data in Item_Dictionary:
					if((Item_Dictionary[data])!="0"):
						if(data=="Totalprice " or data=="Netprice " or data=="Total Quantity"):
							f.write("----------------------\n")
						f.write(data)
						f.write("\t")
						f.write(Item_Dictionary[data])
						f.write("\n")
			f.write("----------------------\n")			
			f.write("\tENJOY YOUR BREAKFAST\n")
			
		messagebox.showinfo("INVOICE GENRATED",f"Total Quantities={total_quantity.get()}")




###################################################		LABELS AND ENTRY FIELDS			##############################################
#HEADING OF PAGE

###############		FRAME1			###############

Label1=Label(frame1,text="BILL GENRATOR",font=('arial',25,'bold'),fg="dark green",bd=10)
Label1.grid(row=1,column=2)

Label2=Label(frame1,text=now,font=('arial',10,'bold'),fg="blue")
Label2.grid(row=2,column=2)

###############		FRAME2		###################

Name_Label3=Label(frame2,text="Name",fg="black")
Name_Label3.grid(row=1,column=1)

Name_entry=Entry(frame2,textvariable=Name_Var,font=('arial',10,'bold'),bd=2,insertwidth=4,bg="powder blue")
Name_entry.grid(row=1,column=2)

Gender_Label4=Label(frame2,text="\tGender",fg="black")
Gender_Label4.grid(row=1,column=3)

Gender_Male=Radiobutton(frame2,text="Male",variable=Gender_Var,value=1)
Gender_Male.grid(row=1,column=4)

Gender_Female=Radiobutton(frame2,text="Female",variable=Gender_Var,value=2)
Gender_Female.grid(row=2,column=4)

##############		Frame3		######################

Item_Label4=Label(frame3,text="ITEM",font=('arial',12))
Item_Label4.grid(row=1,column=1)
Quantity_Label5=Label(frame3,text="QUANTITY",font=('arial',12))
Quantity_Label5.grid(row=1,column=2)

#Item1
Samosa_Label=Label(frame3,text="Samosa")
Samosa_Label.grid(row=2,column=1)
Entry1=Entry(frame3,textvariable=Samosa_Variable,font=('arial',10,'bold'),bd=2,insertwidth=4,bg="powder blue",justify='right')
Entry1.grid(row=2,column=2)

#Item2
Kachori_Label=Label(frame3,text="Kachori")
Kachori_Label.grid(row=3,column=1)
Entry2=Entry(frame3,textvariable=Kachori_Variable,font=('arial',10,'bold'),bd=2,insertwidth=4,bg="powder blue",justify='right')
Entry2.grid(row=3,column=2)

#Mirchivada
Mirchivada_Label=Label(frame3,text="Mirchivada")
Mirchivada_Label.grid(row=4,column=1)
Entry3=Entry(frame3,textvariable=Mirchivada_Variable,font=('arial',10,'bold'),bd=2,insertwidth=4,bg="powder blue",justify='right')
Entry3.grid(row=4,column=2)

#Breadpakoda
Breadpakoda_Label=Label(frame3,text="Breadpakoda")
Breadpakoda_Label.grid(row=5,column=1)
Entry4=Entry(frame3,textvariable=Breadpakoda_Variable,font=('arial',10,'bold'),bd=2,insertwidth=4,bg="powder blue",justify='right')
Entry4.grid(row=5,column=2)

#Jalebi
Jalebi_Label=Label(frame3,text="Jalebi")
Jalebi_Label.grid(row=6,column=1)
Entry5=Entry(frame3,textvariable=Jalebi_Variable,font=('arial',10,'bold'),bd=2,insertwidth=4,bg="powder blue",justify='right')
Entry5.grid(row=6,column=2)
	
	
	
################################################		Buttons		################################################################

Calculate_button=Button(frame5,bg="orange",fg="black",activebackground="yellow",width=20,bd=10,text="CALCULATE",command=Calculate)
Calculate_button.grid(row=1,column=1)

Reset_button=Button(frame5,bg="orange",fg="black",activebackground="yellow",width=20,bd=10,text="RESET",command=Reset)
Reset_button.grid(row=2,column=1)

Back_button=Button(frame5,bg="orange",fg="black",activebackground="yellow",width=20,bd=10,text="BACK",command=Back)
Back_button.grid(row=3,column=1)


Genrateinvoice_button=Button(frame5,bg="orange",fg="black",activebackground="yellow",width=20,bd=10,text="GENRATE INVOICE",command=Genrate_Invoice)
Genrateinvoice_button.grid(row=4,column=1)

Createdatabase_button=Button(frame5,bg="orange",fg="black",activebackground="yellow",width=20,bd=10,text="CREATE DATABASE",command=Createdatabase)
Createdatabase_button.grid(row=5,column=1)


####################################################		AUTOMATIC ENTRY FIELDS		################################################
Total_quantity_Label=Label(frame4,text="TOTAL UNITS")
Total_quantity_Label.grid(row=1,column=1)
Total_quantity_Entry=Entry(frame4,textvariable=total_quantity,font=('arial',10,'bold'),bd=2,insertwidth=4,bg="powder blue",justify='right')
Total_quantity_Entry.grid(row=1,column=2)

Totalprice_Label=Label(frame4,text="TOTAL PRICE")
Totalprice_Label.grid(row=2,column=1)
Totalprice_Entry=Entry(frame4,textvariable=Totalprice,font=('arial',10,'bold'),bd=2,insertwidth=4,bg="powder blue",justify='right')
Totalprice_Entry.grid(row=2,column=2)

GST_Label=Label(frame4,text="GST")
GST_Label.grid(row=3,column=1)
GST_Entry=Entry(frame4,textvariable=GST_Variable,font=('arial',10,'bold'),bd=2,insertwidth=4,bg="powder blue",justify='right')
GST_Entry.grid(row=3,column=2)


Netprice_Label=Label(frame4,text="NET PRICE")
Netprice_Label.grid(row=4,column=1)
Netprice_Entry=Entry(frame4,textvariable=Netprice_Variable,font=('arial',10,'bold'),bd=2,insertwidth=4,bg="powder blue",justify='right')
Netprice_Entry.grid(row=4,column=2)

Selection_menu.mainloop()	