#------------------------------------
#day2_variablesandoperators
#------------------------------------

#1.Even or Odd

num=int(input("Enter the number :"))
if(num%2==0):
    print("The given number is even.")
else:
    print("The given number is odd.")
print("------------------------------")


#2.Positive/Negative/Zero

n=int(input("Enter the value:"))
if(n>0):
  print("The given number is Positive.")
elif(n<0):
  print("The given number is Negative.")
else:
  print("The given number is Zero.")
print("------------------------------")


#3.Largest of 3 NUMBERS 

x=int(input("Enter x="))
y=int(input("Enter y="))
z=int(input("Enter z="))
if(x>y and x>z):
  print("Largest number is",x)
elif(y>x and y>z):
  print("Largest number is",y)
else:
  print("Largest number is",z)
print("-----------------------------")


#4.Leap year check

year=int(input("Enter year:"))
if(year%4==0):
   print("It is a leap year.")
else:
   print("It is not a leap year.")
print("----------------------------")
