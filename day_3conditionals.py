#--------------------------------------
#day3_conditionals
#--------------------------------------


#1.Grade calculator 

name=str(input("Enter name:"))
English=int(input("Enter marks in English="))
Maths=int(input("Enter marks in Maths="))
Science=int(input("Enter marks in Science="))
avg=(English+Maths+Science)//3
print("Average Marks=",avg)
print("Calculating the Grade:")
if (avg>85):
    print(" Grade:'A' ")
elif (avg>65 and avg<=85):
    print("Grade:'B' ")
elif (avg>45 and avg<=65):
    print("Garde:'C' ")
else:
    print("Failed!")
print("----------------------------------")


#2.