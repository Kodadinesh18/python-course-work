from abc import ABC,abstractmethod

class order(ABC):
    @abstractmethod
    def process_order(self):
        pass
class foodorder(order):
    def process_order(self):
        print("Processing FOod order:check chief availabilty,estimate time")
        
class GroceryOrder(order):
    def process_order(self):
        print("processing Grocery order: check inventory")

class MedicineOrder(order):
    def process_order(self):
        print("processing medicine order: valididate prescription, assign secure ")

class cloudkitchen(order):
    def process_order(self):
        print("processing cloud kitchen order")
        
class cakeorder(order):
    def process_order(self):
        print("processing cake order!")

class partyorder(order):
    def process_order(self):
        print("processing party order!")

class juiceorder(order):
    def process_order(self):
        print("processing juice order!")

def handle_order(order):
    order.process_order()

orders=[
    foodorder(),
    GroceryOrder(),
    MedicineOrder(),
    cloudkitchen(),
    cakeorder(),
    partyorder(),
    juiceorder()
]

for order in orders:
    handle_order(order)
