"""
Создайте класс book с именем книги, автором,
кол-м страниц, ISBN, флагом, зарезервирована ли
книги или нет. Создайте класс пользователь который
может брать книгу, возвращать, бронировать. Если
другой пользователь хочет взять зарезервированную
книгу(или которую уже кто-то читает - надо ему про
это сказать).
"""


class Book:
    def set_details(self, title, author, pages, isbn):
        """
        Set details of the book.
        """
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.is_reserved = False
        self.current_user = None

    def reserve(self, user):
        """
        Reserve the book by a user.
        """
        if self.is_reserved:
            print(f"Book '{self.title}' is "
                  f"already reserved by user "
                  f"{self.current_user.name}.")
        else:
            self.is_reserved = True
            self.current_user = user
            print(f"Book '{self.title}' is reserved "
                  f"by user {user.name}.")

    def take(self, user):
        """
        Take the book by a user.
        """
        if self.is_reserved and self.current_user != user:
            print(f"Book '{self.title}' is already "
                  f"reserved by user {self.current_user.name}.")
        elif self.current_user is not None:
            print(f"Book '{self.title}' is already "
                  f"taken by user {self.current_user.name}.")
        else:
            self.current_user = user
            self.is_reserved = False
            print(f"Book '{self.title}' is taken by user {user.name}.")

    def return_book(self):
        """Return the book."""
        if self.current_user is None:
            print(f"Book '{self.title}' is not taken by anyone.")
        else:
            print(f"Book '{self.title}' is returned "
                  f"by user {self.current_user.name}.")
            self.current_user = None
            self.is_reserved = False


class User:
    def set_details(self, name):
        """
        Set details of the user.
        """
        self.name = name

    def reserve_book(self, book):
        """
        Reserve a book.
        """
        book.reserve(self)

    def take_book(self, book):
        """
        Take a book.
        """
        book.take(self)

    def return_book(self, book):
        """
        Return a book.
        """
        book.return_book()


book1 = Book()
book1.set_details("White fang", "Jack London",
                  100, "1234567890")
book2 = Book()
book2.set_details("Animals",
                  "Ivan Ivanov", 101,
                  "2232442")

user1 = User()
user1.set_details("Alex")
user2 = User()
user2.set_details("Siarhei")

user1.reserve_book(book1)
user2.reserve_book(book2)

user2.take_book(book1)
user1.take_book(book2)

user1.return_book(book1)
user2.return_book(book2)
