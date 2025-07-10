'''A list in Python is a built-in data structure that allows storing multiple values in a single
variable. Lists are ordered, mutable, and allow duplicate elements.'''

#Creating Lists:
mylist1=[]# Empty list
mylist2=list()# Using list() constructor

#List with Elements
numbers = [1, 2, 3, 4, 5] # List of integers
fruits = ["apple", "banana", "cherry"] # List of strings
mixed = [10, "Python", 3.14, True] # Mixed data types

#list with nested list:
nested_list=[["a","b","c"],[1,2,3],[True,False]]

#4 List using list() Constructor
list_tuple=list((1,2,3,4,5))
print(type(list_tuple))#<class 'list'>


#3. Accessing Elements in a List
#Using Indexing (Positive & Negative)
my_list=["dinesh","deepak"]
print(my_list[0])#dinesh
print(my_list[-1])#deepak

#Using Slicing
my_list1=[1,2,3,45,2,45,2]
print(my_list1[0:5])#[1, 2, 3, 45, 2]
print(my_list1[::-1])#Reverse list
print(my_list1[-3:-1])#[2,45]

#Modifying Lists
#Changing Elements
numbers = [10, 20, 30, 40]
numbers[3]=100
print(numbers)#[10, 20, 30, 100]

#Adding elements:
# Append (adds to the end)
numbers.append(90)

# Insert (adds at a specific position)
numbers.insert(1, 15)

# Extend (adds multiple elements)
numbers.extend([60, 70, 80])

print(numbers) #[10, 15, 20, 30, 100, 90, 60, 70, 80]

#Removing Elements
numbers.remove(100) # Removes first occurrence of 100
numbers.pop(2) # Removes element at index 2
numbers.pop() # Removes last element
del numbers[1] # Deletes element at index 1
numbers.clear() # Clears the entire list

#5. List Methods

numbers = [10, 20, 30, 40]
#index:
print(numbers.index(20))#1
numbers.extend([10,20,30,30,50,0,None])
print(numbers)
#count:
print(numbers.count(10))#2

print(numbers)
arr2=numbers.copy()#[50, 40, 30, 30, 30, 20, 20, 10, 10]
print(arr2)
print(any(numbers))#True
print(all(numbers))#False