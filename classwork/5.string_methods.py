#Strings are immutable, meaning once created, they cannot be changed.
# Defining strings
str1='hello'
str2="Dinesh"
str3='''I joined python full stack
in code gnan at ameerpet.
'''
print(str1)
print(str2)
print(str3)

'''output:
hello
Dinesh
I joined python full stack
in code gnan at ameerpet
'''

#Operations on Strings

#1. Concatenation (+)
print(str1+" "+str2)
#output: hello dinesh

#2. Repetition (*)
print("Dinesh "*3)
#output:Dinesh Dinesh Dinesh

#3. Indexing
text="animals are in the zoo"
print(text[0])#a
print(text[-1])#0

#4. Slicing
print(text[0:7])#animals
print(text[-1:-4:-1])#ooz

#5. Membership (in, not in)
print("animals" in text)#True
print("zebra" in text)#False

#Built-in String Functions
#1. len() -
print(len(str1))#5

#2. max() / min() -
print(min(str2))#D
print(max(str2))#s

#3. sorted() -
print(sorted(str1))#['e', 'h', 'l', 'l', 'o']

#4. chr() / ord() -
print(chr(97))#a
print(ord("a"))#97

#1. Case Conversion Methods
str4= "Codegnan is at Ameerpet"
print(str4)#Codegnan is at Ameerpet

#upper():
print(str4.upper())#CODEGNAN IS AT AMEERPET
#lower():
print(str4.lower())#codegnan is at ameerpet
#capitalize():
print(str4.capitalize())#Codegnan is at ameerpet
#title():
print(str4.title())#Codegnan Is At Ameerpet
#swapcase():
print(str4.swapcase())#cODEGNAN IS AT aMEERPET

#2. Alignment & Formatting Methods

str5="python"

#center(width,fillchar):
print(str5.center(10,"*"))#**python**
#ljust(width,fillchar):
print(str5.ljust(12,'&'))#python&&&&&&
#rjust(width,fillchar):
print(str5.rjust(12,'^'))#^^^^^^python
#zfill(width):
print("543".zfill(5))#00543

#3. Search & Find Methods
str6="hello gullyls"

#find(sub)
print(str6.find('l'))#2
#rfind(sub):
print(str6.rfind('l'))#11
#index()-Like find(), but raises an error if not found.
print(str6.rfind('j'))#-1
#count():
print(str6.count('l'))#5

#4. String Testing Methods (Boolean Results):
str7='python'
print(str7.startswith('p'))#True
print(str7.endswith('.'))#False
str8='pythonfullstack30'
print(str8.isalpha())#false
print(str8.isalnum())#True
print(str7.islower())#true
print(str8.isupper())#false
str9="    "
print(str9.isspace())#True
print("Hello World".istitle())#True
print("variable1".isidentifier())#True

'''isdecimal() → Most strict; only base-10 digits ('0'–'9' and
equivalents)
● isdigit() → Allows additional digit characters like superscripts
● isnumeric() → Most flexible; includes digits, fractions, Roman
numerals, etc.'''

#5. Replace & Modify Methods
#replace(old,new):
print("Apple".replace("p","b"))#Abble

#translate(table)
print("abc".translate(str.maketrans("a", "x")))#xbc

#6.Splitting & Joining Methods
str9="a,b,c,d,e"
#split(sep):
print(str9.split())#['a,b,c,d,e']
#rsplit():
print(str9.rsplit())#['a,b,c,d,e']
#splitlines()
str10='''
my name is 
dinesh koda 
i am from 
visakhaptanam'''
print(str10.splitlines())
#output:['', 'my name is ', 'dinesh koda ', 'i am from ', 'visakhaptanam']

#join(iterable)
print("-".join(["Hello", "World"]))#Hello-World

#partition(sep):
print("apple-pie-like-me".partition("-"))
#output:Splits into a 3 tuple
#('apple', '-', 'pie-like-me')

#7. Whitespace & Trimming Methods
#strip(chars)
str11="   my world   "
print(str11.strip())#my world
#lstrip(chars)
print(str11.lstrip())
#rstrip(chars)
print(str11.rstrip())











