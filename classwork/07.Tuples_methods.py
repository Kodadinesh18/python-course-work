#A tuple is an immutable, ordered collection of elements.

# Empty Tuple
empty_tuple = ()
# Single-element Tuple (note the trailing comma)
single_tuple = (5,)
# Multi-element Tuple
my_tuple = (1, "apple", 3.5)
# Without parentheses (implicit tuple creation)
new_tuple=1,2,3
print(new_tuple)
print(type(new_tuple))#<class 'tuple'>

#2. Accessing Tuple Elements:
#positive indexing:
my_tuple = (10, 20, 30, 40)
print(my_tuple[2]) # Output: 30
#negative indexing
my_tuple = (10, 20, 30, 40)
print(my_tuple[-1]) # Output: 40

#Slicing:
print(my_tuple[0:2])#output:(10, 20)

#3. Operations on Tuples
tuple1=(1,2,3,4)
tuple2=("M","X","L","XL")
combined_tuple=tuple1+tuple2
print(combined_tuple)#output:(1, 2, 3, 4, 'M', 'X', 'L', 'XL')
#repetation:
print(tuple1*3)#output:(1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4)
#membership operator:
print(2 in tuple1)#True
#tuple unpacking:
a,b,c,d=tuple1
print(a,b,c,d)#1 2 3 4

#tuple-methods:
tuple33=1,2,3,4,4,34,2,2,2,4,2,2,4
print(tuple33)#output:(1, 2, 3, 4, 4, 34, 2, 2, 2, 4, 2, 2, 4)
#count:
print(tuple33.count(2))#6
#index:
print(tuple33.index(4))#3
#len:
print(len(tuple33))#13
#max:
print(max(tuple33))#34
print(min(tuple33))#1
#terable:
new_tup=tuple([1,2,3,54,3,5])
print(new_tup)#(1, 2, 3, 54, 3, 5)




