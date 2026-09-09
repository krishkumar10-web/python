#  string is a data type which stores sequence of characters
# strings are immutable


#  it uses concetenation operator + to add two strings 
a="krish"
b="sher"
print(a+b)



# indexing
a= "krish_and_kumar"
print(a[0:4])
print(a[4])
print(a[0:])           

#  string fuction qusetion


# WAP to input user’s first name & print its length
a=input("enter your name ")
print(len(a))


# WAP to find the occurrence of ‘$’ in a String
a=input("enter a word")
print(a.count("$"))


# WAP to check if a number entered by the user is odd or even
a=int(input("enter a number"))
if a%2==0:
    print("number is even")
else:
    print("number is odd")


# WAP to find the greatest of 3 numbers entered by the user
a=int(input("enter first "))
b=int(input("enter second number"))
c=int(input("enter a third number"))
if a>b and a>c:
    print("a is greatest")
elif b>a and b>c:
    print("b is greatest")
else:
    print("c is greatest")    


# WAP to check if a number is a multiple of 7 or not.
a=int(input("enter a number"))
if a%7==0:
    print("number is multiple of 7")
else:
    print("not divisible")
    

    