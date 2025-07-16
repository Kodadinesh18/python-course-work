print("Welcome to grocery store".center(50,"-"))

data={1:{"name":"Rice","price":60},2:{"name":"Wheat Flour","price": 45},3:{"name":"sugar","price":40},4:{"name":"Milk","price":25},5:{"name":"Eggs(12pcs)","price":70},
       6:{"name":"Cooking oil","price":130},
       7:{"name":"Tea Powder","price":90},8:{"name":"Salt","price":20},9:{"name":"Bread","price":30},10:{"name":"Soap","price":25}}

for i in range(1,len(data)):
    print(f"{i}.{data[i]['name']}-{data[i]['price']}")
    
items=list(map(int,input("Enter the product with indexes: ").split(",")))
print(items)
total=0
print("Selected items:")
for i in items:
    
    total+=data[i]["price"]
    print(f"{data[i]['name']}-{data[i]['price']}")
print(f"total amount:{total}")
    
    
