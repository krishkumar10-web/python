# # # LIST
# # # A built-in data type that stores set of values
# # # It can store elements of different types (integer, float, string, etc).

myList = [1, "hello", 3.14, True]
print(myList)
print(type(myList))

# # List methods:

# # append(item): Adds an element to the end of the list.
myList.append("world")
print(myList)

# # insert(index, item)Inserts an element at a specific index.
myList.insert(1, "Python")
print(myList)

# # remove(item) Removes the first occurrence of the specified item.
myList.remove("hello")
print(myList)

# # pop(index): Removes and returns the element at the specified index. If no index is provided, removes the last element.
item = myList.pop(2)
print(myList)
print("Removed item:", item)

# # len(list): Returns the number of elements in the list.
print("Length of list:", len(myList))

# # sorted(list): Returns a new sorted list.
numbers = [3, 1, 4, 1, 5, 9, 2]
sorted_numbers = sorted(numbers)
print("Sorted list:", sorted_numbers)






# #  TUPLES IN PYTHON

# #  immutables
# #  eg of tuples
tup=()
tupe=(1,)


# tup.index( el )  #returns index of first occurrence
# tup.count( el )  #counts total occurrences 
tup = (2, 1, 3, 1)
print(tup.index(1))
print(tup.count(1)) 

# WAP to ask the user to enter names of their 3 favorite movies & store them in a list
movie = []
movie.append(input("Enter 1st favorite movie: "))
movie.append(input("Enter 2nd favorite movie: "))
movie.append(input("Enter 3rd favorite movie: "))
print(movie)

# WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)
# [1, 2, 3, 2, 1]
# [1, “abc”, “abc”, 1]
a=[1, 2, 3, 2, 1]
b=a.copy()
b.reverse()
if a==b:
    print("list is palindrome")
else:
    print("list is not palindrome")

# WAP to count the number of students with the “A” grade in the following tuple.
# [”C”, “D”, “A”, “A”, “B”, “B”, “A”]
# Store the above values in a list & sort them from “A” to “D”.

a=['C', 'D', 'A', 'A', 'B', 'B', 'A']
print(a.count("A"))
a.sort()
print(a)





