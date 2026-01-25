#---------------------------------------

#day4_loops

#---------------------------------------


#1.print numbers from 1 to 100

for i in range(1,101,1):
   print("Numbers from 1 to 100:",i)

print("-----------------------------")


#2.sum of N numbers

n=int(input("Enter n:"))
sum_n=n*(n+1)//2
print("The sum of N numbers:",sum_n)


n=int(input("Enter n:"))
sum_n=0
for i in range(1,n+1):
  sum_n += 1
print("Sum of N numbers:",sum_n)

print("------------------------------")






