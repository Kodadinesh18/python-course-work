#1.Converting from int
int_a=5
print(float(int_a))#5.0
print(str(int_a))#'5'
print(bool(int_a))#True

#converting from float:
float_b=5.78
print(int(float_b))#5
print(str(float_b))
print(bool(float_b))#True

#converting from string:
str_c='12'
print(int(str_c))#12
print(list(str_c))#['1', '2']
print(tuple(str_c))#('1', '2')
print(set(str_c))#{'1', '2'}

#converting from tuple:
tup_d=(1,2,3,4)
print(str(tup_d))#(1, 2, 3, 4)
print(list(tup_d))#[1, 2, 3, 4]
print(set(tup_d))#{1, 2, 3, 4}

#converting from set:
set_e={3,4,5,6,7}
print(str(set_e))#{3, 4, 5, 6, 7}
print(list(set_e))#[3, 4, 5, 6, 7]
print(tuple(set_e))#(3, 4, 5, 6, 7)

#converting from dictionary:
dict_d={1:"dinesh",2:"Deepak",3:"Raju"}
print(list(dict_d))#[1,2,3]
#same as list we can also use in set and tuple but it only dispalys the key values 

#Dictionary conversiomn:
d = [('name', 'teja'), ('batch', '22'), ('subject', 'python')]
print(dict(d))#{'name': 'teja', 'batch': '22', 'subject': 'python'}


