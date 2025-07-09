#A dictionary in Python is an ordered, mutable collection that stores key-value pairs.

#Syntax of a Dictionary:
#dictionary_name = {key1: value1, key2: value2, key3: value3}

#creating a dictionary=
student={"name":"Dinesh koda","Age":21,"gender":"M"}
print(student)
#output:{'name': 'Dinesh koda', 'Age': 21, 'gender': 'M'}

#Accessing Values
print(student["name"])#Dinesh koda
print(student.get("name"))#->>most prefarable

#Adding and updating:
student["college"]="lendi"
print(student)
#output:{'name': 'Dinesh koda', 'Age': 21, 'gender': 'M', 'college': 'lendi'}

#removing items:
student.pop("Age")
print(student)
#removes last item:
student.popitem()
print(student)#{'name': 'Dinesh koda', 'gender': 'M'}
#clear:
student.clear()
print(student)#{}

#Dictionary Built-in Methods
student={"name":"Dinesh koda","Age":21,"gender":"M"}
print(student.keys())#dict_keys(['name', 'Age', 'gender'])
print(student.values())#dict_values(['Dinesh koda', 21, 'M'])
print(student.items())#dict_items([('name', 'Dinesh koda'), ('Age', 21), ('gender', 'M')])

#Dictionary Methods for Adding and Updating Data
print(student.update({
    "gender":"male","phone":347382
}))
print(student)#{'name': 'Dinesh koda', 'Age': 21, 'gender': 'male', 'phone': 347382}
student.setdefault("city","unknown")
print(student['city'])#unknown

#Dictionary Methods for Removing Data
#pop:
print(student.pop("Age"))