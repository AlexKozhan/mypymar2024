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
    """
    Represents a book.
    """
    def __init__(self, title, author, pages, isbn):
        """
        Initialize a Book object with its details.
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
            print(f"Book '{self.title}' is already "
                  f"reserved by user {self.current_user.name}.")
        else:
            self.is_reserved = True
            self.current_user = user
            print(f"Book '{self.title}' is "
                  f"reserved by user {user.name}.")

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
            print(f"Book '{self.title}' is taken "
                  f"by user {user.name}.")

    def return_book(self, user):
        """
        Return the book.
        """
        if self.current_user is None:
            print(f"Book '{self.title}' is not taken by anyone.")
        elif self.current_user != user:
            print(f"Book '{self.title}' cannot be"
                  f" returned by user {user.name} because "
                  f"it is taken by {self.current_user.name}.")
        else:
            print(f"Book '{self.title}' is returned "
                  f"by user {self.current_user.name}.")
            self.current_user = None
            self.is_reserved = False


class User:
    """
    Represents a user.
    """
    def __init__(self, name):
        """
        Initialize a User object with its name.
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

    @staticmethod
    def return_book(book, user):
        """
        Return a book.
        """
        book.return_book(user)


book1 = Book("White Fang", "Jack "
                           "London", 100, "1234567890")
book2 = Book("Animals", "Ivan "
                        "Ivanov", 101, "2232442")

user1 = User("Alex")
user2 = User("Siarhei")

user1.reserve_book(book1)
user2.reserve_book(book2)

user2.take_book(book1)
user1.take_book(book2)

User.return_book(book1, user1)
User.return_book(book2, user2)
User.return_book(book1, user2)
