# Functions in Python -> Block of statements that perform a specific task.


# A built-in function is a pre-defined block of code that 
# comes built directly into a programming language's library

def sum(a ,b):  #parameter
    sum=a+b
    return sum
print(sum(3,6))
print(sum(7,88)) #argument

# average of three number
def calc_avg(a,b,c):
    sum=(a+b+c)
    avg=sum/3
    print(avg)
    return(avg)
calc_avg(1,2,3)

# average of two number
def calc_avg(a,b):
    sum=a+b
    avg=sum/2
    print(avg)
    return(avg)
calc_avg(34,67)


# WAF to print the length of a list. ( list is the parameter)
list=[1,2,"krish",89,"harsh"]
print(len(list))

# using def fumction
list=[1,2,"krish",89,"harsh"]
def print_len(list):
    print(len(list))
print_len(list)

# WAP to print the elements of a list in a single line. ( list is the parameter)
list=[1,2,"krish",89,"manya"]
def sing_line(list):
    for item in list:
        print(item, end=" ")
sing_line(list)


# WAF to find the factorial of n. (n is the parameter)

n=int(input("enter a number"))  # it is by simple method
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)

#by function method
n= int(input("enter a number"))

def calc_fact(n):
    fact=1  
    for i in range (1,n+1):
        fact = fact*i
    return fact
print(calc_fact(n))


# WAF to convert USD to INR. 
def conv_dol(usd):
    inr = usd*83.30
    print(inr)
print(conv_dol(10))   








