class Library:

    def __init__(self, list_of_books, name):
        self.booksList = list_of_books
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"we have the following books in pur library: {self.name}")
        for book in self.booksList:
            print(book)

    def lendBook(self, user, book)
        if book not in self.booksList
           print("Sorry, We dont have that book.")
        elif book in self.lendDict:
           print(f"The book is already being used by {self.lendDict[book]}")
        else:
            self.lendDict[book] = user
            print(
                "Lender-Book database has been updated.You can take the book now"
            )   
    def addBook(self, book)
        self.booksList.append(book)
        print(f"{book} has been added to the Book list")

    def returnBook(self , book)
        if book in self.lendDict
            del self.lendDict[book]
            print("Book Has been returned")
        else:
            print("That book wasn't borrowed from us")

if __name__ == '__main__':
    books = Library([
        'Python', 'Rich Dad Poor Dad', 'Harry Potter', 'C++ Basics', 'Algorithms by CLRS'
    ])