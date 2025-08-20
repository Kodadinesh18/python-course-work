class Book:
    def __init__(self, title, author, isbn):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        
    def get_masked_isbn(self):
        return "X" * (len(self.__isbn) - 4) + self.__isbn[-4:]
    
    def get_book_info(self):
        return f"{self.__title} by {self.__author} (ISBN: {self.get_masked_isbn()})"
    
class Borrowed(Book):
    def __init__(self, title, author, isbn, borrower_name, due_date):
        super().__init__(title, author, isbn)
        self.__borrower_name = borrower_name
        self.__due_date = due_date
    
    def get_borrow_info(self):
        return f"{super().get_book_info()}\nBorrower: {self.__borrower_name}\nDue Date: {self.__due_date}"
        
# Test
b1 = Borrowed("na saav nenu sastha", "Dinesh koda", "231123", "dinesh", "22/12/2023")
print(b1.get_borrow_info())
