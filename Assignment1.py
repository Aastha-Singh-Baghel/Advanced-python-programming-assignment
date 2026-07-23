class Book:
    def __init__(self, title):
        self.title = title
        self.available = True
class Patron:
    def __init__(self, name):
        self.name = name
class Library:
    def __init__(self):
        self.books = []
        self.patrons = []
    def add_book(self):
        title = input("Enter book title: ")
        self.books.append(Book(title))
        print("Book added successfully!")
    def register_patron(self):
        name = input("Enter patron name: ")
        self.patrons.append(Patron(name))
        print("Patron registered successfully!")
    def borrow_book(self):
        name = input("Enter patron name: ")
        title = input("Enter book title: ")

        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                print(name, "borrowed", title)
                return

        print("Book is not available.")
    def return_book(self):
        title = input("Enter book title to return: ")

        for book in self.books:
            if book.title == title:
                book.available = True
                print("Book returned successfully!")
                return

        print("Book not found.")
    def display_books(self):
        if len(self.books) == 0:
            print("No books in library.")
        else:
            print("\nBooks in Library:")
            for book in self.books:
                if book.available:
                    status = "Available"
                else:
                    status = "Borrowed"
                print(book.title, "-", status)


library = Library()

while True:
    print("\n Library Management System ")
    print("1. Add Book")
    print("2. Register Patron")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Display Books")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        library.add_book()
    elif choice == 2:
        library.register_patron()
    elif choice == 3:
        library.borrow_book()
    elif choice == 4:
        library.return_book()
    elif choice == 5:
        library.display_books()
    elif choice == 6:
        print("Thank You!")
        break
    else:
        print("Invalid Choice!")