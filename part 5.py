#  loops - loops are used to repeat instruction 


# basic eg of for and while loops
# print  hello world 10 times 

for i in range(10):
    print("hello world")



#  print  hello world 10 times using while loop 

i=0
while i<10:
    print("hello world")
    i+=1

#  wap to print 1 to 100 using for loop
for i in range(1,101):
    print(i)

# wap to print 1 to 100 using while loop
i=0
while i<101:
    print(i)
    i+=1

# wap to print 100 to 1 using for loop

for i in range(100,0,-1):
    print(i)

# wap to print 100 to 1 using while loop
i=100
while i>0:
    print(i)
    i-=1


# Print the multiplication table of a number n.
number = int(input("enter a number"))

for i in range(1,11):
     print(number,"X",i,"=",number*i)

#Print the elements of the following list using a loop: 
tuple =[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
for i in tuple:
    print(i)

#Search for a number x in this tuple using loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100] 



#WAP to find the sum of first n numbers. (using while)
n=int(input("enter first number"))
print (n*(n+1)/2)

# wap to find the sum of even number from 1 to 100 /#new added
count=0
for i in range(1,101):
    if i%2==0:
        count=count+1
sum=count*(count+1)
print(sum)



# WAP to find the factorial of first n numbers. (using for)

n = int(input("enter a value"))
fact=1
while i>0:
    fact*=i
    i-=1
print(fact)






    