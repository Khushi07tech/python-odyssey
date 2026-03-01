class Book:

    def __init__(self, title, author, isbn, is_available):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = is_available

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def borrow (self):
        if self.is_available:
            self.is_available = False
            print (f"You borrowed '{self.title}'")
        else:
            print (f"'{self.title}' is already borrowed")

    def return_book (self):
        if self.is_available:
            print (f"'{self.title}' is already on the shelf.")
        else:
            print (f"Thank you for returning '{self.title}'")
            self.is_available = True

    def get_info (self):
        print ("*" * 20)
        print (self.title)
        print (self.author)
        print (self.isbn)
        print ("*" * 20)

book1  = Book("1984", "George Orwell", 9780451524935, True)
book2  = Book("To Kill a Mockingbird", "Harper Lee", 9780061120084, True)
book3  = Book("The Great Gatsby", "F. Scott Fitzgerald", 9780743273565, False)
book4  = Book("Pride and Prejudice", "Jane Austen", 9780141439518, True)
book5  = Book("The Catcher in the Rye", "J.D. Salinger", 9780316769488, True)
book6  = Book("Brave New World", "Aldous Huxley", 9780060850524, False)
book7  = Book("The Alchemist", "Paulo Coelho", 9780061122415, True)
book8  = Book("The Kite Runner", "Khaled Hosseini", 9781594631931, True)
book9  = Book("Animal Farm", "George Orwell", 9780451526342, False)
book10 = Book("Little Women", "Louisa May Alcott", 9780147514011, True)
book11 = Book("Jane Eyre", "Charlotte Brontë", 9780141441146, True)
book12 = Book("Wuthering Heights", "Emily Brontë", 9780141439556, False)
book13 = Book("The Book Thief", "Markus Zusak", 9780375842207, True)
book14 = Book("Fahrenheit 451", "Ray Bradbury", 9781451673319, True)
book15 = Book("Crime and Punishment", "Fyodor Dostoevsky", 9780140449136, False)
book16 = Book("The Hobbit", "J.R.R. Tolkien", 9780547928227, True)
book17 = Book("Moby-Dick", "Herman Melville", 9780142437247, False)
book18 = Book("The Odyssey", "Homer", 9780140268867, True)
book19 = Book("Dracula", "Bram Stoker", 9780141439846, True)
book20 = Book("The Stranger", "Albert Camus", 9780679720201, False)

class Library:
    total_books = 0

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        Library.total_books += 1

    def show_available_books(self):
        for book in self.books:
            if book.is_available:
                print(book)


    def find_book_by_title(self, title):
        for book in self.books:
            if title.strip().title() == book.title.strip().title():
                return book
        return None

    def show_borrowed_books(self):
        print ("*" * 30)
        print("BORROWED BOOKS:")
        for book in self.books:
            if not book.is_available:
                print(book)

books = [book1, book2, book3, book4, book5,
         book6, book7, book8, book9, book10,
         book11, book12, book13, book14, book15,
         book16, book17, book18, book19, book20, ]

library1 = Library ()
for book in books:
    library1.add_book(book)

def main():
    name = input ("Name: ").title()
    print (f"Welcome {name}!")
    is_running = True

    while is_running:
        print ("-----Echo Library-----")
        print ("1. Borrow")
        print ("2. Return")
        print ("3. Get info")
        print ("4. Show available books")
        print ("5. Find book by title")
        print ("6. Show borrowed books")
        print ("7. Add book")
        print ("8. Exit")
        choice = int(input("Enter (1-8): "))

        if choice == 1:
            title = input ("Enter the book title: ")
            book = library1.find_book_by_title(title)

            if book :
                book.borrow()
            else:
                print ("Book not found")

        elif choice == 2:
            title = input("Enter the book title: ")
            book = library1.find_book_by_title(title)

            if book:
                book.return_book()
            else:
                print ("Book not found")

        elif choice == 3:
            title = input("Enter the book title: ")
            book = library1.find_book_by_title(title)

            if book:
                book.get_info()
            else:
                print ("Book not found")

        elif choice == 4:
            library1.show_available_books()

        elif choice == 5:
            title = input("Enter the book title: ")
            book = library1.find_book_by_title(title)

            if book:
                print(book)
            else:
                print ("Book not found")

        elif choice == 6:
            library1.show_borrowed_books()

        elif choice == 7:
            title = input ("Enter a title: ").strip().title()
            existing_book = library1.find_book_by_title(title)

            if existing_book:
                print (f"{existing_book} is already found")
            else:
                author = input ("Enter author's name: ").title()
                isbn = input ("Enter isbn: ")
                if not isbn:
                    isbn = Library.total_books + 100000000
                else:
                    isbn = int (isbn)
                new_book = Book (title, author, isbn, True)
                library1.add_book(new_book)
                print (f"'{title}' added to the library.")

        elif choice == 8:
            is_running = False

        else:
            print ("Invalid")

    print ("Thank You!")

if __name__ == '__main__':
    main ()