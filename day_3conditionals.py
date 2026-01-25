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
if (avg>=85):
    print(" Grade:'A' ")
elif (avg>=65 and avg<85):
    print("Grade:'B' ")
elif (avg>=45 and avg<65):
    print("Garde:'C' ")
else:
    print("Failed!")
print("----------------------------------")


#2.Vowel_Consonant

c=str(input("Enter character:"))
vowels='AEIOUaeiou'
if(c in vowels):
    print("The given character is a vowel.")
else:
    print("The given character is a consonant.")
print("-----------------------------")


#3.Triangle validity 

print("The sides of a Triangle:")

a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
if((a+b)>c and (b+c)>a and (a+c)>b):
   print("The given sides form a valid    Triangle.")
else:
   print("It's not a valid Triangle")

print("-------------------------------")

