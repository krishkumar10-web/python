# dictionary 
# WAP to enter names of students and their marks & store them in a dictionary.
a={}
for i in range(3):
    name=input("enter name")
    marks=int(input("enter marks"))
    # a[name]=marks
print(a) 

#  nested dictionary
home={"name":"krish", 
"area":{"gumla":18,
"ranchi":1, "raipur":1}}
print(home["area"]["raipur"])

# set in python
num={1,2,2,3,4,4,5,5,6,6,7,7,8,8,9,9}   #sets does not allow duplicates
print(num)
print(type(num))

# Set Methods
# set.add( el )  #adds an element 
# set.remove( el )  #removes the elemants
# set.clear( )  #empties the set 
# set.pop( )  #removes a random value


#  uses of all the sets methods
set={1,2,3,4,5}
print(set)
set.add(6)
print(set)
set.remove(1)
print(set)
set.pop()
print(set)


# Store following word meanings in a python dictionary : 
# table : “a piece of furniture”, “list of facts & figures”
# cat : “a small animal”
a={"table":["a piece of furniture", "list of facts & figures"], "cat":["a small animal"]}
print(a)



# You are given a list of subjects for students. Assume one classroom is required for 1
# subject. How many classrooms are needed by all students.
# ”python”, “java”, “C++”, “python”, “javascript”,
# “java”, “python”, “java”, “C++”, “C
# we list all the unique java python javascript c++ c only 5 classrooms are needed 
subj=["python", "java", "C++", "python", "javascript",
"java", "python", "java", "C++", "C"]
print(set(subj))

# figure out a way to store 9 & 9.0 as separate values in the set. 
# (You can take help of built-in data types) 
s={9,9.0}
print(s)        #it is storing only one value that is 9


# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
# an empty dictionary & add one by one. Use subject name as key & marks as value

a={}
a=int(input("enter marks"))
a=int(input("enter marks"))
a=int(input("enter marks"))
print(a)








