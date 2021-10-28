#IMPORTING NECESSARY PACKAGES AND LIBRARY
import numpy as np
import pandas as pd
import csv
import datetime
import re
from matplotlib import pyplot as plt


#ASKING USER FOR WHICH DATE HE/SHE WATS TO ANALYSE DATA
date=input("\nPlease type the date of which analysis you want in date-month-year(2021) format")

#READING THE CSV
data=pd.read_csv(f"Database{date}.csv")

#PRINTING DATAFRAME INDEXES
print("\nDataframe indexes")
Index=(data.columns[0:])
for name in Index:
    print (name,end="\t")


#PRINTING SUM OF ALL GST FIELDS
print("\nSum of all GST Fields")
print(round(data["GST"].sum(),3))


#Printing Sum of all GST fields and total sales
GST_total=data["GST"].sum()
Price_total=round(data["TOTALPRICE"].sum(),3)
print(f"Sum of GST is {GST_total} \nSum of all Totalprice is {Price_total}")


#COUNTING
total_people=len(data.axes[0])
print("Number of people visited and purchased")
print(total_people)

#Printing number of males and females visited to our shop and purchased
print("Number of males and females came to your shop")
print(data["GENDER"].value_counts(ascending=True))


#Printing Percentage of males and females
print("Percentage of males and females")
print(round(data["GENDER"].value_counts(ascending=True,normalize=True)*100,3))


#Printing Whole analysis of Price column
print("Whole analysis of Price given to us by customers")
print(round(data["TOTALPRICE"].describe(),3))

#Number of people paid you more then 100
df=data[data["TOTALPRICE"]>100]["TOTALPRICE"]
print("Number of people paid you more then 100")
num=len(df.axes[0])
print(num)


###############################################################     PIE CHART       ###############################

#Analysis of each quantity sold
Samosa_total=data["SAMOSA"].sum()
Kachori_total=data["KACHORI"].sum()
Mirchivada_total=data["MIRCHIVADA"].sum()
Breadpakoda_total=data["BREADPAKODA"].sum()
Jalebi_total=(data["JALEBI"].sum())/1000

print("Samosa sold today ",Samosa_total)
print("Kachori sold today ",Kachori_total)
print("Mirchivada sold today ",Mirchivada_total)
print("Breadpakoda sold today ",Breadpakoda_total)
print("Jalebi sold today(in Kgs) ",Jalebi_total)


Items_list=["SAMOSA","KACHORI","MIRCHIVADA","BREADPAKODA"]
Items_data=[Samosa_total,Kachori_total,Mirchivada_total,Breadpakoda_total]
fig=plt.figure(figsize=(5,5))
plt.title("ITEMS QUANTITY SOLD TODAY")
plt.pie(Items_data,labels=Items_list,autopct="%0.1f%%",shadow=False,colors=['r','g','y','b'],explode=[0,0,0,0.1],startangle=145)
plt.show()


########################################################        BAR CHART       ####################################
#PLOTTING A BAR CHART BETWEEN MALES AND FEMALES VISITED
plt.title("NUMBER OF MALE AND FEMALE")
data["GENDER"].value_counts().plot(kind="bar",color=["y","r"],width=0.5)
plt.grid(color="b",linestyle='--', linewidth=0.5)
plt.xlabel("GENDER")
plt.ylabel("NUMBER")
plt.show()







